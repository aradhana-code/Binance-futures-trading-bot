# Binance Futures Testnet Trading Bot

CLI bot for placing Market/Limit orders on Binance Futures Testnet USDT-M.

## Setup Steps
1. Register: https://testnet.binancefuture.com
2. Generate API Key + Secret with Futures permission
3. Create `.env` file in root folder:
   BINANCE_API_KEY=your_api_key
   BINANCE_API_SECRET=your_secret_key
4. Install dependencies: `pip install -r requirements.txt`

## How to Run Examples
Market Buy: `python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001`
Market Sell: `python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001`
Limit Buy: `python cli.py --symbol ETHUSDT --side BUY --type LIMIT --quantity 0.01 --price 2000`
Limit Sell: `python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.01 --price 2500`

## Assumptions
- Only USDT-M futures pairs supported
- Testnet account has sufficient fake USDT balance
- Quantity follows Binance minimum lot size rules

## Logging
All API requests, responses, and errors logged to `bot.log` file.