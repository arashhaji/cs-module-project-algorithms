'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # base case: when there are no more cookies
    # print(n)
    if n == 0:
        return 1
    elif n < 1:
        return 0
    else:
    # this represents our recursive case where there still some cookies 
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


    # represents Cookie Monster eating one Cookie
    eating_cookies(n-1)
    # represents Cookie Monster eating two cookies
    eating_cookies(n-2)
    # represents Cookie Monster eating three cookies
    eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
