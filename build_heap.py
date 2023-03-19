# 221RDB014 Mihails Ruhļa 13. grupa


def build_heap(arr):
    n = len(arr)
    swaps = []
    for i in range(n//2 - 1, -1, -1):
        heap(arr, n, i, swaps)
    
    return swaps

def heap(arr, n, i, swaps):
    min = i 	
    lSon = 2*i + 1
    rSon = 2*i + 2
    if lSon < n and arr[lSon] < arr[min]:
        min = lSon
    if rSon < n and arr[rSon] < arr[min]:
        min = rSon
    if min != i:
        arr[i], arr[min] = arr[min], arr[i]  
        swaps.append((i, min))  
        heap(arr, n, min, swaps)  
	
def main():
    let = input().strip()
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
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))
    assert len(swaps) <= 4 * n
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
