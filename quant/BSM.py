import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# BSM 模型函数
def black_scholes(S0, K, T, r, sigma, option_type='call'):
    """
    计算欧式期权的 Black-Scholes 价格
    参数：
        S0: 标的资产当前价格
        K: 执行价格
        T: 到期时间（年）
        r: 无风险利率（年化）
        sigma: 波动率（年化）
        option_type: 'call' 或 'put'
    返回：
        期权价格
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    return price

# 参数设置
S0 = 100  # 标的资产价格
K = 100   # 执行价格
T = 1.0   # 到期时间（1年）
r = 0.05  # 无风险利率
sigma = 0.2  # 波动率

# 计算期权价格
call_price = black_scholes(S0, K, T, r, sigma, 'call')
put_price = black_scholes(S0, K, T, r, sigma, 'put')
print(f"Call Option Price: {call_price:.2f}")
print(f"Put Option Price: {put_price:.2f}")

# 绘制期权价格随标的价格变化
S_range = np.linspace(50, 150, 100)
call_prices = [black_scholes(S, K, T, r, sigma, 'call') for S in S_range]
put_prices = [black_scholes(S, K, T, r, sigma, 'put') for S in S_range]

plt.figure(figsize=(10, 6))
plt.plot(S_range, call_prices, label='Call Option', color='blue')
plt.plot(S_range, put_prices, label='Put Option', color='red')
plt.axvline(K, color='black', linestyle='--', label='Strike Price')
plt.title('Black-Scholes Option Prices vs. Underlying Price')
plt.xlabel('Underlying Price (S)')
plt.ylabel('Option Price')
plt.legend()
plt.grid(True)
plt.show()
