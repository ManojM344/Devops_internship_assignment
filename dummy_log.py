import logging
import time
import random

# Configure logging
logging.basicConfig(filename='log_file.log', level=logging.DEBUG)

# Create a logger
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.ERROR: "ERROR message",
    404: "HTTP 404 Not Found",
    500: "HTTP 500 Internal Server Error",
    403: "HTTP 403 Forbidden",
    400: "HTTP 400 Bad Request",
    logging.INFO: "INFO message", 
    logging.DEBUG: "DEBUG message",
}

# Define log levels to cycle through
log_levels = [logging.ERROR, logging.DEBUG, logging.INFO, 404, 500, 403, 400]

# Main loop to log messages
for _ in range(100):  # Generate 100 log entries
    # Randomly select a log level
    log_level = random.choice(log_levels)
    # Get the log message format for the selected log level
    log_message = formats[log_level]
    # Log the message
    if log_level == logging.ERROR:
        logger.log(log_level, log_message)
    else:
        logger.log(logging.ERROR, log_message)
    # Sleep for a short interval
    time.sleep(3)
