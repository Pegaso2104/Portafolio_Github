import utils
import sorts
from random import randrange

# 1. Load the books and print titles
bookshelf = utils.load_books('books_small.csv')
for book in bookshelf:
    print(book['title'])

# 2. Investigate Unicode code points for 'a', ' ', 'A'
print(ord('a'))  # Code point of 'a'
print(ord(' '))  # Code point of space
print(ord('A'))  # Code point of 'A'

# 3. Ensure case-insensitive comparisons by adding lowercased version of title and author
# This is done in utils.py when loading the books

# 4. Bubble sort with custom comparison function
def bubble_sort(arr, comparison_function):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if comparison_function(arr[j], arr[j+1]):  # Use the comparison function
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count

# 5. Comparison function to sort books by title
def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

# 6. Sort books by title using bubble sort
sort_1 = bookshelf.copy()  # Make a copy to preserve original
swap_count = bubble_sort(sort_1, by_title_ascending)
for book in sort_1:
    print(book['title'])
print(f"Total swaps: {swap_count}")

# 7. Comparison function to sort books by author
def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

# 8. Sort books by author using bubble sort
bookshelf_v1 = bookshelf.copy()
sort_2 = bookshelf_v1.copy()
swap_count_author = bubble_sort(sort_2, by_author_ascending)
for book in sort_2:
    print(book['author'])
print(f"Total swaps for author sort: {swap_count_author}")

# 9. Create a copy of the bookshelf before sorting with quicksort
bookshelf_v2 = bookshelf.copy()

# 10. Quicksort function with custom comparison
def quicksort(arr, start, end, comparison_function):
    if start >= end:
        return
    
    pivot_idx = randrange(start, end + 1)
    pivot_element = arr[pivot_idx]
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]

    less_than_pointer = start
    for i in range(start, end):
        if comparison_function(arr[i], pivot_element):
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer += 1

    arr[end], arr[less_than_pointer] = arr[less_than_pointer], arr[end]
    quicksort(arr, start, less_than_pointer - 1, comparison_function)
    quicksort(arr, less_than_pointer + 1, end, comparison_function)

# 11. Perform quicksort by author
quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for book in bookshelf_v2:
    print(book['author'])

# 12. Comparison function to sort by total length of title + author
def by_total_length(book_a, book_b):
    total_length_a = len(book_a['title']) + len(book_a['author'])
    total_length_b = len(book_b['title']) + len(book_b['author'])
    return total_length_a > total_length_b

# 13. Load large dataset
long_bookshelf = utils.load_books('books_large.csv')

# 14. Run bubble sort on large dataset with by_total_length
swap_count_large = bubble_sort(long_bookshelf, by_total_length)
print(f"Total swaps for large dataset: {swap_count_large}")

# 15. Test performance with quicksort on large dataset
long_bookshelf_copy = long_bookshelf.copy()
quicksort(long_bookshelf_copy, 0, len(long_bookshelf_copy) - 1, by_total_length)
for book in long_bookshelf_copy:
    print(book['title'])

# 16. Compare performance of bubble sort on large dataset (comment out the previous bubble sort block for testing)
# Comment out the previous bubble sort attempt if you wish to test the performance of bubble sort

# 17. Quicksort should perform faster. Print results after quicksort.
for book in long_bookshelf_copy:
    print(book['author'])

# 18. Play around with other comparison functions (optional)
def by_title_length(book_a, book_b):
    return len(book_a['title']) > len(book_b['title'])

# 19. Test new comparison function
bubble_sort(long_bookshelf, by_title_length)

# 20. Experiment with creating more comparison operators and sorting algorithms
# Add any additional sorting functions or optimizations here as needed.
