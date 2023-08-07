def is_palindrome(input_string):
    return input_string == input_string[::-1]

# Example usage
string1 = "radar"
string2 = "hello"
print(is_palindrome(string1))
print(is_palindrome(string2))