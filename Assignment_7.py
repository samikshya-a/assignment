#!/usr/bin/env python
# coding: utf-8

# 1)The re module in Python is responsible for generating Regex objects.
# 
# 2)Raw strings (prefixed with r) are often used in Regex objects because they treat backslashes (\) as literal characters rather than escape characters. Since Regex patterns often contain backslashes, using raw strings helps to avoid conflicts or unintended escape sequences.
# 
# 3)The search() method in Python's re module returns a match object if the pattern is found in the searched string. If a match is not found, it returns None.
# 
# 4)From a Match object, you can use the group() method to retrieve the actual strings that match the pattern. Calling group(0) returns the entire matched string, and you can use group(1), group(2), and so on, to retrieve the matched strings from specific groups captured by parentheses in the regex pattern.
# 
# 5)In the given regex pattern r'(\d\d\d)-(\d\d\d\d\d\d\d)':
# 
# ->Group 0 covers the entire matched string (e.g., '123-4567890').
# ->Group 1 captures the first three digits (e.g., '123').
# ->Group 2 captures the next seven digits (e.g., '4567890').
# 
# 6)To match real parentheses and periods in a regex pattern, you can escape them by prefixing them with a backslash (\). For example, to match literal parentheses, use \( and \) in the pattern. Similarly, to match a literal period, use \..
# 
# 7)The findall() method in Python's re module returns a list of strings if the regex pattern does not contain any capturing groups (parentheses). If the pattern contains capturing groups, it returns a list of tuples, where each tuple corresponds to a match and contains the captured groups.
# 
# 8)In regular expressions, the character . (dot) is a special metacharacter that matches any character except a newline.
# 
# 9)In regular expressions, the character * is a quantifier that means "zero or more occurrences" of the preceding element. It matches zero or more repetitions of the character or group preceding it.
# 
# 10)In regular expressions, the + character is a quantifier that means "one or more occurrences" of the preceding element. It matches one or more repetitions of the character or group preceding it. The * quantifier, as mentioned earlier, matches zero or more occurrences.
# 
# 11)In regular expressions, (4) represents a capturing group that captures the digit '4'. It will match the exact character '4'. On the other hand, (4,5) represents a capturing group that matches either the character '4' or the character '5'. It is essentially an expression of choice between the two characters.
# 
# 12)In regular expressions:
# 
# ->\d represents a shorthand character class that matches any digit (0-9).
# ->\w represents a shorthand character class that matches any alphanumeric character (a-z, A-Z, 0-9, and underscore _).
# ->\s represents a shorthand character class that matches any whitespace character (space, tab, newline, etc.).
# 
# 13)In regular expressions:
# ->\D represents a shorthand character class that matches any non-digit character.
# ->\W represents a shorthand character class that matches any7 non-alphanumeric character.
# ->\S represents a shorthand character class that matches any non-whitespace character
# 
# 14)The difference between .? and . in regular expressions is the behavior of the quantifier.
# -->.*? is a non-greedy quantifier that matches as few characters as possible, allowing for a successful match. It will match any character (except a newline) zero or more times, but it tries to match the minimum number of characters necessary to satisfy the pattern.
# -->.* is a greedy quantifier that matches as many characters as possible. It will match any character (except a newline) zero or more times, trying to match as many characters as possible while still allowing for a successful match.
# For example, given the input string "abcdefg", the pattern a.g will match the entire string, while a.?g will only match "abcdefg" (minimum match).
# 
# 15)The syntax for matching both numbers and lowercase letters with a character class in regular expressions is [a-z0-9]. This character class will match any lowercase letter (a to z) or any digit (0 to 9).
# 
# 16)To make a regular expression case-insensitive, you can use the re.IGNORECASE flag or the (?i) inline flag.
# 
# Here are the two approaches:
# ->Using the re.IGNORECASE flag: You can pass re.IGNORECASE as the second argument to the re.compile() function or as the optional flags argument to other regex functions. For example: re.compile(pattern, re.IGNORECASE).
# ->Using the inline flag (?i): You can include (?i) at the beginning of the regular expression pattern. For example: pattern = "(?i)regex".
# Both methods will make the regular expression match regardless of the case of the letters.
# 
# 17)In regular expressions, the . (dot) character normally matches any character except a newline character. However, if re.DOTALL is passed as the second argument to re.compile(), it changes the behavior of the dot. In this case, the dot will match any character, including a newline character.
# 
# 18)Given the code numRegex = re.compile(r'\d+'), calling numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') will return the string 'X drummers, X pipers, five rings, X hen'. The sub() method replaces all occurrences of the pattern (one or more digits) in the input string with the replacement string ('X').
# 
# 19)Passing re.VERBOSE as the second argument to re.compile() allows you to write regular expressions with comments and whitespace. It enables verbose mode, which ignores whitespace and treats the # character as the start of a comment until the end of the line. This feature improves the readability and maintainability of complex regular expressions by allowing you to add comments and break down the expression into multiple lines

# QUESTION 20

# In[1]:


import re
regex = r"^\d{1,3}(,\d{3})*$"
test_cases= ['42','1,234','6,368,745','12,34,567','1234']
for test_case in test_cases:
    if re.match(regex,test_case):
        print(f"{test_case} matches the pattern")
    else:
        print(f"{test_case} does not match the pattern")


# QUESTION 21

# In[2]:


import re

regex = r"^[A-Z][a-z]*\sWatanabe$"
test_cases = ['Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe', 'haruto Watanabe', 'Mr. Watanabe', 'Watanabe', 'Haruto watanabe']
for test_case in test_cases:
    if re.match(regex, test_case):
        print(f"{test_case} matches the pattern")
    else:
        print(f"{test_case} does not match the pattern")


# QUESTION 22

# In[4]:


import re

regex = r"^(Alice|Bob|Carol)\s+(eats|pets|throws)\s+(apples|cats|baseballs)\.$"
test_cases = ['Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.', 'Alice throws Apples.', 'BOB EATS CATS.', 'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.']
for test_case in test_cases:
    if re.match(regex, test_case, re.IGNORECASE):
        print(f"{test_case} matches the pattern")
    else:
        print(f"{test_case} does not match the pattern")


# In[ ]:




