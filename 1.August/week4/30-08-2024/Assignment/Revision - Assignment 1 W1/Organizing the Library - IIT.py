def sort_books_ascending(books_list):
    # Return the list of books sorted in ascending order by number of pages
    return sorted(books_list,key=lambda x:x[1])

def sort_books_descending(books_list):
    # Return the list of books sorted in descending order by number of pages
    return sorted(books_list,key=lambda x:x[1],reverse=True)