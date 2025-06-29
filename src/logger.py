import logging
import os
from datetime import datetime



# Generate log file name using current timestamp
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"   # ➤ example: "27_06_2025_12_45_10.log"


# Create logs directory if not exists
logs_dir = os.path.join(os.getcwd(), "logs")   # ➤ creates a 'logs' folder in the current working directory
os.makedirs(logs_dir, exist_ok=True)           # ➤ creates the folder if it doesn't already exist


# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)   # ➤ example: ".../logs/27_06_2025_12_45_10.log"


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] Line : %(lineno)d [Logger: %(name)s | Module: %(module)s] - %(levelname)s - %(message)s",
    level=logging.INFO
)
