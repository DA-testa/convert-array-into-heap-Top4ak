# 221RDB014 Mihails Ruhļa 13. grupa

def build_heap(arr):
    n = len(arr)
    swaps = []
    
    for i in range(n//2 - 1, -1, -1):
        heap(arr, n, i, swaps)
    
    return swaps

def heap(arr):
    n = len(arr)
    swaps = []
    
    for i in range(n):
        min_index = i
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n and arr[left_index] < arr[min_index]:
            min_index = left_index
        if right_index < n and arr[right_index] < arr[min_index]:
            min_index = right_index
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps.append((i, min_index))
            i = min_index
            
    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    let= input().strip()
    if let == 'I':
        n = int(input().strip())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif let == 'F':
        file = input().strip()
        file = "tests/" + file
        with open(file, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))  
            
            assert len(data) == n
            
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))
    assert len(swaps) <= 4 * n
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
