import logging  
import logging.config
import os
from pathlib import Path

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
app_logger.debug("INI-style fileConfig is working!")


# Declarative logging configuration - Dictionary config

# Declarative logging configuration - JSON config

# Dynamically building config

