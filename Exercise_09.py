# In This Step we are creating 2 lists one Odd Numbers and one Even Numbers
mix_list1 = [1, 3, 4, 6, 5, 6, 7, 8, 9, 11, 12, 13, 14]
mix_list2 = [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17]

# In This Step We are making a new Empty List
new_list = []

# In This Step We Are using For Loop For iteration And using if condition to store only Odd numbers and Append it to new list
for num in mix_list1:
    if num % 2 == 1:
        new_list.append(num)

# In This Step We Are using For Loop For iteration And using if condition to store only Even numbers and Append it to new list
for num in mix_list2:
    if num % 2 == 0:
        new_list.append(num)

# In This Step We Are using Print Function to show show Output
print("Our New List Contains : ",new_list)
