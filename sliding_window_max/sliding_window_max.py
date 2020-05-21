'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# Create an array max_upto and a stack to store indices. Push 0 in the stack.
# Run a loop from index 1 to index n-1.
# Pop all the indices from the stack, which elements (array[s.top()]) is less than the current element and update max_upto[s.top()] = i – 1 and then insert i in the stack.
# Pop all the indices from the stack and assign max_upto[s.top()] = n – 1.
# Create a variable j = 0
# Run a loop from 0 to n – k, loop counter is i
# Run a nested loop until j < i or max_upto[j] < i + k – 1, increment j in every iteration.
# Print the jth array element.

def sliding_window_max(nums, k):
    # Your code here
    n = len(nums)
    max_nums = []
    max_upto=[0 for i in range(n)] 
    # Update max_up to array similar to 
    # finding next greater element 
    s=[] 
    s.append(0) 
    for i in range(1,n): 
        while (len(s) > 0 and nums[s[-1]] < nums[i]): 
            max_upto[s[-1]] = i - 1
            del s[-1] 
        s.append(i) 
    while (len(s) > 0): 
        max_upto[s[-1]] = n - 1
        del s[-1] 
    j = 0
    for i in range(n - k + 1): 
        # j < i is to check whether the 
        # jth element is outside the window 
        while (j < i or max_upto[j] < i + k - 1): 
            j += 1
        max_nums.append(nums[j]) 
    return max_nums

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
