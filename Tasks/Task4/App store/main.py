from login_system import LoginSystem
from product import Product
from store import Store

def make_products():
    """
    builds the starting list of electronic products for the store
    returns:
    list: a list of Product objects
    """
    products = [
    Product("MacBook Air M3", 1299, 10),
    Product("iPhone 16", 999, 15),
    Product("Samsung Galaxy S25", 899, 12),
    Product("iPad Air", 599, 8),
    Product("Apple Watch Series 10", 399, 10),
    Product("Sony WH-1000XM5 Headphones", 349, 20),
    Product("Logitech MX Master 3S Mouse", 99, 18),
    Product("Keychron K2 Keyboard", 89, 14),
    Product("Dell UltraSharp U2723QE Monitor", 549, 6),
    Product("Samsung T9 Portable SSD 1TB", 149, 16),
    Product("Anker 737 Power Bank", 129, 25),
    Product("GoPro HERO13 Black", 399, 7),
    Product("Canon EOS R50 Camera", 679, 5),
    Product("PlayStation 5 Slim", 499, 9),
    Product("Nintendo Switch OLED", 349, 11),

    ]
    return products


def main():
    #runs the whole program,the login flow first, then the store
    login_system = LoginSystem("Engy", "engy1234?")
    login_system.login()

    products = make_products()
    store = Store(products)
    store.start()


if __name__ == "__main__":
    main()