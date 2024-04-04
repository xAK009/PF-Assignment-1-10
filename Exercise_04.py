# In This Step We Are asking USER to input a String
input_string = input("Enter a string : ")
# In This Step We Are asking USER to input an Ingeter (n) Value To Remove
input_n = int(input("Enter the number of characters to remove : "))

# # In This Step We Are Checking If The Input (n) Value is Less Than The Length Of The String
if input_n < len(input_string):
    result = input_string[input_n:]
    print("Your Given Output Is:", result)
else:
    print("Input Is Invalid Because n must be less than the length of the string.")
