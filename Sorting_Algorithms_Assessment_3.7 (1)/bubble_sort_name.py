"""
Assessment 3.7: Sorting Algorithms
Full Name: Krystel Vei Enonsa-on M.

Steps:
1. Build an array from the letters of the full name.
2. Clean the array:
   - Remove symbols (spaces, hyphens, periods, etc.) -- only letters are kept.
   - Remove duplicate letters (case-insensitive), keeping the first
     occurrence so the original letter case is preserved.
3. Print the UNSORTED array.
4. Sort the array using Bubble Sort.
5. Print the SORTED array.
"""


def clean_name_to_array(full_name):
    """Turn a full name string into an array (list) of unique letters,
    discarding symbols and duplicate letters."""

    unsorted_array = []
    seen_letters = set()  # tracks letters already added (case-insensitive)

    for char in full_name:
        if char.isalpha():                 # exclude symbols (spaces, "-", ".")
            lower_char = char.lower()
            if lower_char not in seen_letters:  # exclude duplicate letters
                seen_letters.add(lower_char)
                unsorted_array.append(char)

    return unsorted_array


def bubble_sort(array):
    """Sort an array of letters alphabetically using Bubble Sort."""

    sorted_array = array.copy()        # keep the original array unsorted
    n = len(sorted_array)

    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            # compare letters case-insensitively so order is alphabetical
            if sorted_array[i].lower() > sorted_array[i + 1].lower():
                sorted_array[i], sorted_array[i + 1] = sorted_array[i + 1], sorted_array[i]
                swapped = True
        if not swapped:        # array is already sorted, stop early
            break

    return sorted_array


if __name__ == "__main__":
    full_name = "Krystel Vei Enonsa-on M."

    unsorted_array = clean_name_to_array(full_name)
    sorted_array = bubble_sort(unsorted_array)

    print("Full Name:", full_name)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:  ", sorted_array)
