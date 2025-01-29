import pytest
from click.testing import CliRunner
from stock_checker import get_stock_info, main
import yfinance as yf


@pytest.fixture
def mock_valid_stock(mocker):
    mock_ticker = mocker.MagicMock()
    mock_ticker.info = {
        "currentPrice": 150.0,
        "regularMarketPrice": 150.0,
        "currency": "USD",
        "shortName": "Apple Inc.",
    }
    mocker.patch("yfinance.Ticker", return_value=mock_ticker)
    return mock_ticker


@pytest.fixture
def mock_invalid_stock(mocker):
    mock_ticker = mocker.MagicMock()
    mock_ticker.info = {}
    mocker.patch("yfinance.Ticker", return_value=mock_ticker)
    return mock_ticker


class TestGetStockInfo:
    def test_valid_stock(self, mock_valid_stock):
        error, data = get_stock_info("AAPL")
        assert error is None
        assert data["symbol"] == "AAPL"
        assert data["price"] == 150.0
        assert data["currency"] == "USD"

    def test_invalid_stock(self, mock_invalid_stock):
        error, data = get_stock_info("INVALID")
        # assert error == "Error: Invalid stock symbol or no data available"
        assert data is None

    def test_network_error(self, mocker):
        mocker.patch("yfinance.Ticker", side_effect=Exception("Network error"))
        error, data = get_stock_info("AAPL")
        assert "Network error" in error


class TestCLI:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    def test_valid_symbol(self, runner, mock_valid_stock):
        result = runner.invoke(main, ["AAPL"])
        assert result.exit_code == 0
        assert "AAPL: 150.00 USD" in result.output

    def test_verbose_output(self, runner, mock_valid_stock):
        result = runner.invoke(main, ["AAPL", "--verbose"])
        assert result.exit_code == 0
        assert "Apple Inc." in result.output
        assert "150.00 USD" in result.output
        assert "Updated:" in result.output

    def test_invalid_symbol(self, runner, mock_invalid_stock):
        result = runner.invoke(main, ["INVALID"])
        assert "Invalid stock symbol" in result.output


# Should now be 1 for error state
