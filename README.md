# Syslog Analyzer

A final project for a Linux course.  
This project collects and analyzes system log messages (`/var/log/syslog`) from an AWS EC2 server and generates a CSV report with useful statistics.

## 🧠 What It Does

- Reads log entries from the EC2 server's syslog file
- Filters and counts messages by severity level: `INFO`, `WARNING`, and `ERROR`
- Adds a timestamp indicating when the report was generated
- Saves the summary as a local file on the server
- Transfers the result file to the client machine using `scp`
- Appends a new row to a local CSV file (`log_report.csv`) on the client

## 📁 Project Structure

- **Server script (on EC2)**  
  `logs_analysis.py`: Parses the syslog file and generates a summary output.

- **Client script (on local machine)**  
  `client_side.py`: Connects to the EC2 instance via SSH, retrieves the summary file, and updates a local CSV log report. It uses credentials loaded from a `.env` file.

## 🔧 Technologies Used

- Python
- Linux (syslog)
- AWS EC2
- SSH / SCP
- CSV file handling
- `dotenv` (for secure credential management)

## 🚀 How to Run

### On the EC2 server:

Ensure that `logs_analysis.py` exists and is executable.

### On the local machine:

1. Create a `.env` file with the following variables:

   ```ini
   PEM_FILE_PATH=C:/path/to/your/key.pem
   HOST=your.ec2.host.ip
   USERNAME=ubuntu

   ```

2. Run `client_side.py` to:

- Connect to the EC2 instance
- Fetch the result file
- Append the new data to `log_report.csv`

### Example CSV Output:

| Timestamp  | INFO | WARNING | ERROR |
| ---------- | ---- | ------- | ----- |
| 1743880919 | 245  | 12      | 3     |
| 1743881040 | 198  | 9       | 1     |
