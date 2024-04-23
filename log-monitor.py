import logging
import time
import os
import signal
import sys
import random
from collections import defaultdict

# Configure logging
logging.basicConfig(filename='./log_file.log', level=logging.DEBUG)

# Create a logger
logger = logging.getLogger(__name__)

# Define keywords or patterns to look for
keywords = ['ERROR', 'DEBUG', 'INFO']

# Define a flag for the monitoring loop
running = True

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

# Define a handler for the interrupt signal
def handler(signum, frame):
    global running
    running = False
    # Print the keyword counts when Ctrl+C is pressed
    print("Total counts:")
    for keyword, count in counts.items():
        print(f'{keyword}: {count}')

# Set the signal handler
signal.signal(signal.SIGINT, handler)

# Initialize a dictionary to store keyword counts
counts = defaultdict(int)

# Get the size of the log file
size = os.stat('log_file.log').st_size

# Open the log file
with open('log_file.log', 'r') as f:
    # Move to the end of the file
    f.seek(size)

    # Start the monitoring loop
    while running:
        try:
            # Randomly select a log level
            log_level = random.choice(log_levels)
            # Get the log message format for the selected log level
            log_message = formats[log_level]
            # Log the message
            logger.log(log_level, log_message)
            # Sleep for a short interval
            time.sleep(1)
        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C)
            print("\nLogging interrupted. Exiting.")
            break

        # Read the next line
        line = f.readline()

        # If the line is not empty, process it
        if line:
            # Check each keyword
            for keyword in keywords:
                # If the keyword is found in the line, increment the count
                if keyword in line:
                    counts[keyword] += 1
                    print(f'New {keyword} message:')
                    print(line)
                    break

        # If the line is empty, sleep for a short interval
        else:
            time.sleep(1)
