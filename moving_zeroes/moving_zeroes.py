'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    i = 0
    end = len(arr)
    while i < end:
        if arr[i] == 0:
            del arr[i]
            arr.append(0)
            end -= 1
        else:
            i += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")