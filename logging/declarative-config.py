import logging  
import logging.config
import os
from pathlib import Path
from typing import Dict, Any

""" 
# Uncomment the following lines to load logging config from an INI file

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
config_logger.info("This is an info message")

# Declarative logging configuration - JSON config

# Dynamically building config

