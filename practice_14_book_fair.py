'''
https://www.codechef.com/practice/course/infosys-pyq/INFOSYS04/problems/QQQUOC06
'''


def unplacedBooks(books, shelf):
    # i, j = 0, 0
    # n = len(books)
    # m = len(shelf)
    
    # unplaced_books = 0
    
    # while i < n and j < m:
    #     if shelf[j] >= books[i]:
    #         i+=1
    #         j+=1
        
    #     elif shelf[j] < books[i]:
    #         j+=1
    #     # else:
    #     #     j-=1
        
    # unplaced_books = n - i
    
    # return unplaced_books
    
    n = len(books)
    used = [False] * n
    unplaced_books = 0
    
    for book in books:
        placed = False # initially book is unplaced, so False
        for i in range(n):
            if not used[i] and shelf[i] >= book:
                used[i] = True # mark True if shelf is used
                placed = True # mark True if book is placed
                break
        
        if not placed:
            unplaced_books += 1
    
    return unplaced_books

# books = [2,5,7]
books = [80,45,60,90,30,55]
# shelf = [6,3,8]
shelf = [70,50,65,85,25,40]

'''
6
80,45,60,90,30,55
70,50,65,85,25,40
'''

print(unplacedBooks(books, shelf))