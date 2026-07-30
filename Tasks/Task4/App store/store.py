class Store:
    """
    handles the whole shopping flow, from showing the products to picking items, working out discounts, adding a delivery or pick-up charge, changing the currency, and finishing the order
    attributes:
    products (list): the list of Product objects for sale
    order_list (list): the items the customer has added so far
    """
    CURRENCY_RATES = {
        "USD": 1.0,
        "EUR": 0.92,
        "EGP": 48.0,
    }

    def __init__(self, products):
        self.products = products
        self.order_list = []

    def show_products(self):
        #prints the products in a table with the name, price, and how much stock is left for each one
        print("Name\tPrice\tStock")
        for item in self.products:
            print(item.name + "\t" + str(item.price) + "\t" + str(item.stock))

    def find_product(self, name):
        """
        looks for a product with the given name in the product list
        args:
        name (str): the name to look for
        returns:
        Product: the item if it is found, otherwise none
        """
        for item in self.products:
            if item.name.lower() == name.lower():
                return item
        return None

    def choose_product(self):
        """
        asks the customer for a product name and keeps asking until they type a real one from the list
        returns:
        Product: the item the customer picked
        """
        name = input("Enter the product name you want to purchase: ")
        item = self.find_product(name)
        while item is None:
            name = input("Sorry, This Product is not found. Enter a valid product name: ")
            item = self.find_product(name)
        return item

    def choose_quantity(self, item):
        """
        asks the customer how many they want and keeps asking until that amount is actually in stock
        args:
        item (Product): the product being bought
        returns:
        int: the amount the customer picked
        """
        amount = int(input("Enter the quantity you want to purchase: "))
        while amount > item.stock or amount <= 0:
            amount = int(input("Sorry, the requested quantity is not available. Please enter a different quantity: "))
        return amount

    def work_out_discount(self, amount, price):
        """
        works out the discount and the price after that discount,the customer gets 5% off for every 5 units bought, up to a highest discount of 25%
        args:
        amount (int): how many units were bought
        price (float): the price of one unit
        returns:
        tuple: the discount percent and the price after it
        """
        discount = (amount // 5) * 5
        if discount > 25:
            discount = 25
        price_before = price * amount
        price_after = price_before * (1 - discount / 100)
        return discount, price_after

    def add_item_to_order(self):
       # runs the full add-item flow, picking a product,choosing a quantity,working out the discount, taking it out of stock and adding it to the order list, then shows the discounted price to the customer
        item = self.choose_product()
        amount = self.choose_quantity(item)
        discount, price_after = self.work_out_discount(amount, item.price)
        item.take_from_stock(amount)

        order_item = {
            "name": item.name,
            "amount": amount,
            "discount": discount,
            "price": price_after,
        }
        self.order_list.append(order_item)

        print("Discount applied:", discount, "%")
        print("Price after discount for", item.name, ":", price_after)

    def wants_more_items(self):
        """
        asks the customer if they want to add another product to their order
        returns:
        bool: true if they want to add another one, false if not
        """
        answer = input("Do you want to add another product? (yes/no): ")
        return answer.lower() == "yes"

    def get_shipping_cost(self):
        """
        asks the customer to pick delivery or pick-up and gives back the matching charge
        returns:
        float: 200 for delivery, or 50 for pick-up
        """
        choice = input("Choose delivery or pick-up: ")
        while choice.lower() not in ("delivery", "pick-up"):
            choice = input("Invalid choice. Choose delivery or pick-up: ")
        if choice.lower() == "delivery":
            return 200
        return 50

    def choose_currency(self):
        """
        asks the customer to pick a currency to pay with, if the one they type is not supported it falls back to usd
        returns:
        str: the currency code they end up with usd or eur or egp
        """
        currency = input("Select currency (USD, EUR,EGP): ").upper()
        if currency not in self.CURRENCY_RATES:
            print("Invalid currency. Defaulting to USD.")
            currency = "USD"
        return currency

    def get_total(self, shipping_cost, currency):
        """
        works out the final total for the order, adding up every discounted item plus the delivery or pick-up charge, then converts it into the chosen currency
        args:
        shipping_cost (float): the delivery or pick-up charge
        currency (str): the chosen currency code
        returns:
        float: the final total in the chosen currency
        """
        subtotal = 0
        for order_item in self.order_list:
            subtotal += order_item["price"]
        total_usd = subtotal + shipping_cost
        rate = self.CURRENCY_RATES[currency]
        return total_usd * rate

    def finish_order(self, total, currency):
        """
        shows the final total price and lets the customer know the order has been sent off
        args:
        total (float): the final total to show
        currency (str): the currency code the total is in
        """
        print("Final total price:", total, currency)
        print("Your order is on its way. Thank you for your purchase.")

    def start(self):
        #runs the whole store flow, from showing the products all the way to finishing the order
        self.show_products()

        keep_adding = True
        while keep_adding:
            self.add_item_to_order()
            keep_adding = self.wants_more_items()

        shipping_cost = self.get_shipping_cost()
        currency = self.choose_currency()
        total = self.get_total(shipping_cost, currency)
        self.finish_order(total, currency)