from datetime import datetime

import click
import yfinance as yf


def get_stock_info(symbol, currency=None):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        if not info:
            return "Error: Invalid stock symbol or no data available", None

        price = info.get("currentPrice", info.get("regularMarketPrice"))
        currency = currency or info.get("currency", "USD")
        name = info.get("shortName", symbol)
        updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return None, {
            "symbol": symbol,
            "name": name,
            "price": price,
            "currency": currency,
            "updated": updated,
        }
    except Exception as e:
        return f"Error: {str(e)}", None


@click.command()
@click.argument("symbol")
@click.option(
    "--currency", "-c", default=None, help="Convert price to different currency"
)
@click.option("--verbose", "-v", is_flag=True, help="Show detailed information")
def main(symbol, currency, verbose):
    """Get current stock price for a given company symbol"""
    error, data = get_stock_info(symbol, currency)

    if error:
        click.secho(error, fg="red")
        return

    if verbose:
        click.echo(
            f"""
        {click.style(data['name'], fg='bright_white')} ({data['symbol']})
        {click.style('➤ Price:', fg='bright_cyan')} {data['price']:.2f} {data['currency']}
        {click.style('➤ Updated:', fg='bright_cyan')} {data['updated']}
        """
        )
    else:
        click.echo(
            click.style(f"{data['symbol']}: ", fg="green")
            + click.style(f"{data['price']:.2f} {data['currency']}", fg="bright_white")
        )


if __name__ == "__main__":
    main()
