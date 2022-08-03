import re
import sys

from loguru import logger


def replace_message(message: str):
    """Obfuscate sensitive information."""
    result = re.sub(r"pass: .*", "pass: xxx", message)
    return result


def formatter(record):
    # record["extra"]["obfuscated_message"] = replace_message(record["message"])
    message = replace_message(record["message"])
    return "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " \
           "[{level}] {extra[obfuscated_message]}\n{exception}"


logger.remove()
logger.add(sys.stderr, format=formatter)
# logger.add('./log/{time}.log', rotation='00:00', format=formatter)

if __name__ == '__main__':
    logger.info("This is a demo and here is the pass: secret")
