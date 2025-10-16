import logging
import os
import logging.handlers
import time


def cleanup_log_files(base_name: str):
    for file_name in os.listdir("."):
        if file_name.startswith(base_name):
            os.remove(file_name) 

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

cleanup_log_files(rotating_logs_filename)

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

print("\ntime-based log rotation with TimedRotatingFileHandler")
print("---------------------------------\n")

timed_rotating_logs_filename = "timedrotatingfile.log"

cleanup_log_files(timed_rotating_logs_filename)

timed_rotating_logger = logging.getLogger("file.timed")
timed_rotating_logger.setLevel(logging.DEBUG)

timed_rotating_fh = logging.handlers.TimedRotatingFileHandler(
    timed_rotating_logs_filename, 
    when="S", 
    backupCount=2,
    encoding="utf-8"
    )

timed_rotating_fh.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))

timed_rotating_logger.addHandler(timed_rotating_fh)

for i in range(30):
    timed_rotating_logger.info(f"Entry {i}: {'Z' * 50}")
    time.sleep(0.5)
