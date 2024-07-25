# Quantitative Trading Strategies

## Introduction

This repository has been designed to store the Quantitative Trading Homework .....

### Homework 1 - Futures Spread Dynamics

This homework focuses on the analysis of spreads in futures markets, specifically examining two different pairs. The objective is to explore and understand the individual dynamics of these spreads, as well as their interactions with each other.

Assignment Overview:

* Data Collection and Preparation: Collect historical data for two distinct pairs of futures contracts. The data will include prices, volumes, and other relevant market metrics.
* Analyze Individual Spreads: Evaluate the price differences between the futures contracts within each pair. This will involve calculating the spread and analyzing its historical behavior, volatility, and trends.
* Explore Cross-Spread Dynamics: Investigate the relationship between the two spreads. This will include exploring correlations, potential causation, and how changes in one spread might impact the other.


### Homework 2 - Simple Spread Trading

This homework focuses on implementing a spread trading strategy. this strategy involves monitoring the displacement between two related financial instruments and making trades based on the expectation that this displacement will decrease over time. The displacement is specifically defined in terms of recent returns. 

Assignment Overview:
* Data Collection and Preparation: Collect historical data for split- and dividend-adjusted prices of two related financial instruments. The data will include prices, volumes, and other relevant market metrics.
* Strategy Development and Analysis: Develop a spread trading strategy based on the displacement between the two instruments. This will involve defining the displacement, setting thresholds for trading signals, and backtesting the strategy on historical data.
* Correlation Analysis: Investigate the relationship between the two instruments, including their historical correlation, cointegration, and other relevant metrics.
* Risk Management: Implement risk management techniques to control the exposure and potential losses of the trading strategy.

### Homework 3 - Financial Ratio Quantile Strategies

This homework revolves around utilizing financial accounting ratios to explore a “quantamental” approach to investment strategies. The focus is on investigating the profitability of a quantile-based long-short strategy, leveraging specific financial ratios to make informed trading decisions.

Assignment Overview:
* Data Collection and Preparation: The data will be extracted from a review of Zacks Fundamentals B documentation, which includes six related tables: FC, FR, MT, MKTV, SHRC, and HDM. 
* Strategy Development and Analysis: Develop a quantile-based long-short strategy using financial ratios as signals. The rations will be calculated weekly or monthly, and the strategy will be rebalanced accordingly. The strategy will rank stocks into quantiles based on the financial ratios and take long positions in the top quantile and short positions in the bottom quantile.
* Performance Evaluation: Evaluate the performance of the strategy using various metrics, including Sharpe ratio, maximum draw-down, and other relevant risk-adjusted return measures.
* Risk Management: Implement risk management techniques to control the exposure and potential losses of the trading strategy.

### Homework 4 - Return Predictions From Trade Flow

This homework focuses on assessing profit opportunities in 3 cryptotoken markets. The exercise emphasizes the challenge of capitalizing these opportunities given the high data rates and nature of these markets' price-time priority mechanisms.

Assignment Overview:
* Data Preparation: Collect historical data for three different cryptocurrencies, including trades and book data. The data will include bid-ask prices, trade sizes, and other relevant market metrics.
* Data Analysis and Trade Flow: Analyze high-frequency trade data to compute trade flows. This metric captures the net buy and sell activity in the market over the specifies interval.
* Return Prediction: Develop a model to predict future returns based on trade flows. This will involve training a machine learning model on historical data and using it to make predictions on unseen data.
* Trading Strategy: Implement a trading strategy based on the return predictions. This will involve taking long or short positions based on the model's output and evaluating the strategy's performance.
* Risk Management: Implement risk management techniques to control the exposure and potential losses of the trading strategy.

### Homework 5 - FX Carry Strategy

This homework focuses on the implementation of a carry trade strategy in the foreign exchange market. The FX carry trade involves borrowing funds in a currency with a low-interest rate and investing in a currency with a higher interest rate. The objective is to profit from the difference in interest rates, which is typically facilitated through a cross-currency swap.

Assignment Overview:
* Data Collection and Preparation: Collect data on the shortest available rates for UK overnight index swaps (OIS) and spot FX rates for the dollar versus the pound. Additionally, collect swap yield curves and FX rates for the Egyptian Pound, Hungarian Forint, Costa Rican Colon, and Romanian Leu from the earliest available date to the present. 
* Strategy Development and Analysis: Develop a carry trade strategy based on the interest rate differentials between the currencies. This will involve calculating the carry and analyzing its historical behavior, volatility, and trends.
* Profitability Analysis: Calculate an approximate profit and loss (PL) statement for the weekly-traded cross-currency swaps. The calculation will account for the interest rate differential, exchange rate movements, and the impact of rolling over the swaps weekly. 