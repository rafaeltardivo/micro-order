import logging
logFormatter = ('TIMESTAMP:%(asctime)s LEVEL:%(levelname)s MSG:%(message)s'
                ' PAYLOAD:%(payload)s')
logging.basicConfig(format=logFormatter, level=logging.INFO)
logger = logging.getLogger(__name__)