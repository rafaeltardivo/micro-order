import sys

from loguru import logger

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time}</green> <blue>{level}</blue> {message}"
)
