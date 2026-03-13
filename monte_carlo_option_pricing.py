import numpy as np

# Parameters
S0 = 100        # Initial stock price
K = 100         # Strike price
T = 1.0         # Time to maturity (1 year)
r = 0.05        # Risk-free rate
sigma = 0.2     # Volatility
simulations = 10000

# Generate random stock price paths
Z = np.random.standard_normal(simulations)
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

# Option payoff (European Call)
payoff = np.maximum(ST - K, 0)

# Discounted expected payoff
option_price = np.exp(-r * T) * np.mean(payoff)

print("Estimated European Call Option Price:", option_price)
