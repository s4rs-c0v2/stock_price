FROM python:alpine

WORKDIR /usr/scr/app

# Define dafault company
ENV STOCK_SYMBOL="AAPL"

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["sh", "-c", "python stock_checker.py $STOCK_SYMBOL"]
