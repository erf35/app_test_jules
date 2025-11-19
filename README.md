# Currency Converter

A simple library to convert currencies.

## Installation

```bash
pip install .
```

## Usage

```python
from currency_converter import converter

amount = 100
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = converter.convert(amount, from_currency, to_currency)
print(f'{amount} {from_currency} is equal to {converted_amount} {to_currency}')
```
