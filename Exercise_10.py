# In This Step We Are Taking Input (integers) From User
reverse_number = int(input("Enter Your Intergers Numbers For Reverse Order : "))

# In This Step We Are Converting It To String For Slicing Because Slicing String is easy then Integers
result_str = str(reverse_number)[::-1]

# In This Step We Are Using Print Function To show Output And We Are using Join function to add spaces between characters
print(" ".join(result_str))
