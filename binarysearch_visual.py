"""
BINARY SEARCH VISUAL EXPLANATION
=================================

Binary Search works by repeatedly dividing the search space in half.
It requires a SORTED list/array to work correctly.

HOW IT WORKS:
-------------
1. Start with two pointers: low (start) and high (end)
2. Calculate middle index: mid = (low + high) // 2
3. Compare the middle element with target:
   - If equal → FOUND! Return index
   - If middle > target → search LEFT half (set high = mid - 1)
   - If middle < target → search RIGHT half (set low = mid + 1)
4. Repeat until found or low > high (not found)

VISUAL EXAMPLE - Searching for 3 in [1, 3, 5, 7, 9]:
----------------------------------------------------

Initial state:
  Index:  0  1  2  3  4
  Value: [1, 3, 5, 7, 9]
          ↑     ↑     ↑
        low   mid   high
        (low=0, mid=2, high=4)

Step 1: Check middle element at index 2
  list[2] = 5
  5 > 3? YES → Search LEFT half
  New bounds: low=0, high=1

  Index:  0  1  2  3  4
  Value: [1, 3, 5, 7, 9]
          ↑  ↑
        low mid,high
        (low=0, mid=0, high=1)

Step 2: Check middle element at index 0
  list[0] = 1
  1 < 3? YES → Search RIGHT half
  New bounds: low=1, high=1

  Index:  0  1  2  3  4
  Value: [1, 3, 5, 7, 9]
             ↑
          low,mid,high
        (low=1, mid=1, high=1)

Step 3: Check middle element at index 1
  list[1] = 3
  3 == 3? YES → FOUND! Return index 1

VISUAL EXAMPLE - Searching for -1 in [1, 3, 5, 7, 9]:
-----------------------------------------------------
(NOT FOUND case)

Initial state:
  Index:  0  1  2  3  4
  Value: [1, 3, 5, 7, 9]
          ↑     ↑     ↑
        low   mid   high

Step 1: Check middle element at index 2
  list[2] = 5
  5 > -1? YES → Search LEFT half
  New bounds: low=0, high=1

Step 2: Check middle element at index 0
  list[0] = 1
  1 > -1? YES → Search LEFT half
  New bounds: low=0, high=-1

Step 3: low (0) > high (-1)? YES → NOT FOUND, return None

TIME COMPLEXITY: O(log n) - Very efficient!
SPACE COMPLEXITY: O(1) - Only uses a few variables
"""

def binary_search_visual(list, item):
    """
    Binary search with step-by-step visualization
    """
    low = 0
    high = len(list) - 1
    step = 1
    
    print(f"\n{'='*60}")
    print(f"Searching for {item} in {list}")
    print(f"{'='*60}\n")
    
    # Create visual representation
    def print_state(low, mid, high, step_num):
        print(f"Step {step_num}:")
        print(f"  Indices: ", end="")
        for i in range(len(list)):
            print(f"{i:^4}", end="")
        print()
        print(f"  Values: ", end="")
        for i in range(len(list)):
            print(f"{list[i]:^4}", end="")
        print()
        print(f"  Pointers:", end="")
        for i in range(len(list)):
            if i == low == mid == high:
                print(f"{'low,mid,high':^4}", end="")
            elif i == low == mid:
                print(f"{'low,mid':^4}", end="")
            elif i == mid == high:
                print(f"{'mid,high':^4}", end="")
            elif i == low:
                print(f"{'low':^4}", end="")
            elif i == mid:
                print(f"{'mid':^4}", end="")
            elif i == high:
                print(f"{'high':^4}", end="")
            else:
                print(f"{'':^4}", end="")
        print()
        print(f"  low={low}, mid={mid}, high={high}")
        print()
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        
        print_state(low, mid, high, step)
        print(f"  Checking list[{mid}] = {guess}")
        
        if guess == item:
            print(f"  ✓ FOUND! {item} is at index {mid}")
            print(f"{'='*60}\n")
            return mid
            
        if guess > item:
            print(f"  {guess} > {item} → Search LEFT half")
            high = mid - 1
        else:
            print(f"  {guess} < {item} → Search RIGHT half")
            low = mid + 1
        
        step += 1
        print()
    
    print(f"  ✗ NOT FOUND: {item} is not in the list")
    print(f"{'='*60}\n")
    return None

# Examples
if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    
    # Example 1: Item found
    binary_search_visual(my_list, 3)
    
    # Example 2: Item not found
    binary_search_visual(my_list, -1)
    
    # Example 3: Another search
    binary_search_visual(my_list, 7)

