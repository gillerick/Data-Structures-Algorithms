def factors(number):
    _factors = []
    for i in range(2, number):
        if number % i == 0:
            _factors.append(i)
    return _factors


if __name__ == "__main__":
    print(factors(15))
    print(factors(12))
    print(factors(13))
