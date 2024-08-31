"""
A logging module that provides a simple logging class for printing log messages.

This module defines a Log class with methods for printing log messages at different levels.

The Log class is designed to be simple and easy to use, with a minimalistic approach to logging.

Attributes:
    None

Classes:
    Log: A logging class that provides methods for printing log messages.

Methods:
    info(text): Prints an info log message.
    error(text): Prints an error log message.

Usage:
    log = Log()
    log.info("This is an info log message")
    log.error("This is an error log message")
"""
import colorama
colorama.init()

class Log:
    """
    A logging class that provides methods for printing log messages.

    Attributes:
        None

    Methods:
        info(text): Prints an info log message.
        error(text): Prints an error log message.
    """

    def info(self, text: str) -> None:
        """
        Prints an info log message.

        Args:
            text (str): The log message to be printed.

        Returns:
            None
        """
        print("[INFO] - ".join(["", text]) + "\033[0m")

    def error(self, text: str) -> None:
        """
        Prints an error log message.

        Args:
            text (str): The log message to be printed.

        Returns:
            None
        """
        print(colorama.Fore.RED ,"[ERROR] - ".join(["", text]))
