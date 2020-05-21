'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# first-pass solution
# we all keep an array, call it 'no_dups' to hold numbers we see in the nums array
#  iterate through nums
# check to see if the number is already in the 'no_dups' array
# if it is, remove it fro the 'no_dups' array
# when we are done iterating, the only number in our 'no_dups" array iis the odd number out
# return it 
def single_number(arr):
    
    return 2 * sum(set(arr)) - sum(arr)
 
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")