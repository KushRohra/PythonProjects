import pandas as pd
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter


def combine_all_data():
    all_months_data = pd.DataFrame()  # Initializing a new Data Frame

    files = [file for file in os.listdir('./Sales_Data')]
    for file in files:
        df = pd.read_csv("./Sales_Data/" + file)  # Read from a csv file
        all_months_data = pd.concat([all_months_data, df])  # Concat one data frame to another

    all_months_data.to_csv("all_data.csv", index=False)

    return all_months_data


def cleanup_data(all_data):
    # (Drop Rows of NaN)
    all_data = all_data.dropna(how='all')

    # Filter rows which are not equal to Or as initials of Order Date
    all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

    # Convert Column to the correct type (to_numeric automatically takes care of data type)
    all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
    all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

    return all_data


def monthly_sales_task(all_data):
    monthly_sales = all_data.groupby('Month').sum()
    months = range(1, 13)

    plt.bar(months, monthly_sales['Sales'])
    plt.xticks(months)
    plt.ylabel('Sales in USD($)')
    plt.xlabel('Month Number')
    plt.show()


def city_with_highest_sales(all_data):
    # Add a city Column also with the state
    all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{x.split(',')[1]} ({x.split(',')[2].split(' ')[1]})")
    city_sales = all_data.groupby('City').sum()

    cities = [city for city, df in all_data.groupby('City')]
    plt.bar(cities, city_sales['Sales'])
    plt.xticks(cities, rotation='vertical')
    plt.ylabel('Sales in USD($)')
    plt.xlabel('Month Number')
    plt.show()


def best_time_to_advertise(all_data):
    # Convert to DateTime Object
    all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

    # Extract Hour and Minute from Order Date
    all_data['Hour'] = all_data['Order Date'].dt.hour
    all_data['Minute'] = all_data['Order Date'].dt.minute

    hours = [hour for hour, df in all_data.groupby('Hour')]
    plt.plot(hours, all_data.groupby(['Hour']).count())
    plt.xticks(hours)
    plt.xlabel('Hours')
    plt.ylabel('Number of Orders')
    plt.grid()
    plt.show()


def items_ordered_together(all_data):
    df = all_data[all_data['Order ID'].duplicated(keep=False)]
    '''
        keep = first, last, false
        first => first copy of duplicate entry
        last => last copy of duplicate entry
        false => all copy of duplicate entry
    '''
    df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

    # Remove duplicate pairs
    df = df[['Order ID', 'Grouped']].drop_duplicates()

    count = Counter()

    for row in df['Grouped']:
        row_list = row.split(',')
        # here 2 specifies how many items we want to group, could use 3 or 4
        count.update(Counter(combinations(row_list, 2)))

    for key, value in count.most_common():
        print(key, value)


def most_sold_product(all_data):
    product_group = all_data.groupby('Product')
    quantity_ordered = product_group.sum()['Quantity Ordered']

    prices = all_data.groupby('Product').mean()['Price Each']
    products = [product for product, df in product_group]

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.bar(products, quantity_ordered, color='g')
    ax2.plot(products, prices, 'b-')
    ax1.set_xticklabels(products, rotation='vertical', size=8)
    ax1.set_xlabel('Product Name')
    ax1.set_ylabel('Quantity Ordered', color='g')
    ax2.set_ylabel('Price in USD($)', color='b')

    plt.show()


def main():
    all_data = combine_all_data()

    # Clean up data
    all_data = cleanup_data(all_data)

    # TASK 1 => Add a separate month column to the dataset
    all_data['Month'] = all_data['Order Date'].str[0:2]
    all_data['Month'] = all_data['Month'].astype('int32')

    # TASK 2 => Add a sales column (Quantity Ordered * Price of each)
    all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

    # TASK 3 => Best month for sales and money earned in that month
    monthly_sales_task(all_data)

    # TASK 4 => City with highest number of sales
    city_with_highest_sales(all_data)

    # TASK 5 => Best time to advertise
    ''' Aggregate Order Dates into a 24-hour period. Simple parse could lead to errors so use datetime object '''
    best_time_to_advertise(all_data)

    # TASK 6 => What products are often most sold together
    ''' Products with same Order Id are ordered together at the same location '''
    items_ordered_together(all_data)

    # TASK 7 => What products sold the most and why do you think it did?
    most_sold_product(all_data)


if __name__ == "__main__":
    main()
