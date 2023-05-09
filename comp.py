def comp_function(num): 
    num_str = str(num)
    total_result = 0
    for digit in num_str:
        total_result += int(digit)
    return total_result
print(comp_function(55555))  # result is : 25


def reserve_palindrome(num): 
    num_string = str(num)
    return num_string == num_string[::-1] # sliced the numbers with ::-1
print(reserve_palindrome(1331))  # result : True cause it cannot be reserved

if __name__ == "__main__":

    def comp_function():
        print("This is a function in comp module.")
