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

## Formula

Stock price simulation:

S(T) = S0 * exp((r - 0.5σ²)T + σ√T Z)

Where:

S0 = initial stock price  
σ = volatility  
r = risk-free rate  
T = time to maturity  
Z = random normal variable  

## Tools

Python  
NumPy
