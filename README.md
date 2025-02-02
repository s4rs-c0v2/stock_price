# Stock Price Checker

A command-line tool to quickly check real-time stock prices using Yahoo Finance data.

## Features

- Get current stock prices for any publicly traded company
- Display basic or detailed stock information
- Optional currency conversion
- Clean and colorful command-line interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/stock-price-checker.git
cd stock-price-checker
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python stock_checker.py AAPL
```

With verbose output:
```bash
python stock_checker.py AAPL -v
```

With currency conversion:
```bash
python stock_checker.py AAPL -c EUR
```

### Options

- `-v, --verbose`: Show detailed information including company name and last update time
- `-c, --currency`: Convert price to a different currency (e.g., EUR, GBP, JPY)
- `--help`: Show help message and exit

### Examples

Basic output:
```bash
AAPL: 173.25 USD
```

Verbose output:
```bash
Apple Inc. (AAPL)
➤ Price: 173.25 USD
➤ Updated: 2024-01-20 14:30:45
```

## Requirements

- Python 3.6+
- click
- yfinance

## Dependencies

Create a `requirements.txt` file with the following:
```
click>=8.0.0
yfinance>=0.2.0
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## Disclaimer

This tool uses Yahoo Finance data and is for educational purposes only. Stock prices may be delayed and should not be used for actual trading decisions.
