import logging
import os
from datetime import datetime # type: ignore

file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
file_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(file_path, exist_ok=True)
FILE_PATH = os.path.join(file_path, file_name)

logging.basicConfig(
    filename=FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



"""import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)"""