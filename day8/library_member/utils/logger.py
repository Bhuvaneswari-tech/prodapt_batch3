import logging

logging.basicConfig(filename="data/logs.txt", level=logging.INFO)

def log_activity(message):
    logging.info(message)
