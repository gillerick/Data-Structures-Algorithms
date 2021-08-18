import math


def calculate_total_price(prices, discount):
    prices = sorted(prices)
    max_price = prices[-1]
    discounted_price = max_price * (1 - discount)
    total_price = 0

    for p in range(0, len(prices) - 1):
        total_price += p
    total_price += max_price
    return math.ceil(total_price)


if __name__ == "__main__":
    prices = [123, 45, 678, 678, 890]
    discount = 10
    print(calculate_total_price(prices, discount))
