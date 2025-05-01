import pandas as pd
import yfinance as yf
import statsmodels.api as sm

# 获取股票数据
stock = 'AAPL'
start_date = '2020-01-01'
end_date = '2025-01-01'
stock_data = yf.download(stock, start=start_date, end=end_date)['Adj Close']
stock_returns = stock_data.pct_change().dropna()

# 假设因子数据（示例：市场回报、GDP增长、通胀率）
# 实际需从可靠来源获取（如FRED数据库）
factor_data = pd.DataFrame({
    'Market': yf.download('^GSPC', start=start_date, end=end_date)['Adj Close'].pct_change(),
    'GDP_Growth': np.random.normal(0.02, 0.01, len(stock_returns)),  # 模拟数据
    'Inflation': np.random.normal(0.03, 0.005, len(stock_returns))   # 模拟数据
}).dropna()
factor_data = factor_data.loc[stock_returns.index]  # 对齐时间

# 计算超额回报（假设无风险利率为常数）
rf = 0.03 / 252  # 日化无风险利率
excess_returns = stock_returns - rf

# 回归分析
X = factor_data[['Market', 'GDP_Growth', 'Inflation']]
X = sm.add_constant(X)  # 添加截距（alpha）
model = sm.OLS(excess_returns, X).fit()

# 输出结果
print(model.summary())
print(f"Factor Exposures (Betas):")
print(f"Market: {model.params['Market']:.2f}")
print(f"GDP Growth: {model.params['GDP_Growth']:.2f}")
print(f"Inflation: {model.params['Inflation']:.2f}")
print(f"Alpha: {model.params['const']:.4f}")
