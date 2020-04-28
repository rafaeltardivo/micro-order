import logging

logFormatter = ('TIMESTAMP:%(asctime)s MODULE:%(module)s MSG:%(message)s')
logging.basicConfig(format=logFormatter, level=logging.INFO)
logger = logging.getLogger(__name__)
