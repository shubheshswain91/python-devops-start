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

print("\nLogging with extra context")
print("------------------------------\n")

extra_context = {
    "context_data": {
        "user_id": 123, 
        "session_id": "abc123",
        "source_ip": "10.0.0.5"

    }
    
}

json_logger.warning(
    "Request took longer than 5s to complete", 
    extra=extra_context)


# Logging exceptions as JSON

print("\nLogging exceptions as JSON")
print("------------------------------\n")

try:
    result = 1 / 0
except ZeroDivisionError:
    json_logger.exception(
        "ZeroDivisionError occurred",
        extra={"operation": "divide", "value": 0})    
