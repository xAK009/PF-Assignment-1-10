# In This Step We Are Making A Variable Name Previous to store our Previous Values
previous_number = 0
# In This Step We Are Making A Variable Name Current to store our Current Values
current_number = 1
# In This Step We Are Making A Variable Name iteration to store our iteration Values
iteration = 1
# In This Step We Are Using While Loop For Iteration
while iteration <= 10:
    print("Iteration", iteration, ":", current_number)
    temp = current_number
    current_number = previous_number + current_number
    previous_number = temp
    iteration += 1

