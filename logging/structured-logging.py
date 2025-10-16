# Configuring python-json-logger
print("Configuring python-json-logger")
print("------------------------------\n")


from pythonjsonlogger.json import JsonFormatter
import logging 
import sys

json_logger = logging.getLogger("demo.json")
json_logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
json_formatter = JsonFormatter(
    "{asctime} {levelname} {message}", 
    style='{', 
    json_indent=4,
    rename_fields={"asctime": "timestamp", "levelname": "log_level", "message": "log_message"}

)

handler.setFormatter(json_formatter)

json_logger.addHandler(handler)
json_logger.info("Structured logging initialized")

# Logging with extra context

# Logging exceptions as JSON
