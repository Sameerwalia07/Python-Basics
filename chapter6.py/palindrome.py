def check_palindrome(str):
    
    #cleaning the string i.e removing spaces
    clean_str = str.replace(" ", "").lower()
    
    reverse_str = clean_str[::-1]
    
    return clean_str == reverse_str

str = input("Enter a string :")
#print(check_palindrome(str))
if(check_palindrome(str)):
    print("It is a palindrome")
    
else:
    print("It is not a palindrome")