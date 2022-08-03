import sys
import cn2en

from loguru import logger


logger.remove()
logger.add(sys.stderr, format=cn2en.formatter)
# logger.add('./log/{time}.log', rotation='00:00', format=formatter)

if __name__ == '__main__':
    logger.info("This is a demo and here is the pass: secret")
