import simp
import comp

# Flag to keep track of whether a function in simp module has been called
simp_module_called = False


def enforce_rule():
    if not simp_module_called:
        raise Exception("You must call at least one function in the simp module before calling functions in the comp module.")


def call_simp_function(num1, num2):
    global simp_module_called
    simp.simp_function(num1, num2)
    simp_module_called = True


def call_comp_function(num):
    enforce_rule()
    comp.comp_function(num)

# Test case 1: Calling comp before calling simp_function should raise an exception
simp_module_called = False
try:
    call_comp_function(42)
    call_simp_function(10, 20)
 
except Exception as e:
    print(f"Exception occurred: {e}")
