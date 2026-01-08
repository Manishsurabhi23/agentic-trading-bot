import os
import sys
class TradingBotException(Exception):
    """Base exception class for trading bot errors."""
    def __init__(self,error_message: str,error_details_using_sys:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details_using_sys.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return f"Error occurred in script: {self.file_name} at line number: {self.lineno} with message: {self.error_message}"


if __name__ == "__main__":
    try:
        a = 1 / 0
        print("this will not be printed",a)
    except Exception as e:
        raise TradingBotException(e,sys)
    

