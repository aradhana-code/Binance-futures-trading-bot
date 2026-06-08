import logging
import os

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)
    
    # File handler - bot.log mein save hoga
    fh = logging.FileHandler('bot.log', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    return logger

logger = setup_logger()