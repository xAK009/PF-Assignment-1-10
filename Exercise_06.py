# In This Step We Made a Random List
numbers_list = [5, 12, 9, 14, 1, 200, 21, 36, 40, 80,100,450]

# In This Step We Are Using For Loop To Iterate Through List
for divisible in numbers_list:
    # In This Step We Are Using Remainder Function To check if it is divisible by 5 And The Remainder is 0
    if divisible % 5 == 0:
        #In This Step We Are Using Print Function To Show Output
        print("Numbers Divisible By 5 : ",divisible)
