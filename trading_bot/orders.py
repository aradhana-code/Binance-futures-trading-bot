import importlib
import sys
from pathlib import Path

# Add parent directory to path if needed
sys.path.insert(0, str(Path(__file__).parent))

try:
    from logging_config import logger
except ImportError:
    from .logging_config import logger

try:
    from client import get_testnet_client
except ImportError:
    from .client import get_testnet_client

try:
    BinanceAPIException = importlib.import_module('binance.exceptions').BinanceAPIException
except (ImportError, ModuleNotFoundError, AttributeError):
    BinanceAPIException = Exception

client = get_testnet_client()

def place_market_order(symbol, side, quantity):
    logger.info(f"API Request: MARKET {side} {symbol} Qty={quantity}")
    try:
        order = client.futures_create_order(
            symbol=symbol, 
            side=side, 
            type='MARKET', 
            quantity=quantity
        )
        logger.info(f"API Response: OrderID={order['orderId']} Status={order['status']}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
        raise Exception(f"Binance Error: {e.message}")
    except Exception as e:
        logger.error(f"Network Error: {e}")
        raise

def place_limit_order(symbol, side, quantity, price):
    logger.info(f"API Request: LIMIT {side} {symbol} Qty={quantity} Price={price}")
    try:
        order = client.futures_create_order(
            symbol=symbol, 
            side=side, 
            type='LIMIT', 
            timeInForce='GTC',
            quantity=quantity, 
            price=str(price)
        )
        logger.info(f"API Response: OrderID={order['orderId']} Status={order['status']}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
        raise Exception(f"Binance Error: {e.message}")
    except Exception as e:
        logger.error(f"Network Error: {e}")
        raise