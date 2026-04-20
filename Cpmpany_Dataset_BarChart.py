import matplotlib.pyplot as plt

# Dataset: 30 companies with ratings (out of 5)
data = {
    "Google": 4.6,
    "Microsoft": 4.5,
    "Apple": 4.4,
    "Amazon": 4.2,
    "Meta": 4.3,
    "Tesla": 4.1,
    "IBM": 4.0,
    "Oracle": 3.9,
    "Intel": 4.2,
    "Cisco": 4.3,
    "SAP": 4.2,
    "Salesforce": 4.4,
    "Adobe": 4.5,
    "NVIDIA": 4.6,
    "Uber": 4.1,
    "Airbnb": 4.4,
    "Netflix": 4.3,
    "PayPal": 4.2,
    "Spotify": 4.3,
    "Zoom": 4.0,
    "Twitter": 3.8,
    "Snap": 3.9,
    "Shopify": 4.4,
    "Dell": 4.1,
    "HP": 4.0,
    "Wipro": 3.7,
    "Infosys": 3.9,
    "TCS": 4.0,
    "Accenture": 4.2,
    "HCLTech": 3.8
}

# Sort by rating (optional, makes chart cleaner)
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

companies = list(sorted_data.keys())
ratings = list(sorted_data.values())

# Plot
plt.figure(figsize=(12, 8))
plt.barh(companies, ratings)

plt.xlabel("Rating (out of 5)")
plt.ylabel("Companies")
plt.title("Company Ratings Comparison (30 Companies)")

plt.xlim(3.5, 5)  # zoom for better visualization
plt.show()
