# Devops_internship_assignment

# Log File Monitoring and Analysis

## Introduction
This Python script continuously monitors a specified log file for new entries and performs real time analysis on log entries. It counts occurrences of specific keywords or patterns (e.g., error messages, HTTP status codes) and generates summary reports.

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
we can test the script by running it and adding new entries to the log file. now check if the script correctly prints the new entries and counts the keywords.

## Dependencies
No external dependencies are required to run this script.

![alt text](Result/result.png)

## Note
In this, the total counts of each keyword will be printed when Ctrl+C is pressed. Also, whenever a new message containing one of the keywords is found, it will be printed immediately with a prefix indicating the type of the message. This should make it easier to spot new error messages. Please note that this code will only work if it’s run in a console that supports Ctrl+C interrupt signal. If you’re running this code in an environment that doesn’t support Ctrl+C, you might need to find another way to send an interrupt signal to the script. The script is now more robust and efficient with the use of defaultdict for counting keywords and improved error handling.


#log_file.log contains that the dummy logs that was generated from the dummy_log.py python script.




