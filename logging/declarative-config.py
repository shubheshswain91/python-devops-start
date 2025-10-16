import logging  
import logging.config
import os
from pathlib import Path
from typing import Dict, Any
import json

""" 
# Uncomment the following lines to test INI-based logging

# Declarative logging configuration - INI-file
print("Declarative logging configuration - INI-file")
print("----------------------------------------\n")


#print(os.getcwd() + '\\logging\\declarative-config.ini')  # Adjust the path as needed  
base_dir = Path(__file__).parent
config_path = base_dir / "declarative-config.ini"

# print(f"Loading logging config from: {config_path}")
# print(config_path.exists())  # Should print True


# print(f"If file present in the dir: ", os.path.isfile(config_path))
logging.config.fileConfig(
    fname=config_path
    )

app_logger = logging.getLogger("application")
app_logger.debug("INI-style fileConfig is working!") """

""" 
# Uncomment the following lines to test dict-based logging
# Declarative logging configuration - Dictionary config

print("Declarative logging configuration - Dictionary config")
print("----------------------------------------\n")

dict_config:Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": " %(levelname)8s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple"
        }
    },
    "loggers": {
        "config.dict": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False   
        }
    }
}                

logging.config.dictConfig(dict_config)
config_logger = logging.getLogger("config.dict")
config_logger.debug("Dictionary-style dictConfig is working!")
config_logger.info("This is an info message") """


""" 
# Uncomment the following lines to test JSON-based logging
# Declarative logging configuration - JSON config

# Declarative logging configuration - JSON config

print("Declarative logging configuration - JSON config")
print("----------------------------------------\n")

base_dir = Path(__file__).parent
config_path = base_dir / "declarative-config.json"

with open(config_path, "r") as config_file:
    json_config = json.load(config_file)

logging.config.dictConfig(json_config)
config_logger = logging.getLogger("config.json")
config_logger.debug("JSON-style dictConfig is working!")
config_logger.info("INFO goes to the console")
 """


# Dynamically building config

print("Dynamically building config")
print("----------------------------------------\n")

base_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {},
    "formatters": {},
    "loggers": {}
}

base_config["formatters"]["simple"] = {
    "format": "%(levelname)8s - %(message)s"
}

base_config["handlers"]["console"] = {
    "class": "logging.StreamHandler",
    "level": "DEBUG",
    "formatter": "simple",
    "stream": "ext://sys.stdout"
}

base_config["loggers"]["config.dynamic"] = {
    "handlers": ["console"],
    "level": "WARNING",
    #"propagate": False
}

def is_debug():
    return True # setting to False will suppress debug messages

if is_debug():
    for logger, _config in base_config["loggers"].items():
        base_config["loggers"][logger]["level"] = "DEBUG"

logging.config.dictConfig(base_config)
config_logger = logging.getLogger("config.dynamic")
config_logger.debug("Dynamic config setup successful!")
config_logger.info("This is an info message")