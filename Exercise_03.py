# We Are Taking Input From User In This Step

input_string = input("Enter a string: ")

# We Are Making A Variable To Store Position (Index) U can Name it Anything You Want In This Step

index = 0

# In This Step We Are Making An Empty String To Store Our Even Characters

even_characters = ""

# In This Step We Are Using While Loop For Iteration Of Every Character Of A String
while index < len(input_string):
    # In This Step We Are Checking If The Index Is Even Or Odd Or Anything
    if index % 2 == 0:
        #In This Step we are using += operator to connect or join the right hand side with the left hand side
        #and we are using "f" string to add quotation marks between the results its not necessary u can remove it if u want
        even_characters = even_characters + input_string[index]
    # In This Step We Are Adding +1 to the index for each iteration until it becomes equal to the string length
    index = index + 1

# In This Step We Are Using Print Statement To Show Results
print("Characters at even index positions :",even_characters)
