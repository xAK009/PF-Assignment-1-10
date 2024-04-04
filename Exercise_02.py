# In This Step We Are Making A Variable Name Previous to store our Previous Values
previous = 0
# In This Step We Are Making A Variable Name Current to store our Current Values
current = 1
# In This Step We Are Using While Loop For Iteration
while previous<=10:
    # In This Step We Are Adding Both Values
    sum=current + previous
    print("Current number:", current, "Previous number:", previous, "Sum:", sum)
    # In This Step We Are Adding +1 to Both Values so That the values Changes For Next Iteration
    current=current + 1
    previous = previous + 1
