# In This Step We Are Using Input Function To Ask User To Specify Rows
input_rows = int(input("Enter Your Rows Numbers : "))

# In This Step We Are using for loop for iteration And Range Function
for rows in range(1, input_rows + 1):
    # In This Step We Are Using Print Function To Show Output
    print(*[rows]*rows)
