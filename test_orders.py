import unittest
import pandas as pd
from datetime import datetime
from order_analysis import read_orders_csv, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, identify_top_customers

class TestOrderAnalysis(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.sample_data = {
            'order_id': [1, 2, 3],
            'customer_id': ['C101', 'C102', 'C103'],
            'order_date': ['2023-01-15', '2023-01-16', '2023-02-10'],
            'product_id': ['P001', 'P002', 'P001'],
            'product_name': ['Product_A', 'Product_B', 'Product_A'],
            'product_price': [20.0, 30.0, 20.0],
            'quantity': [2, 1, 3]
        }
        self.orders_df = pd.DataFrame(self.sample_data)

    def test_read_orders_csv(self):
        # Test read_orders_csv function
        orders_df = read_orders_csv('orders.csv')
        self.assertIsNotNone(orders_df)
        self.assertTrue('order_id' in orders_df.columns)

    def test_compute_monthly_revenue(self):
        # Test compute_monthly_revenue function
        self.orders_df['order_date'] = pd.to_datetime(self.orders_df['order_date'])
        self.orders_df['month'] = self.orders_df['order_date'].dt.to_period('M')
        monthly_revenue = compute_monthly_revenue(self.orders_df)
        self.assertEqual(monthly_revenue.iloc[0], 70.0)  # January total revenue

    def test_compute_product_revenue(self):
        # Test compute_product_revenue function
        product_revenue = compute_product_revenue(self.orders_df)
        self.assertEqual(product_revenue['Product_A'], 100.0)  # Total revenue for Product_A

    def test_compute_customer_revenue(self):
        # Test compute_customer_revenue function
        customer_revenue = compute_customer_revenue(self.orders_df)
        self.assertEqual(customer_revenue['C101'], 40.0)  # Total revenue for customer C101

    def test_identify_top_customers(self):
        # Test identify_top_customers function
        customer_revenue = compute_customer_revenue(self.orders_df)
        top_customers = identify_top_customers(customer_revenue)
        self.assertEqual(top_customers.iloc[0], 60.0)  # Top customer's revenue

if __name__ == '__main__':
    unittest.main()

