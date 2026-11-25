# Assessment 3.7: Sorting Algorithms

**Full Name:** Krystel Vei Enonsa-on M.

## What this does

1. Builds an array from the letters of the full name.
2. Cleans the array:
   - Removes symbols (spaces, the hyphen in "Enonsa-on", the period).
   - Removes duplicate letters (case-insensitive), keeping the first occurrence.
3. Prints the **unsorted** array.
4. Sorts the array using **Bubble Sort**.
5. Prints the **sorted** array.

## Output

```
Full Name: Krystel Vei Enonsa-on M.
Unsorted Array: ['K', 'r', 'y', 's', 't', 'e', 'l', 'V', 'i', 'n', 'o', 'a', 'M']
Sorted Array:   ['a', 'e', 'i', 'K', 'l', 'M', 'n', 'o', 'r', 's', 't', 'V', 'y']
```

## Algorithm for the sorting process (Bubble Sort)

1. Start at the beginning of the array.
2. Compare each pair of adjacent elements; if the left one is alphabetically
   greater than the right one, swap them.
3. Repeat this pass across the whole array — after each full pass, the
   largest unsorted element "bubbles" to its correct position at the end.
4. Repeat the passes (shrinking the unsorted portion each time) until a full
   pass makes no swaps — the array is then sorted.

## How to run

```bash
python3 bubble_sort_name.py
```

## Submitting

1. Push this project to a **new GitHub repository**.
2. Submit the repository link along with this algorithm description.
