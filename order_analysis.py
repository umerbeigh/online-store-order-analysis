import pandas as pd
from datetime import datetime

def read_orders_csv(file_path):
    try:
        orders_df = pd.read_csv(file_path)
        return orders_df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def compute_monthly_revenue(orders_df):
    try:
        # Convert 'order_date' to datetime explicitly
        orders_df['order_date'] = pd.to_datetime(orders_df['order_date'], errors='coerce')

        # Drop rows with NaT (Not a Time) values after conversion
        orders_df = orders_df.dropna(subset=['order_date'])

        # Include quantity in revenue calculation
        orders_df['revenue'] = orders_df['product_price'] * orders_df['quantity']
        
        # Compute monthly revenue
        monthly_revenue = orders_df.groupby(orders_df['order_date'].dt.to_period('M'))['revenue'].sum()
        return monthly_revenue
    except Exception as e:
        print(f"Error computing monthly revenue: {e}")
        return None

def compute_product_revenue(orders_df):
    try:
        # Include quantity in revenue calculation
        orders_df['revenue'] = orders_df['product_price'] * orders_df['quantity']
        
        # Compute product revenue
        product_revenue = orders_df.groupby('product_name')['revenue'].sum()
        return product_revenue
    except Exception as e:
        print(f"Error computing product revenue: {e}")
        return None

def compute_customer_revenue(orders_df):
    try:
        # Include quantity in revenue calculation
        orders_df['revenue'] = orders_df['product_price'] * orders_df['quantity']
        
        # Compute customer revenue
        customer_revenue = orders_df.groupby('customer_id')['revenue'].sum()
        return customer_revenue
    except Exception as e:
        print(f"Error computing customer revenue: {e}")
        return None

def identify_top_customers(customer_revenue):
    try:
        top_customers = customer_revenue.nlargest(10)
        return top_customers
    except Exception as e:
        print(f"Error identifying top customers: {e}")
        return None

if __name__ == "__main__":
    # Read orders data
    file_path = 'orders.csv'
    orders_df = read_orders_csv(file_path)

    if orders_df is not None:
        # Task 1: Compute monthly revenue
        monthly_revenue = compute_monthly_revenue(orders_df)
        if monthly_revenue is not None:
            print("Monthly Revenue:\n", monthly_revenue)

        # Task 2: Compute product revenue
        product_revenue = compute_product_revenue(orders_df)
        if product_revenue is not None:
            print("\nProduct Revenue:\n", product_revenue)

        # Task 3: Compute customer revenue
        customer_revenue = compute_customer_revenue(orders_df)
        if customer_revenue is not None:
            print("\nCustomer Revenue:\n", customer_revenue)

        # Task 4: Identify top 10 customers
        top_customers = identify_top_customers(customer_revenue)
        if top_customers is not None:
            print("\nTop 10 Customers:\n", top_customers)

