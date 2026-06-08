# Binance Futures Trading Bot

Python CLI bot for placing MARKET orders on Binance Futures Testnet. Built for college assignment.

## Setup Steps

1. **Clone repo**
```bash
git clone <your-repo-link>
cd binance-futures-trading-bot
install dependencies
pip install -r requirements.txt
1.Get Testnet API KeysGo to: testnet.binancefuture.comRegister/Login → API Key
2. Create APICopy API Key and Secret Key
   BINANCE_API_KEY=your_testnet_api_key_here
   BINANCE_API_SECRET=your_testnet_secret_key_here
How to Run Example
Market Buy Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Market Sell Order:
python cli.py --symbol ETHUSDT --side SELL --type MARKET --quantity 0.01
Project structure
trading_bot/
├── cli.py          # Main entry point
├── config.py       # API keys load karta hai
├── requirements.txt
├── .env.example    # Sample env file
└── bot.log         # Logs yaha save hote hain
