import matplotlib.pyplot as plt

# Dataset: 30 companies with approximate revenues (in billions USD)
data = {
    "Walmart": 611,
    "Amazon": 575,
    "Apple": 394,
    "ExxonMobil": 344,
    "UnitedHealth": 324,
    "CVS Health": 322,
    "Berkshire Hathaway": 302,
    "Alphabet (Google)": 307,
    "Microsoft": 211,
    "Tesla": 97,
    "Meta": 134,
    "Intel": 54,
    "Oracle": 50,
    "IBM": 61,
    "Cisco": 57,
    "SAP": 34,
    "Salesforce": 31,
    "Adobe": 19,
    "NVIDIA": 60,
    "Uber": 37,
    "Airbnb": 10,
    "Netflix": 33,
    "PayPal": 29,
    "Spotify": 13,
    "Zoom": 4,
    "Twitter": 5,
    "Snap": 4.6,
    "Shopify": 7,
    "Dell": 102,
    "HP": 63
}

# Sort data (largest to smallest → funnel shape)
sorted_data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

companies = list(sorted_data.keys())
revenues = list(sorted_data.values())

# Plot horizontal bars (funnel style)
plt.figure(figsize=(10, 12))
plt.barh(companies, revenues)

# Invert y-axis so largest is at top
plt.gca().invert_yaxis()

plt.title("Funnel Chart: Companies by Revenue (Billion USD)")
plt.xlabel("Revenue (Billion USD)")
plt.ylabel("Companies")

plt.show()
