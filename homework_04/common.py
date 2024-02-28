import logging

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
    )
