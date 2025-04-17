import numpy as np
import argparse
import uuid
import pandas as pd
import datetime
from typing import List, Dict

# Define menu items with fixed prices
MENU_ITEMS = {
    'Burger': 10.99,
    'Pizza': 15.99,
    'Salad': 8.99,
    'Pasta': 12.99,
    'Sandwich': 9.99,
    'Drink': 2.99,
    'Dessert': 5.99,
    'Appetizer': 7.99
}

def generate_fake_data(number_of_days: int, number_of_stores: int) -> pd.DataFrame:
    """Generates fake data for restaurant operations simulation.
    Args:
        number_of_days (int): Number of days to generate data for.
        number_of_stores (int): Number of stores.
    Returns:
        pd.DataFrame: DataFrame containing fake transaction data.
    """
    # Start from January 1st of current year
    start_date = datetime.datetime(datetime.datetime.now().year, 1, 1)
    data = []

    for day in range(number_of_days):
        current_date = start_date + datetime.timedelta(days=day)
        
        # Each store will have 50-200 transactions per day
        for store_id in range(1, number_of_stores + 1):
            num_transactions = np.random.randint(50, 200)
            
            for _ in range(num_transactions):
                # Generate random timestamp within the day
                hours = np.random.randint(6, 23)  # Operating hours 6 AM to 11 PM
                minutes = np.random.randint(0, 60)
                seconds = np.random.randint(0, 60)
                timestamp = current_date.replace(hour=hours, minute=minutes, second=seconds)
                
                # Generate 1-5 items per transaction
                items_count = np.random.randint(1, 6)
                items: List[str] = np.random.choice(list(MENU_ITEMS.keys()), items_count).tolist()
                
                # Calculate total price
                total_price = sum(MENU_ITEMS[item] for item in items)
                
                transaction = {
                    'timestamp': timestamp,
                    'store_id': store_id,
                    'items_sold': ' '.join(items),
                    'price': round(total_price, 2),
                    'transaction_id': str(uuid.uuid4())
                }
                data.append(transaction)
    
    # Convert to DataFrame and sort by timestamp
    df = pd.DataFrame(data)
    df = df.sort_values('timestamp')
    return df

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate fake data for restaurant operations simulation.")
    parser.add_argument("--number_of_days", type=int, default=30, help="Number of days to generate data for.")
    parser.add_argument("--number_of_stores", type=int, default=50, help="Number of stores.")
    parser.add_argument("--output", type=str, default="restaurant_transactions.csv", help="Output file name (CSV format)")

    args = parser.parse_args()
    
    # Generate fake data
    df = generate_fake_data(args.number_of_days, args.number_of_stores)
    
    # Save to CSV
    df.to_csv(args.output, index=False)
    print(f"Generated {len(df)} transactions and saved to {args.output}")

if __name__ == "__main__":
    main()