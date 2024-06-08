s = "MCMXCIV"
num = 0
length = len(s)
roman_to_int = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
for i in range(length):
    # If the current value is less than the next value, subtract current value
    if i + 1 < length and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
        num -= roman_to_int[s[i]]
    else:
        num += roman_to_int[s[i]]
print(num)
