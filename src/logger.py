import logging
import os
from datetime import datetime

file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
file_path = os.path.join(os.get_cwd(), 'logs', file_name)
os.makedirs(file_path, exist_ok=True)

logging.basicConfig(
    filename=file_name,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)