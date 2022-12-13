
def isValidSubsequence(array, sequence):
    # Write your code here.
    sIndex = 0
    for idx, ele in enumerate(array):
        if array[idx] == sequence[sIndex]:
            sIndex += 1
            if sIndex == len(sequence):
                return True
    return False


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))
