import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# data parameters
tickers = ["IBM", "WMT", "O"]
start_date = "2022-01-01"  # 2 year daily data
end_date = "2024-01-01"

# new dataframe to store prices
close_prices_df = pd.DataFrame()

# download data and fill dataframe with necessary data
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    close_prices_df[ticker] = data["Adj Close"]

# clean up dataframe
close_prices_df["Date"] = data.index
close_prices_df.reset_index(drop=True, inplace=True)
close_prices_df = close_prices_df[["Date", "IBM", "WMT", "O"]]
close_prices_df = close_prices_df.rename(
    columns={"IBM": "IBM Adj Close", "WMT": "WMT Adj Close", "O": "O Adj Close"}
)

# add daily returns
for ticker in tickers:
    close_prices_df[f"{ticker} Daily Return"] = close_prices_df[
        f"{ticker} Adj Close"
    ].pct_change()

# plot of daily returns
plt.figure(figsize=(10, 6))
plt.plot(close_prices_df["IBM Daily Return"], label="IBM", color="black", linewidth=1.5)
plt.plot(
    close_prices_df["WMT Daily Return"], label="WMT", color="darkorange", linewidth=1.25
)
plt.plot(
    close_prices_df["O Daily Return"], label="O", color="cornflowerblue", linewidth=1
)
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.title("Daily Returns of IBM, WMT, O for past 2 years")
plt.legend()
plt.show()

# distribution of daily returns
close_prices_df["WMT Daily Return"].hist(bins=25)
plt.show()

# statistics
ibm_avg = close_prices_df["IBM Daily Return"].mean()
wmt_avg = close_prices_df["WMT Daily Return"].mean()
o_avg = close_prices_df["O Daily Return"].mean()

ibm_sd = close_prices_df["IBM Daily Return"].std()
wmt_sd = close_prices_df["WMT Daily Return"].std()
o_sd = close_prices_df["O Daily Return"].std()

ibm_skew = close_prices_df["IBM Daily Return"].skew()
wmt_skew = close_prices_df["WMT Daily Return"].skew()
o_skew = close_prices_df["O Daily Return"].skew()

ibm_kurt = close_prices_df["IBM Daily Return"].kurtosis()
wmt_kurt = close_prices_df["WMT Daily Return"].kurtosis()
o_kurt = close_prices_df["O Daily Return"].kurtosis()

# correlation and covariance matrix
daily_returns_df = pd.DataFrame()
columns = ["IBM Daily Return", "WMT Daily Return", "O Daily Return"]
daily_returns_df[columns] = close_prices_df[columns]
corr_matrix = daily_returns_df.corr()
cov_matrix = daily_returns_df.cov()
print(corr_matrix)
print(cov_matrix)
