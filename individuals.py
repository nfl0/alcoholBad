import pandas as pd
import statsmodels.api as sm

# Define the parameters
params = {
    'health_effects': [0.3, 0.7, 0.5, 0.2, 0.1, 0.2, 0.1, 0.8, 0.7, 0.6, 0.5],
    'economic_impact': [-0.1, -0.3, -0.2, -0.3, -0.2, -0.1, 0.2, 0.3, 0.2, 0.1, 0.1],
    'social_issues': [0.4, 0.5, 0.6, 0.5, 0.4, 0.3, 0.2, 0.3, 0.4, 0.5, 0.6],
    'crime_rate': [-0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
    'road_accidents': [-0.2, -0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, -0.1, -0.2, -0.3],
    'productivity_loss': [-0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.2, 0.1, -0.1, -0.2, -0.3],
    'tax_revenue': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2],
    'mental_health': [0.5, 0.6, 0.6, 0.5, 0.4, 0.3, 0.2, 0.3, 0.4, 0.5, 0.6],
    'physical_health': [0.4, 0.5, 0.6, 0.5, 0.4, 0.3, 0.2, 0.3, 0.4, 0.5, 0.6],
    'social_life': [0.3, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.1],
    'financial_status': [0.6, 0.7, 0.8, 0.9, 1.0, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5],
    'net_impact': [0, -1, -1, -2, -2, -1, 1, 2, 2, 1, 0]
}

# Load the data
data = pd.DataFrame.from_dict(params)

# Define the variables and the outcome
X = data[['health_effects', 'economic_impact', 'social_issues', 'crime_rate', 'road_accidents', 'productivity_loss', 'tax_revenue', 'mental_health', 'physical_health', 'social_life', 'financial_status']]
y = data['net_impact']

# Fit the model
model = sm.OLS(y, sm.add_constant(X)).fit()

# Print the results summary
print(model.summary())

# Compute the net impact on individuals
individual_net_impact = model.params['mental_health'] * data['mental_health'] + \
                        model.params['physical_health'] * data['physical_health'] + \
                        model.params['social_life'] * data['social_life'] + \
                        model.params['financial_status'] * data['financial_status']

# Print the overall impact on individuals
if individual_net_impact.mean() > 0:
    print("Based on the analysis, alcohol has a net positive impact on individuals.")
elif individual_net_impact.mean() < 0:
    print("Based on the analysis, alcohol has a net negative impact on individuals.")
else:
    print("Based on the analysis, alcohol has a neutral impact on individuals.")

# Interpretation of the results
print("Note: Interpretation of the results: The interpretation of the results is based on a single criterion (net impact) and may not fully capture the complex effects of alcohol on individuals.")