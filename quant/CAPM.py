import numpy as np
import pandas as pd
import yfinance as yf

# 获取数据
stock = 'AAPL'  # 示例：苹果股票
market = '^GSPC'  # 标普500指数
start_date = '2020-01-01'
end_date = '2025-01-01'

# 下载股票和市场数据
stock_data = yf.download(stock, start=start_date, end=end_date)['Adj Close']
market_data = yf.download(market, start=start_date, end=end_date)['Adj Close']

# 计算日回报
stock_returns = stock_data.pct_change().dropna()
market_returns = market_data.pct_change().dropna()

# 计算贝塔
cov_matrix = np.cov(stock_returns, market_returns)
beta = cov_matrix[0, 1] / cov_matrix[1, 1]
print(f"Beta for {stock}: {beta:.2f}")

# CAPM 预期回报
rf = 0.03  # 无风险利率（年化）
market_return = 0.10  # 市场预期回报（年化）
expected_return = rf + beta * (market_return - rf)
print(f"Expected Return for {stock}: {expected_return:.4f}")
