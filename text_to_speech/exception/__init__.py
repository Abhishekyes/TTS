import os

def error_message_details(error,error_detail):
    _,_,exc_tb=error_detail.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message = "Error occur pytho script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
                                                                                                    


class TTSException(Exception):
    
    def __init__(self,error_message,error_details):
        super().__init__(error_message)
        self.error_message =error_message_details(error_message,error_details=error_details)
        
    def __str__(self):
        return self.error_message