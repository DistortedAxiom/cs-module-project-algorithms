'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    dict1 = {}
    for x in arr:
        if x not in dict1:
            dict1[x] = 1
        else:
            dict1[x] += 1

    print(dict1)

    for k,v in dict1.items():
        if v == 1:
            return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")