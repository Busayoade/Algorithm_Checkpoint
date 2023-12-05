#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if the target is at the middle
        if arr[mid] == target:
            return True
        
        # If the target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If the target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If the element is not present in the array
    return False

# Test cases
print(binary_search([1,2,3,5,8], 6)) # Should output False
print(binary_search([1,2,3,5,8], 5)) # Should output True




# In[2]:


#Question 2
def power(base, exponent):
    return base ** exponent

# Test case
print(power(3, 4))  # Output will be 81


# In[3]:


#Question 3
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

# Sorting the list using bubble sort
bubble_sort(data)

# Display the sorted list
print("Sorted list:", data)


# In[5]:


#Question 4
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in left_half and right_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

# Sorting the list using merge sort
merge_sort(data)

# Display the sorted list
print("Sorted list:", data)


# In[6]:


#Question 5
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

# Sorting the list using quick sort
quick_sort(data, 0, len(data) - 1)

# Display the sorted list
print("Sorted list:", data)


# In[ ]:




