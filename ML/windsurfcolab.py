# function to calculate compound annual growth rate (caggr)
def cagr(start_value, end_value, time_period):
    return ((end_value / start_value) ** (1 / time_period)) - 1

def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """Calculate Sharpe Ratio for portfolio returns"""
    import numpy as np
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)


def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """Calculate Sharpe Ratio for portfolio returns"""
    import numpy as np
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)
