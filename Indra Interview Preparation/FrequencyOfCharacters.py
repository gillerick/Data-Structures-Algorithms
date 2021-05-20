s = input("Enter String\n")
cache = {}

# Initialize all frequencies to 0
for char in s:
    cache[char] = 0

# Add frequencies for every recurrence
for char in s:
    cache[char] += 1

# Display frequencies
for k, v in cache.items():
    print(k, v)
