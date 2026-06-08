import os

try:
    from binance.spot import SpotClient
    _BINANCE_CONNECTOR = True
except ImportError:
    from binance.client import Client as SpotClient
    _BINANCE_CONNECTOR = False

def get_testnet_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        raise ValueError("BINANCE_API_KEY aur BINANCE_API_SECRET .env mein daal de")
    
    # Use SpotClient from binance.spot and point to testnet base URL
    # The binance connector uses base_url for testnet endpoints
    client = SpotClient(api_key=api_key, api_secret=api_secret, base_url="https://testnet.binance.vision")
    return client