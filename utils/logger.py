import logging
import os

def get_logger(name: str):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"{name}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # File handler
        fh = logging.FileHandler(log_path, mode='w')
        fh.setLevel(logging.DEBUG)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add handlers
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
