import yfinance as yf
import pandas as pd
import argparse

def download_options(ticker: str, outdir: str):
    """
    Download all available options data for a given ticker.
    
    :param ticker: Stock ticker symbol, e.g. 'AAPL'
    :param save_to_csv: Save data to CSV files if True
    :return: Dictionary with expiration dates as keys and DataFrames as values
    """
    stock = yf.Ticker(ticker)
    expirations = stock.options
    print(f"Found {len(expirations)} expiration dates for {ticker}")

    options_data = {}
    for expiry in expirations:
        opt_chain = stock.option_chain(expiry)
        
        # Combine calls and puts with a column indicating type
        calls = opt_chain.calls.copy()
        calls["type"] = "call"
        puts = opt_chain.puts.copy()
        puts["type"] = "put"
        df = pd.concat([calls, puts], ignore_index=True)
        options_data[expiry] = df

        filename = f"{outdir}/{expiry}.csv"
        df.to_csv(filename, index=False)
        
    return options_data


if __name__ == "__main__":

    parser=argparse.ArgumentParser(description="Yahoo historical data")
    parser.add_argument("symbol")
    parser.add_argument("outdir")
    args=parser.parse_args()

    options = download_options(args.symbol, args.outdir)


