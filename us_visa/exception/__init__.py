# utils/exception_handler.py

import sys
import os
import traceback

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Generate a detailed error message with file name, line number, and error info.

    Args:
        error (Exception): The original exception.
        error_detail (sys): The sys module to extract traceback info.

    Returns:
        str: Formatted error message.
    """
    exc_type, exc_value, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        file_name = os.path.basename(exc_tb.tb_frame.f_code.co_filename)
        line_no = exc_tb.tb_lineno
        error_message = (
            f"Error occurred in script [{file_name}] "
            f"at line [{line_no}]: {str(error)}"
        )
    else:
        error_message = str(error)

    return error_message


class USvisaException(Exception):
    """
    Custom Exception class for the US Visa project.
    Provides detailed context for debugging.
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
