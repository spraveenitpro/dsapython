def iterative_factorial(n):
    #print(f"Starting iterative_factorial({n})")
    factorial = 1
    print(f"Initial factorial = {factorial}")
    for i in range( 2, n+1):
        #print(f"Loop iteration: i = {i}")
        #print(f"Before: factorial = {factorial}")
        factorial = factorial * i
    return factorial


print(iterative_factorial(4))

def recursive_factorial(n):
    print(f"  " * (5-n) + f"Entering recursive_factorial({n})")
    if n == 1:
        print(f"  " * (5-n) + f"Base case reached: n = {n}, returning 1")
        return 1
    else:
        print(f"  " * (5-n) + f"Recursive case: n = {n}, calling recursive_factorial({n-1})")
        temp = recursive_factorial(n-1)
        print(f"  " * (5-n) + f"Got temp = {temp} from recursive_factorial({n-1})")
        result = n * temp
        print(f"  " * (5-n) + f"Calculating: {n} * {temp} = {result}")
        print(f"  " * (5-n) + f"Returning {result} from recursive_factorial({n})")
        return result

print(recursive_factorial(4))