import pandas as pd
import yfinance as yf
import statsmodels.api as sm

# 获取股票数据
stock = 'AAPL'
start_date = '2020-01-01'
end_date = '2025-01-01'
stock_data = yf.download(stock, start=start_date, end=end_date)['Adj Close']
stock_returns = stock_data.pct_change().dropna()

# 获取Fama-French 三因子数据（从Kenneth French网站下载）
ff_data = pd.read_csv('F-F_Research_Data_Factors_daily.csv', parse_dates=['Date'], index_col='Date')
ff_data = ff_data / 100  # 转换为小数
ff_data = ff_data.loc[stock_returns.index]  # 对齐时间

# 计算超额回报
rf = ff_data['RF']  # 无风险利率
excess_returns = stock_returns - rf

# 准备因子数据
X = ff_data[['Mkt-RF', 'SMB', 'HML']]
X = sm.add_constant(X)  # 添加截距（alpha）

# 回归分析
model = sm.OLS(excess_returns, X).fit()
print(model.summary())

# 输出因子敏感性
print(f"Beta (Market): {model.params['Mkt-RF']:.2f}")
print(f"SMB Exposure: {model.params['SMB']:.2f}")
print(f"HML Exposure: {model.params['HML']:.2f}")
print(f"Alpha: {model.params['const']:.4f}")
