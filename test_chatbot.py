import pandas as pd

# Define the URL of the data
url = "https://stats.oecd.org/sdmx-json/data/DP_LIVE/.GDP.../OECD?contentType=csv&detail=code&separator=comma&csv-lang=en"

# Use pandas to download the data
data = pd.read_csv(url)

# Print the data
print(data)

# regress gdp on unemployment, inflation, public spending
import statsmodels.api as sm

# Define dependent variable and independent variables
Y = data['GDP']
X = data[['unemployment', 'inflation', 'public_spending']]

# Add a constant to the independent variables
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(Y, X)
results = model.fit()

# Print the summary
print(results.summary())

