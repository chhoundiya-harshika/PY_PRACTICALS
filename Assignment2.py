
def split_by_highest_num(lst):
    # Find all numeric values with their original indices
    nums = [(val, idx) for idx, val in enumerate(lst) if isinstance(val, (int, float))]
    
    if not nums:
        print("No numbers found in the list.")
        return lst, []

    # Identify the highest number and its index
    highest_val, highest_idx = max(nums, key=lambda x: x[0])
    
    # Split the list at the highest number's index
    first_part = lst[:highest_idx]
    second_part = lst[highest_idx:]
    
    # Print and return the results
    print(f"Highest Number found: {highest_val}")
    print(f"Part 1: {first_part}")
    print(f"Part 2: {second_part}")
    
    return first_part, second_part

# Example Usage
mixed_list = ["apple", 10, 45, "banana", 32, ]
part1, part2 = split_by_highest_num(mixed_list)