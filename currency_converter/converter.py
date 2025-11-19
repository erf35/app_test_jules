RATES = {
    'USD': 1.0,
    'EUR': 0.9,
    'GBP': 0.8,
}

def convert(amount, from_currency, to_currency):
    """
    Converts an amount from one currency to another.
    """
    if from_currency not in RATES or to_currency not in RATES:
        raise ValueError('Invalid currency')

    return amount / RATES[from_currency] * RATES[to_currency]
