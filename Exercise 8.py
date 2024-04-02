# In This Step We Are Taking Input (integers) From User For Any Number
palindrome_numbers = int(input("Enter Your Intergers Numbers For Reverse Order : "))

# In This Step We Are Converting It To String For Slicing Because Slicing String is easy then Integers
palindrome_str = str(palindrome_numbers)

# In This Step We Are Using If & Else Condition To Check If The Given Number is Palindromic Or Not
if palindrome_str == palindrome_str[::-1]:
    print("The Given Number is a Palindrome Number")
else:
    print("The Given Number is Not a Palindrome Number")
