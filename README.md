# Syslog Analyzer

A final project for a Linux course.  
This project collects and analyzes system log messages (`/var/log/syslog`) from an AWS EC2 server and generates a CSV report with useful statistics.

## 🧠 What It Does

- Reads log lines from the EC2 server's syslog file
- Filters and counts messages based on severity: `INFO`, `WARNING`, and `ERROR`
- Adds a timestamp for when the report was created
- Saves the summary as a local file on the server
- The client machine downloads the result using `scp`
- The client updates a local CSV file (`log_report.csv`) by adding a new row

## 📁 Project Structure

- **Server script (on EC2)**  
  Parses the syslog file and creates a summary result file.

- **Client script (local)**  
  Connects to the EC2 server using `SSH` + `scp`, downloads the result, and updates the CSV.

## 🔧 Technologies Used

- Python
- Linux syslog
- AWS EC2
- SSH and SCP
- CSV file handling

## 🚀 How to Run

1. Run the script on the EC2 server to create the log summary
2. From the local machine, run the client script to download the result via `scp`
3. The local script appends a new row to the CSV file

## 📌 Example Output (CSV)

| Timestamp           | INFO | WARNING | ERROR |
| ------------------- | ---- | ------- | ----- |
| 2025-04-05 12:34:00 | 245  | 12      | 3     |
| 2025-04-05 13:20:15 | 198  | 9       | 1     |
