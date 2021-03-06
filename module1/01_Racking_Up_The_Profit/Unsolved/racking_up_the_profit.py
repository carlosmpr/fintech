"""Racking up the profit."""

# Suppose each stock price is the same
stock_price = 30

# But that dividend yields vary across five stocks in your portfolio
dividend_yields = [0.035, 0.040, 0.072, 0.012, 0.052]

# @TODO: Create a variable to hold tallied dividend income
# YOUR CODE HERE!
hold_dividend = []
for dividend in dividend_yields:
    hold_dividend.append(dividend * stock_price)


total_dividends = sum(hold_dividend)
# @TODO: Create a for loop to calculated and add up all the dividend income
# YOUR CODE HERE!

# @TODO: Once it's all done, print the dividend income for the entire portfolio
# YOUR CODE HERE!
print(f"The total dividends is: {total_dividends}")