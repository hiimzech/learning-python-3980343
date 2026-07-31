# Python code​​​​​​‌‌‌‌‌‌‌‌​‌‌‌​‌‌​‌​​‌​​‌‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False


def is_palindrome(teststr):
    # Your code goes here.
    newstr = str(teststr).lower().strip()   
    newstr = str.replace(newstr," ","")    

    palindrome = str("")
    rpalindrome = str("")

    for x in newstr:       
      if x.isalpha():
        palindrome = palindrome + x

    #print(palindrome)

    for i in range(len(palindrome)-1,-1,-1):
       rpalindrome = rpalindrome + palindrome[i]       
    
    #rpalindrome = palindrome[::-1]
    #print(rpalindrome)

    if rpalindrome == palindrome:    
       return True
    
    return False

# This is how your code will be called.
# Your answer should determine whether a string is a palindrome.
# You can edit this code to try different testing cases.

test_word = "Madam, I'm Adam."
print(is_palindrome(test_word))

# try using some of these other words:
test_word = "RACE CAR!"
print(is_palindrome(test_word))

test_word = "Hello, world"
print(is_palindrome(test_word))

test_word = "Radar?"
print(is_palindrome(test_word))

test_word = "A man, a plan, a canal Panama!"
print(is_palindrome(test_word))