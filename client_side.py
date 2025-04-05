from dotenv import load_dotenv
from SshToServer import SshToServer
import pandas as pd
import os
import ast

load_dotenv()

def create_ssh_client():
    """Creates an SSH client using the credentials from the .env file."""
    pem_file_path = os.getenv("PEM_FILE_PATH")
    host = os.getenv("HOST")
    return SshToServer(pem_file_path, host, "ubuntu")

def append_to_csv(file_path, data):
    """Appends data to a CSV file, creating it if it doesn't exist."""
    df_new = pd.DataFrame([data])
    if os.path.isfile(file_path):
        df_existing = pd.read_csv(file_path)
        df_new = pd.concat([df_existing, df_new], ignore_index=True)
    df_new.to_csv(file_path, index=True)

def fetch_and_process_syslog_data():
    """Fetches syslog data from remote server and processes it."""
    try:
        my_ssh = create_ssh_client()  # Create the SSH client
        stdout, stderr = my_ssh.runRemoteCommand("python3 logs_analysis.py")  # Run the remote command

        if stdout:
            syslog_data = ast.literal_eval(stdout.strip())  
            csv_file_path = "syslog_analysis.csv"
            append_to_csv(csv_file_path, syslog_data)
        else:
            print(f"Error running command: {stderr}")
    except Exception as e:
        print(f"Error processing syslog data: {e}")


fetch_and_process_syslog_data()
