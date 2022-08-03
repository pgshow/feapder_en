import re
import sys

from loguru import logger


logger_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "{extra[ip]} {extra[user]} - <level>{message}</level>"
)
logger.configure(extra={"ip": "", "user": ""})  # Default values
logger.remove()
logger.add(sys.stderr, format=logger_format)

if __name__ == '__main__':
    logger.info("This is a demo and here is the pass: secret")
