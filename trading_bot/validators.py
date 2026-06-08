def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol khaali nahi ho sakta")
    symbol = symbol.upper()
    if not symbol.endswith('USDT'):
        raise ValueError("Sirf USDT-M pair support: BTCUSDT, ETHUSDT")
    return symbol

def validate_side(side):
    side = side.upper()
    if side not in ['BUY', 'SELL']:
        raise ValueError("Side sirf BUY ya SELL ho sakta hai")
    return side

def validate_order_type(order_type):
    order_type = order_type.upper()
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type sirf MARKET ya LIMIT")
    return order_type

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity 0 se badi honi chahiye")
    return quantity