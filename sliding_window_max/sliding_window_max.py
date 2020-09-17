'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    n = len(nums)
    if n == 0:
        return
    s = k-1
    mx = []
    for i in range(len(nums)-s):
        #if nums[i+k] <= nums[-1]:
        mx.append(max(nums[i:i+k]))
    return mx


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
