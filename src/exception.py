import sys
from src.logger import logging

def get_error_details(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"An error is occured in {filename} at {line_number} line. The error is: {error}"

    return error_message

class CustomeException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = get_error_details(error_message, error_details=error_details)
    
    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    logging.info("Logging has started")

    try:
        a = 1/0
    except Exception as e:
        logging.info("Devision by Zero")
        raise CustomeException(e, sys)
    
