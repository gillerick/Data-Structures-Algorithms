def repeated_string(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


if __name__ == "__main__":
    print(repeated_string('aba', 10))
