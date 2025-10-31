"""
ANIMATED BINARY SEARCH VISUALIZATION
====================================
Shows binary search algorithm with animated, frame-by-frame visualization
"""

import time
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def animate_binary_search(arr, target, delay=1.5):
    """
    Animated binary search visualization
    
    Args:
        arr: Sorted list to search in
        target: Value to search for
        delay: Seconds between frames (default: 1.5)
    """
    clear_screen()
    
    low = 0
    high = len(arr) - 1
    step = 1
    
    print("=" * 70)
    print(f"  🔍 ANIMATED BINARY SEARCH")
    print("=" * 70)
    print(f"\n  Searching for: {target}")
    print(f"  Array: {arr}")
    print("=" * 70)
    time.sleep(delay * 0.7)
    
    def draw_array(low_val, mid_val, high_val, checking=None, found=False, eliminated=None):
        """Draw the array with visual indicators"""
        clear_screen()
        print("=" * 70)
        print(f"  🔍 ANIMATED BINARY SEARCH - Step {step}")
        print("=" * 70)
        print(f"\n  Searching for: {target}")
        print(f"  Array: {arr}")
        print("=" * 70)
        print()
        
        # Draw indices
        print("  Index:  ", end="")
        for i in range(len(arr)):
            print(f" {i:^4} ", end="")
        print()
        
        # Draw array values with highlighting
        print("  Array: [", end="")
        for i in range(len(arr)):
            if found and i == checking:
                print(f" \033[92m{arr[i]:^4}\033[0m ", end="")  # Green for found
            elif i == checking:
                print(f" \033[93m{arr[i]:^4}\033[0m ", end="")  # Yellow for checking
            elif eliminated and i in eliminated:
                print(f" \033[90m{arr[i]:^4}\033[0m ", end="")  # Gray for eliminated
            else:
                print(f" {arr[i]:^4} ", end="")
        print("]")
        
        # Draw pointers
        print("  Pointers:", end="")
        for i in range(len(arr)):
            markers = []
            if i == low_val:
                markers.append("LOW")
            if i == mid_val:
                markers.append("MID")
            if i == high_val:
                markers.append("HIGH")
            
            if markers:
                marker = ",".join(markers)
                if i == checking:
                    print(f" \033[93m{marker:^6}\033[0m", end="")
                elif found and i == checking:
                    print(f" \033[92m{marker:^6}\033[0m", end="")
                else:
                    print(f" {marker:^6} ", end="")
            else:
                print(f" {'':^6} ", end="")
        print()
        print()
        
        # Draw search space indicator
        search_space = arr[low_val:high_val+1]
        eliminated_space = []
        if eliminated:
            eliminated_space = [arr[i] for i in eliminated if i < low_val or i > high_val]
        
        print(f"  📍 Low={low_val}, Mid={mid_val}, High={high_val}")
        print(f"  🔎 Search Space: {search_space}")
        if eliminated_space:
            print(f"  ❌ Eliminated: {eliminated_space}")
        print()
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        # Show current state
        eliminated_indices = []
        if step > 1:
            # Show what was eliminated in previous step
            if arr[mid] > target:
                eliminated_indices = list(range(mid, len(arr)))
            else:
                eliminated_indices = list(range(0, mid + 1))
        
        draw_array(low, mid, high, checking=mid, eliminated=eliminated_indices if step > 1 else None)
        
        print(f"  Step {step}: Checking arr[{mid}] = {guess}")
        time.sleep(delay)
        
        if guess == target:
            draw_array(low, mid, high, checking=mid, found=True)
            print(f"  ✅ SUCCESS! Found {target} at index {mid}")
            print()
            print("=" * 70)
            print(f"  🎉 Search completed in {step} step{'s' if step > 1 else ''}!")
            print("=" * 70)
            time.sleep(delay * 1.5)
            return mid
        
        if guess > target:
            print(f"  ➡️  {guess} > {target} → Target is in LEFT half")
            print(f"     Updating: high = {mid} - 1 = {mid - 1}")
            high = mid - 1
        else:
            print(f"  ➡️  {guess} < {target} → Target is in RIGHT half")
            print(f"     Updating: low = {mid} + 1 = {mid + 1}")
            low = mid + 1
        
        step += 1
        time.sleep(delay)
    
    # Not found case
    draw_array(low, -1, high)
    print(f"  ❌ NOT FOUND: {target} is not in the array")
    print(f"     Search space exhausted (low={low} > high={high})")
    print()
    print("=" * 70)
    print(f"  ⚠️  Search completed - Item not found after {step-1} step{'s' if step > 1 else ''}")
    print("=" * 70)
    time.sleep(delay * 1.5)
    return None

def interactive_demo():
    """Interactive demo with multiple examples"""
    examples = [
        ([1, 3, 5, 7, 9], 3, "Finding 3 in [1, 3, 5, 7, 9]"),
        ([1, 3, 5, 7, 9], 7, "Finding 7 in [1, 3, 5, 7, 9]"),
        ([1, 3, 5, 7, 9], -1, "Searching for -1 (not found)"),
        ([2, 4, 6, 8, 10, 12, 14, 16], 10, "Finding 10 in larger array"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, "Finding 5 in [1..10]"),
    ]
    
    print("\n" + "=" * 70)
    print("  🎬 ANIMATED BINARY SEARCH DEMONSTRATION")
    print("=" * 70)
    print("\n  This will show multiple examples with animation.")
    print("  Each frame will show:")
    print("    • Current array state")
    print("    • Position of LOW, MID, HIGH pointers")
    print("    • Elements being checked (highlighted)")
    print("    • Elements eliminated from search")
    print("\n  Press Enter to start...")
    input()
    
    for arr, target, description in examples:
        print(f"\n{'='*70}")
        print(f"  Example: {description}")
        print(f"{'='*70}")
        time.sleep(1)
        animate_binary_search(arr, target, delay=1.2)
        time.sleep(0.5)
    
    clear_screen()
    print("=" * 70)
    print("  ✨ Animation Complete!")
    print("=" * 70)
    print("\n  Key Takeaways:")
    print("    • Binary search divides search space in half each step")
    print("    • Time complexity: O(log n) - very efficient!")
    print("    • Only works on SORTED arrays")
    print("    • At each step, eliminates half the remaining elements")
    print()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Custom search
        try:
            arr = [int(x) for x in sys.argv[1].strip('[]').split(',')]
            target = int(sys.argv[2])
            animate_binary_search(arr, target)
        except:
            print("Usage: python3 binarysearch_animated.py [array] [target]")
            print("Example: python3 binarysearch_animated.py [1,3,5,7,9] 3")
    else:
        # Run interactive demo
        interactive_demo()

