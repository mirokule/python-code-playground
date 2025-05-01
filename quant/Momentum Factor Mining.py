import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 参数设置
stock_list = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']  # 示例股票
start_date = '2020-01-01'
end_date = '2025-01-01'
lookback = 252  # 动量计算窗口（约1年）
forward = 21    # 预测未来回报的窗口（约1个月）

# 获取价格数据
data = yf.download(stock_list, start=start_date, end=end_date)['Adj Close']
returns = data.pct_change().dropna()

# 计算动量因子（过去12个月累计回报，剔除最近1个月）
momentum = (data / data.shift(lookback) - 1).shift(21).dropna()
future_returns = (data.shift(-forward) / data - 1).dropna()

# 对齐数据
common_index = momentum.index.intersection(future_returns.index)
momentum = momentum.loc[common_index]
future_returns = future_returns.loc[common_index]

# 因子筛选：排序分析
def portfolio_sort(factor, returns, n_groups=5):
    portfolios = []
    for date in factor.index:
        # 按因子值排序
        factor_t = factor.loc[date].rank(ascending=True)
        bins = pd.qcut(factor_t, n_groups, labels=False, duplicates='drop')
        # 计算每个分组的平均回报
        returns_t = returns.loc[date]
        group_returns = [returns_t[bins == i].mean() for i in range(n_groups)]
        portfolios.append(group_returns)
    return pd.DataFrame(portfolios, index=factor.index, columns=[f'Quintile {i+1}' for i in range(n_groups)])

# 按动量因子分组
portfolios = portfolio_sort(momentum, future_returns)

# 计算高-低组合（Long-Short）
portfolios['Long-Short'] = portfolios['Quintile 5'] - portfolios['Quintile 1']

# 回测绩效
cum_returns = (1 + portfolios['Long-Short']).cumprod() - 1
sharpe_ratio = portfolios['Long-Short'].mean() / portfolios['Long-Short'].std() * np.sqrt(252)

# 回归分析：检验因子预测力
results = []
for stock in stock_list:
    X = momentum[stock].dropna()
    y = future_returns[stock].loc[X.index]
    X = sm.add_constant(X)  # 添加截距
    model = sm.OLS(y, X).fit()
    results.append({
        'Stock': stock,
        'Beta': model.params[stock],
        'T-Stat': model.tvalues[stock],
        'P-Value': model.pvalues[stock]
    })
regression_results = pd.DataFrame(results)

# 输出结果
print("Portfolio Returns (Annualized):")
print(portfolios.mean() * 252)
print(f"\nLong-Short Sharpe Ratio: {sharpe_ratio:.2f}")
print("\nRegression Results:")
print(regression_results)

# 绘图
plt.figure(figsize=(10, 6))
cum_returns.plot(title='Cumulative Returns of Long-Short Momentum Portfolio')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid(True)
plt.show()