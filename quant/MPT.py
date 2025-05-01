import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 假设数据
n_assets = 3
returns = np.array([0.1, 0.12, 0.15])  # 预期回报
cov_matrix = np.array([[0.005, -0.002, 0.001],
                       [-0.002, 0.008, 0.003],
                       [0.001, 0.003, 0.007]])  # 协方差矩阵
rf = 0.03  # 无风险利率

# 计算组合回报和风险
def portfolio_performance(weights, returns, cov_matrix):
    port_return = np.sum(returns * weights)
    port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))  # 年化波动率
    return port_return, port_vol

# 目标函数：最小化风险
def minimize_volatility(weights, returns, cov_matrix, target_return):
    port_return, port_vol = portfolio_performance(weights, returns, cov_matrix)
    return port_vol if abs(port_return - target_return) < 1e-5 else 1e10

# 优化有效前沿
target_returns = np.linspace(0.05, 0.20, 50)
volatilities = []
for tr in target_returns:
    cons = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
            {'type': 'eq', 'fun': lambda w: portfolio_performance(w, returns, cov_matrix)[0] - tr})
    bounds = tuple((0, 1) for _ in range(n_assets))
    result = minimize(minimize_volatility, n_assets*[1./n_assets], args=(returns, cov_matrix, tr),
                     method='SLSQP', bounds=bounds, constraints=cons)
    volatilities.append(result['fun'])

# 绘图
plt.plot(volatilities, target_returns, 'b-', label='Efficient Frontier')
plt.xlabel('Volatility (Std. Dev.)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier')
plt.legend()
plt.show()
