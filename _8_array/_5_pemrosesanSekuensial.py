var_arr = [1,2,3,4,5]

for i in range(len(var_arr)) :
    current_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr) :
        next_element = var_arr[next_index]
    else :
        next_element = None

    print(f"Current element : {current_element}, next elements : {next_element}")

"""
Output :
Current element : 1, next elements : 2
Current element : 2, next elements : 3
Current element : 3, next elements : 4
Current element : 4, next elements : 5
Current element : 5, next elements : None

"""