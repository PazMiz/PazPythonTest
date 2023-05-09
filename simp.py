# simp.py

# This function COMBINE + num1 and num2 together and returns the final result
def simp_function(num1, num2):
    return num1 + num2

# This function doing MINUS - for num2 & num1 and returns the final result.
def minus_numbers(num1, num2):
    return num1 - num2

if __name__ == "__main__":
    result1 = simp_function(10,20)
    print(result1)  # result: 20

    result2 = minus_numbers(20, 5)
    print(result2)  # result: 15
