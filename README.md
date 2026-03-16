# Monte Carlo Option Pricing

This project implements Monte Carlo simulation to price a European call option using Python.

Monte Carlo methods are widely used in quantitative finance to price derivatives and evaluate financial risk.

## Model Overview

The model simulates thousands of possible future stock prices using geometric Brownian motion.

Steps:

1. Simulate random stock price paths
2. Calculate option payoff
3. Average simulated payoffs
4. Discount to present value

## Mathematical Model

The stock price follows a Geometric Brownian Motion:

dS = μSdt + σSdW

Where:

S = stock price  
μ = expected return  
σ = volatility  
dW = Wiener process

The Monte Carlo method simulates thousands of possible future stock price paths and computes the expected discounted payoff.
## Formula

Stock price simulation:

S(T) = S0 * exp((r - 0.5σ²)T + σ√T Z)

Where:

S0 = initial stock price  
σ = volatility  
r = risk-free rate  
T = time to maturity  
Z = random normal variable  

## Example Parameters

S0 = 100      Initial stock price  
K = 100       Strike price  
T = 1 year    Time to maturity  
r = 5%        Risk-free rate  
σ = 20%       Volatility  
Simulations = 10,000
## Output

The model computes the option price as:

Option Price = exp(-rT) × average(payoff)

Where payoff = max(ST − K, 0)
## Tools

Python  
NumPy

## Future Improvements

• American option pricing  
• Path-dependent options  
• Variance reduction techniques  
• GPU acceleration  
