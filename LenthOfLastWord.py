#leetcode problems
#Given a string s consisting of words and spaces,
#  return the length of the last word in the string.
def length_of_last_word(s):
    words = s.split()
    if words:
        return len(words[-1])
    return 0

# مثال استفاده
input_str = input('give me a string? ')
print(length_of_last_word(input_str))
