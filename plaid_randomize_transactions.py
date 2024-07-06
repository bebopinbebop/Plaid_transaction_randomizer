import json
import random
from datetime import datetime, timedelta

# Define the key-value pairs for logo_url and merchant_name
merchant_logo_pairs = {
    "https://d2q79iu7y748jz.cloudfront.net/s/_squarelogo/256x256/c4ed74a4a07ee5164ea0614b6f95d554": "Walmart, Inc",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUP7o5hVapDXP_84MHh6rtZJGn_K1seonPNWflKpiv8fJbn2plA6zpaCYpoN3tFK-I7Mk&usqp=CAU": "Bank of America",
    "https://plaid-merchant-logos.plaid.com/uber_1060.png": "Uber",
    "https://upload.wikimedia.org/wikipedia/commons/8/84/Venmo_logo.png": "Venmo",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Netflix_icon.svg/2048px-Netflix_icon.svg.png": "Netflix",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Square_Cash_app_logo.svg/1200px-Square_Cash_app_logo.svg.png": "Cash App",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDfzfeoopBeB3xOINf0Yh_53wmmGRaBCGSKQ&s": "Walgreens",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRO5nSeBwbI4cx837xT3wZ4Zbd8xumgMy_TfQ&s": "PayPal",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6_Lv_hwLxhylwFBDihpR82SRV1CsTqyK0rQ&s": "MTA",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRC-JnL1rAYB3BfAp9EN-PLDypaZXdc-IvcGg&s": "Amazon, Inc."
}

# Function to generate a random date within the last 6 months
def random_date():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)  # 6 months ago
    random_day = start_date + timedelta(days=random.randint(0, 180))
    return random_day.strftime('%Y-%m-%d')

# Function to generate a random amount between $10 and $200
def random_amount():
    return round(random.uniform(10.0, 200.0), 2)

# Generate 200 transactions
transactions = []
for _ in range(200):
    # Randomize amount and date
    amount = random_amount()
    date = random_date()

    # Choose a random logo_url and corresponding merchant_name
    logo_url = random.choice(list(merchant_logo_pairs.keys()))
    merchant_name = merchant_logo_pairs[logo_url]

    # Create a transaction object
    transaction = {
        "account_id": "d3F7gTmYn1bVc5xQo2r4eUg9j0l8o7Mm1Hn9l",
        "account_owner": "null",
        "amount": f"{amount}",
        "authorized_date": "2023-08-14",
        "authorized_datetime": "null",
        "category": [
            "Travel",
            "Taxi"
        ],
        "category_id": "22016000",
        "check_number": "null",
        "counterparties": [
            {
                "confidence_level": "VERY_HIGH",
                "entity_id": "eyg8o776k0QmNgVpAmaQj4WgzW9Qzo6O51gdd",
                "logo_url": logo_url,
                "name": merchant_name,
                "phone_number": "null",
                "type": "merchant",
                "website": "uber.com"
            }
        ],
        "date": date,
        "datetime": "null",
        "iso_currency_code": "USD",
        "location": {
            "address": "null",
            "city": "null",
            "country": "null",
            "lat": "null",
            "lon": "null",
            "postal_code": "null",
            "region": "null",
            "store_number": "null"
        },
        "logo_url": logo_url,
        "merchant_entity_id": "eyg8o776k0QmNgVpAmaQj4WgzW9Qzo6O51gdd",
        "merchant_name": merchant_name,
        "name": "Uber 072515 SF**POOL**",
        "payment_channel": "online",
        "payment_meta": {
            "by_order_of": "null",
            "payee": "null",
            "payer": "null",
            "payment_method": "null",
            "payment_processor": "null",
            "ppd_id": "null",
            "reason": "null",
            "reference_number": "null"
        },
        "pending": "false",
        "pending_transaction_id": "null",
        "personal_finance_category": {
            "confidence_level": "VERY_HIGH",
            "detailed": "TRANSPORTATION_TAXIS_AND_RIDE_SHARES",
            "primary": "TRANSPORTATION"
        },
        "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_TRANSPORTATION.png",
        "transaction_code": "null",
        "transaction_id": "k38rQGNWNkuW5xbRg8DpiLByvnbm77tL6NKnD",
        "transaction_type": "special",
        "unofficial_currency_code": "null",
        "website": "uber.com"
    }
    
    # Add transaction to the list
    transactions.append(transaction)

# Sort transactions by "date" field in descending order (most recent to least recent)
transactions_sorted = sorted(transactions, key=lambda x: x['date'], reverse=True)

# Save transactions to JSON file
with open('transactions.json', 'w') as f:
    json.dump(transactions_sorted, f, indent=2)

print("Transactions saved and sorted to transactions.json")
