# function to calculate compound annual growth rate (caggr)
def cagr(start_value, end_value, time_period):
    return ((end_value / start_value) ** (1 / time_period)) - 1