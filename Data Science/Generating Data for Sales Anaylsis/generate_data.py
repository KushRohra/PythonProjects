import pandas as pd
import numpy
import random
import datetime
import calendar

# Product : [Price, weight]
products = {
    'iPhone': [700, 10],
    'Google Phone': [600, 8],
    'Vareebadd Phone': [400, 3],
    '20in Monitor': [109.99, 6],
    '34in Ultrawide Monitor': [379.99, 9],
    '27in 4K Gaming Monitor': [389.99, 9],
    '27in FHD Monitor': [149.99, 11],
    'Flatscreen TV': [300, 7],
    'Macbook Pro Laptop': [1700, 7],
    'ThinkPad Laptop': [999.99, 6],
    'AA Batteries (4-pack)': [3.84, 30],
    'AAA Batteries (4-pack)': [2.99, 30],
    'USB-C Charging Cable': [11.95, 30],
    'Lightning Charging Cable': [14.95, 30],
    'Wired Headphones': [11.99, 26],
    'Bose SoundSport Headphones': [99.99, 19],
    'Apple Airpods Headphones': [150, 22],
    'LG Washing Machine': [600.00, 1],
    'LG Dryer': [600.00, 1]
}

product_list = [product for product in products]
weights = [products[product][1] for product in products]

columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address']


def generate_random_time(month):
    # Generate a date in the format d/m/y H:m
    day_range = calendar.monthrange(2019, month)[1]
    random_day = random.randint(1, day_range)

    if random.random() < 0.5:
        random_date = datetime.datetime(2019, month, random_day, 12, 0)
    else:
        random_date = datetime.datetime(2019, month, random_day, 20, 0)

    time_offset = numpy.random.normal(loc=0, scale=180)
    final_date = random_date + datetime.timedelta(minutes=time_offset)

    return final_date.strftime("%m/%d/%y %H:%M")


def generate_random_address():
    street_names = ['Main', '2nd', '1st', '4th', '5th', 'Park', '6th', '7th', 'Maple', 'Pine', 'Washington', '8th',
                    'Cedar', 'Elm', 'Walnut', '9th', '10th', 'Lake', 'Sunset', 'Lincoln', 'Jackson', 'Church', 'River',
                    '11th', 'Willow', 'Jefferson', 'Center', '12th', 'North', 'Lakeview', 'Ridge', 'Hickory', 'Adams',
                    'Cherry', 'Highland', 'Johnson', 'South', 'Dogwood', 'West', 'Chestnut', '13th', 'Spruce', '14th',
                    'Wilson', 'Meadow', 'Forest', 'Hill', 'Madison']
    cities = ['San Francisco', 'Boston', 'New York City', 'Austin', 'Dallas', 'Atlanta', 'Portland', 'Portland',
              'Los Angeles', 'Seattle']
    weights = [9, 4, 5, 2, 3, 3, 2, 0.5, 6, 3]
    zips = ['94016', '02215', '10001', '73301', '75001', '30301', '97035', '04101', '90001', '98101']
    states = ['CA', 'MA', 'NY', 'TX', 'TX', 'GA', 'OR', 'ME', 'CA', 'WA']

    street = random.choice(street_names)
    city_index = random.choices(range(len(cities)), weights=weights)[0]

    return f"{random.randint(1, 999)} {street} St, {cities[city_index]}, {states[city_index]} {zips[city_index]}"


def write_row(order_id, product, order_date, address):
    price = products[product][0]

    # Geometric progression to order more if the price is less
    quantity_ordered = numpy.random.geometric(p=1.0 - (1.0 / price), size=1)[0]

    return [order_id, product, quantity_ordered, price, order_date, address]


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print(f"Execution Started at {start_time}")

    order_id = 1245

    # Generate random amount data for each month depending on the weight of the products

    for month_value in range(1, 13):
        orders_amount = 5000

        if month_value <= 10:
            # Values centered around 12000 and have a standard deviation of about 4000, i.e, 8000 <= value <= 16000
            orders_amount = int(numpy.random.normal(loc=12000, scale=4000))

        if month_value == 11:
            # Make slightly higher
            orders_amount = int(numpy.random.normal(loc=20000, scale=3000))

        if month_value == 12:
            # Make high value
            orders_amount = int(numpy.random.normal(loc=26000, scale=2500))

        df = pd.DataFrame(columns=columns)

        i = 1
        while orders_amount > 0:
            address = generate_random_address()
            order_date = generate_random_time(month_value)

            # random.choices also considers weight while picking up a choice
            product_choice = random.choices(product_list, weights=weights)[0]

            df.loc[i] = write_row(order_id, product_choice, order_date, address)
            i += 1

            if product_choice == 'iPhone':
                if random.random() < 0.15:
                    df.loc[i] = write_row(order_id, "Lightning Charging Cable", order_date, address)
                    i += 1
                if random.random() < 0.05:
                    df.loc[i] = write_row(order_id, "Apple Airpods Headphones", order_date, address)
                    i += 1
                if random.random() < 0.07:
                    df.loc[i] = write_row(order_id, "Wired Headphones", order_date, address)
                    i += 1
            elif product_choice == "Google Phone" or product_choice == "Vareebadd Phone":
                if random.random() < 0.18:
                    df.loc[i] = write_row(order_id, "USB-C Charging Cable", order_date, address)
                    i += 1
                if random.random() < 0.04:
                    df.loc[i] = write_row(order_id, "Bose SoundSport Headphones", order_date, address)
                    i += 1
                if random.random() < 0.07:
                    df.loc[i] = write_row(order_id, "Wired Headphones", order_date, address)
                    i += 1

            if random.random() <= 0.02:
                product_choice = random.choices(product_list, weights)[0]
                df.loc[i] = write_row(order_id, product_choice, order_date, address)
                i += 1

            if random.random() <= 0.002:
                df.loc[i] = columns
                i += 1

            if random.random() <= 0.003:
                df.loc[i] = ["", "", "", "", "", ""]
                i += 1

            order_id += 1
            orders_amount -= 1

        month_name = calendar.month_name[month_value]
        df.to_csv(f"./Sales data/{month_name}_data.csv")
        print(f"{month_name} finished with {len(df.index)} records")

    # Generate a random address for data

    end_time = datetime.datetime.now()
    print(f"Execution ended at {end_time}")

    print(f"Time taken to execute is {(end_time - start_time).total_seconds()}")
