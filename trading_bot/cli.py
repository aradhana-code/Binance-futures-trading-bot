import argparse
import os
from dotenv import load_dotenv
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity

def print_order_summary(order):
    print("\n" + "="*55)
    print("📋 ORDER REQUEST SUMMARY")
    print(f"Symbol: {order['symbol']}")
    print(f"Side: {order['side']}")
    print(f"Type: {order['type']}")
    print(f"Quantity: {order['origQty']}")
    print(f"Price: {order.get('price','MARKET')}")
    
    print("\n📄 ORDER RESPONSE DETAILS")
    print(f"Order ID: {order['orderId']}")
    print(f"Status: {order['status']}")
    print(f"Executed Qty: {order['executedQty']}")
    print(f"Avg Price: {order.get('avgPrice','N/A')}")
    
    print(f"\n✅ SUCCESS: Order placed successfully on Testnet!")
    print("="*55)

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")
    
    args = parser.parse_args()
    
    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        
        if order_type == "MARKET":
            order = place_market_order(symbol, side, quantity)
        else:
            if not args.price or args.price <= 0:
                raise ValueError("LIMIT order ke liye --price dena zaruri hai")
            order = place_limit_order(symbol, side, quantity, args.price)
        
        print_order_summary(order)
        
    except Exception as e:
        print(f"\n❌ FAILURE: {e}")

if __name__ == "__main__":
    main()