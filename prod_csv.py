import sys
import os
import pandas as pd

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InventoryManage.settings')
import django
django.setup()

# Import your Django model
from dashboard.models import Product

def save_data_from_row(row):
    # Create an instance of your model
    obj = Product()

    # Assign values from the CSV row to model fields
    obj.product_name = row['ProductName']
    obj.brand = row['Brand']
    obj.price = float(row['Price'])
    obj.discount_price = float(row['DiscountPrice'])
    obj.image_url = row['Image_Url']
    obj.category = row['Category']
    obj.sub_category = row['SubCategory']
    obj.absolute_url = row['Absolute_Url']
    obj.sold = int(row['Sold'])
    obj.temperature = row['Temperature']
    obj.quantity_value = float(row['quantity_value'])
    obj.quantity_type = row['quantity_type']

    # Save the object to the database
    obj.save()

    print("Added data from row:", row)

if __name__ == "__main__":
    file_path = 'updated_file.csv'

    try:
        print("Adding data from file:", file_path)
        df = pd.read_csv(file_path)
        df.apply(lambda row: save_data_from_row(row), axis=1)
    except FileNotFoundError:
        print("File not found")
