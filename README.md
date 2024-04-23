# Devops_internship_assignment

# Log File Monitoring and Analysis

## Introduction
This Python script continuously monitors a specified log file for new entries and performs basic analysis on log entries. It counts occurrences of specific keywords or patterns (e.g., error messages, HTTP status codes) and generates summary reports.

## Requirements
- Python 3.x
- Access to a log file

## Usage
1. Configure the logging settings at the beginning of the script. Set the filename to the path of your log file.
2. Define the keywords or patterns you want to monitor in the `keywords` list.
3. Run the script in a console that supports `Ctrl+C` interrupt signal. The script will start monitoring the log file and print new entries containing the keywords in real time.
4. Press `Ctrl+C` to stop the monitoring loop. The script will print the total counts of each keyword.

## Features
- Real-time log file monitoring
- Keyword counting
- Summary report generation
- `Ctrl+C` interrupt signal handling

## Error Handling
The script includes basic error handling. If an error occurs during the execution of the script, it will be logged and the script will continue running. If the script is interrupted by a `Ctrl+C` signal, it will print the total counts of each keyword and exit gracefully.

## Testing
You can test the script by running it and adding new entries to the log file. Check if the script correctly prints the new entries and counts the keywords.

## Dependencies
No external dependencies are required to run this script.

## Note
This is a basic implementation and there are many ways to enhance this script, such as adding more advanced log analysis features, improving error handling, or making the script more robust and efficient.
