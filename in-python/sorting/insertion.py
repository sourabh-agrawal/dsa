# Insertion sort
def insertion_sort(arr):
    # Loop through the arr from 2nd element onwards
    for i in range(1, len(arr)):
        curr = i
        # Try to insert the current element at the right place in the left
        # portion of the array
        while curr > 0 and arr[curr] < arr[curr - 1]:
            # swap elements
            arr[curr - 1], arr[curr] = arr[curr], arr[curr - 1]
            # Reduce the current and move in deeper
            curr -= 1
    return arr

# Starting of the main function
if __name__ == "__main__":
    # Take user input
    input_arr = list(map(int, input("Enter your array ").strip().split()))
    sorted_arr = list(map(str,insertion_sort(input_arr)))
    print("Sorted arrary is", " ".join(sorted_arr))
