'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n != 0:
        _3 = n // 3
        r = n - (_3 * 3)
        num = _3
        #breakpoint()

        _2 = r // 2
        r = r - (_2 * 2)
        num += _2

        _1 = r // 1
        #r = _1 - int(1)
        num += _1

    return num


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
