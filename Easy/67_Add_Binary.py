'''
Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

a = "11"
b = "1"

carry = 0
res = ""
# Pad the shorter number with zeros to make their lengths equal
max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)

# Iterating through the digits in reverse order
for i in range(max_len - 1, -1, -1):
    int_a = int(a[i])
    int_b = int(b[i])
    # Performing binary addition
    temp_sum = int_a + int_b + carry
    # Appending the least significant bit of the sum
    res = str(temp_sum % 2) + res
    carry = temp_sum // 2  # Updating the carry
# If there's a carry after processing all digits, append it to the result
if carry == 1:
    res = "1" + res


print(res)
