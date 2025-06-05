import json
import threading
import socket
import logging
import subprocess
import re
import platform
from functools import lru_cache

logging.basicConfig(filename='server.log', level=logging.DEBUG)

# Import your models (unchanged)
from Models.CheckUp import CheckUp
from Models.Doctor import Doctor
from Models.LaboratoryTest import Laboratory
from Models.Patient import Patient
from Models.Prescription import Prescription
from Models.Staff import Staff
from Models.Transaction import Transaction

DB_CONFIG = {
    "host": "localhost",
    "database": "ClinicSystem",
    "user": "postgres",
    "password": "sphinxclub012"
}

# Socket server setup
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5432

# Admin MAC address (replace with your actual admin MAC)
ADMIN_MAC_ADDRESS = "74:04:f1:4e:e6:02"  # From your ipconfig output


class SocketServer:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.running = False
        self.server_thread = None
        self.admin_mac = ADMIN_MAC_ADDRESS.lower()

    @staticmethod
    @lru_cache(maxsize=32)  # Cache MAC lookups for performance
    def get_mac_from_ip(ip_address):
        """Get MAC address for a given IP using ARP"""
        try:
            if platform.system() == "Windows":
                # Windows ARP command
                arp_output = subprocess.check_output(["arp", "-a", ip_address]).decode('utf-8', errors='ignore')
                mac_match = re.search(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", arp_output)
            else:
                # Linux/Mac OS ARP command
                arp_output = subprocess.check_output(["arp", "-n", ip_address]).decode('utf-8', errors='ignore')
                mac_match = re.search(r"(([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2}))", arp_output)

            if mac_match:
                return mac_match.group(0).lower().replace('-', ':')  # Normalize format
            return None
        except Exception as e:
            logging.warning(f"Could not get MAC for {ip_address}: {str(e)}")
            return None

    def is_admin_connection(self, ip_address):
        """Check if connection is from admin device by MAC address"""
        if not ip_address:
            return False

        client_mac = self.get_mac_from_ip(ip_address)
        if not client_mac:
            return False

        return client_mac == self.admin_mac

    def handle_doctor_staff(self, connection, address):
        ip, port = address
        is_admin = self.is_admin_connection(ip)

        print(f"Connected by {address} (Admin: {is_admin})")
        logging.info(f"Connection from {address} (Admin: {is_admin})")

        db_methods = {
            # PATIENTS
            "CREATE_PATIENT": Patient.create_new_patient,
            "GET_PATIENT_BY_ID": Patient.get_patient_details,
            "GET_ALL_PATIENT": Patient.get_all_patients,
            "GET_PATIENT_ID": Patient.get_patient_id,
            "GET_PATIENT_DETAILS": Patient.get_patient_details,

            # DOCTOR
            "GET_DOCTOR": Doctor.get_doctor,

            # STAFF
            "GET_STAFF": Staff.get_staff,

            # CHECKUPS
            "CREATE_CHECKUP": CheckUp.save_checkup,
            "GET_CHECKUP_DETAILS": CheckUp.get_checkup_details,
            "GET_NEXT_SEQUENCE_NUMBER": CheckUp.get_next_sequence_number,
            "GET_TEST_BY_CHECK_ID": CheckUp.get_test_by_check_id,
            "GET_CHECKUP_BY_PAT_ID": CheckUp.get_checkup_by_pat_id,
            "GET_ALL_CHECKUP": CheckUp.get_all_checkup,
            "GET_PENDING_CHECKUP": CheckUp.get_pending_checkups,

            # TRANSACTIONS
            "CREATE_TRANSACTION": Transaction.add_transaction,
            "GET_ALL_TRANSACTION": Transaction.get_all_transaction,
            "GET_TRANSACTION_BY_PAT_ID": Transaction.get_transaction_by_patient,
            "GET_TRANSACTION_BY_ID": Transaction.get_transaction_by_id,

            # PRESCRIPTIONS
            "CREATE_PRESCRIPTION": Prescription.add_presscription,
            "GET_PRESCRIPTION_BY_CHECKUP": Prescription.get_prescription,

            # LABORATORY TESTS
            "GET_LAB_TEST": Laboratory.get_lab_test,
            "GET_TEST_BY_LAB_CODE": Laboratory.get_test_by_lab_code,
            "GET_ALL_TEST": Laboratory.get_all_test,
        }

        # Admin-only methods (extend as needed)
        admin_methods = {
            "DELETE_PATIENT": Patient.delete_patient,
            "UPDATE_SYSTEM_CONFIG": None,  # Add your admin methods here
        }

        try:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                logging.debug(f"Received: {data.decode()}")

                raw_data = data.decode().strip()
                if not raw_data:
                    break

                command = None
                try:
                    # Parse the incoming command
                    parts = raw_data.split(maxsplit=1)
                    command = parts[0]
                    args_str = parts[1] if len(parts) > 1 else ""

                    # Check if command is admin-only
                    if command in admin_methods and not is_admin:
                        raise PermissionError("Admin privileges required for this command")

                    # Combine regular and admin methods
                    all_methods = {**db_methods, **admin_methods}

                    if command not in all_methods:
                        raise ValueError(f"Invalid command: {command}")

                    method = all_methods[command]

                    # Handle different method types
                    if command.startswith(("CREATE_", "ADD_", "UPDATE_", "DELETE_")):
                        try:
                            kwargs = json.loads(args_str) if args_str else {}
                            result = method(**kwargs)
                        except json.JSONDecodeError:
                            raise ValueError("Invalid JSON data for this method")
                    else:
                        if args_str:
                            if "," in args_str:
                                args = [arg.strip() for arg in args_str.split(",")]
                            else:
                                args = [args_str]
                            result = method(*args)
                        else:
                            result = method()

                    # Send response
                    response = {"status": "success", "data": result, "is_admin": is_admin}
                    connection.sendall(json.dumps(response).encode())

                except PermissionError as e:
                    error_msg = f"Permission denied: {str(e)}"
                    logging.warning(f"Admin attempt failed from {ip}: {error_msg}")
                    connection.sendall(json.dumps({
                        "status": "error",
                        "message": error_msg,
                        "code": "PERMISSION_DENIED"
                    }).encode())
                except Exception as e:
                    error_msg = f"Error processing {command}: {str(e)}"
                    print(error_msg)
                    connection.sendall(json.dumps({
                        "status": "error",
                        "message": error_msg
                    }).encode())

        except Exception as e:
            print(f"Connection error: {str(e)}")
            logging.error(f"Error with {ip}: {e}")
        finally:
            connection.close()

    def _run_server(self):
        """Main server loop"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(5)
            print(f"Socket server running on {self.host}:{self.port}")

            while self.running:
                conn, addr = s.accept()
                client_thread = threading.Thread(
                    target=self.handle_doctor_staff,
                    args=(conn, addr),
                    daemon=True
                )
                client_thread.start()

    def start(self):
        """Start the socket server in a background thread"""
        if not self.running:
            self.running = True
            self.server_thread = threading.Thread(
                target=self._run_server,
                daemon=True
            )
            self.server_thread.start()

    def stop(self):
        """Stop the server gracefully"""
        if self.running:
            self.running = False
            # Unblock the accept() call with a dummy connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
            self.server_thread.join(timeout=1)