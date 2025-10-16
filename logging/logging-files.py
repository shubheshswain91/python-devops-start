import logging
import os
import logging.handlers
import time

# Basic logging with FileHandler
print("basic logging with FileHandler")
print("-------------------------------\n")

basic_logger = logging.getLogger("file.basic")
basic_logger.setLevel(logging.DEBUG)

basic_fh = logging.FileHandler(
    "basicFile.log", delay=True, encoding="utf-8"
    )
basic_fh.setLevel(logging.INFO)
basic_logger.addHandler(basic_fh)

basic_logger.info("INFO: will be written to file")

# Size-based log rotation with RotatingFileHandler
print("\nsize-based log rotation with RotatingFileHandler")
print("---------------------------------\n")

rotating_logs_filename = "rotatingfile.log"

for file_name in os.listdir("."):
    if file_name .startswith(rotating_logs_filename):
        os.remove(file_name)

rotatting_logger = logging.getLogger("file.rotating")
rotatting_logger.setLevel(logging.DEBUG)

rotatting_fh = logging.handlers.RotatingFileHandler(
    rotating_logs_filename, 
    maxBytes=500, 
    backupCount=2,
    encoding="utf-8"
    )

rotatting_fh.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))

for i in range(30):
    rotatting_logger.info(f"Entry {i}: {'Z' * 50}")
    time.sleep(0.05)

# Time-based log rotation with TimedRotatingFileHandler
