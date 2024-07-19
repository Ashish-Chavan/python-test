def bubble_sort(elements):
  """Sorts a list of elements in ascending order using bubble sort algorithm

  Args:
    elements: The list of elements to be sorted.

  Returns:
    None. The function sorts the elements in-place.
  """
  # Outer loop to iterate through the list n times
  for n in range(len(elements) - 1, 0, -1):
    swapped = False
    # Inner loop to compare adjacent elements
    for i in range(n):
      if elements[i] > elements[i + 1]:
        # Swap elements if they are in the wrong order
        swapped = True
        elements[i], elements[i + 1] = elements[i + 1], elements[i]
    # If we didn't make any swaps in a pass, the list is already sorted and we can exit the outer loop
    if not swapped:
      return

# Sample list to be sorted
elements = [39, 12, 18, 85, 72, 10, 2, 18]


print("Sorted list is:")
print(elements)
