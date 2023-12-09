def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        index = i
        while index >= 1 and arr[index - 1] > arr[index]:
            arr[index - 1], arr[index] = arr[index], arr[index - 1]
            index -= 1

        print(f"after pass: {i},", end="")
        for num in arr:
            print(f" {num}", end="")
        print()

    print("after Sorting Final:", end="")
    for num in arr:
        print(f" {num}", end="")
    print()


n = int(input("Enter the number of elements: "))
arr = [int(x) for x in input("Enter the elements separated by spaces: ").split()]

insertion_sort(arr)
