def anagram(s1, s2):
    s1 = s1.replace(' ', '').upper()
    s2 = s2.replace(' ', '').upper()

    # Check if same number of letters
    if len(s1) != len(s2):
        return False

    # Count the frequency of each letter
    count = {}

    for letter in s1: # For every letter in the first string
        if letter in count: # If letter is already in my dictionary, then
            count[letter] += 1 # Add one to that letter key
        else:
            count[letter] = 1

    # Do reverse for the second string
    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True


x = anagram("Gill", "ill g")
print(x)