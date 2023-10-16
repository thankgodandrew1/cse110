# """ 
# Author Name: ThankGod Andrew

# Purpose: practice finding items in a file core requirements
# """

# largest_chap = -1
# largest_book = None
# max_chap = -1
# max_name = None

# with open('books_and_chapters.txt') as books:
#     for book in books:
#         parts = book.strip().split(':')

#         book_name = parts[0]
#         book_chap = int(parts[1]) 
#         scripture = parts[2]
    
#         print(f'Scripture: {scripture}, Book: {book_name}, Chapter: {book_chap}')
    
#         if book_chap > largest_chap:
          
#             largest_chap = book_chap
#             largest_book = book_name

#     print(f'\nThe highest number of chapters in the list is: {largest_chap} with the scripture name {largest_book}')
              
                 
#                   # STRETCHY STRETCH CHALLENGE

#     books.seek(0)

#     user_scripture = input('Which scripture do you want to learn about? ')

#     with open('books_and_chapters.txt') as books:
#         for book in books:
#             parts = book.strip().split(':')

#             book_name = parts[0]
#             book_chap = int(parts[1]) 
#             scripture = parts[2]
        
#             if scripture.lower() == user_scripture:
#                 print(f'Scripture: {scripture}, Book: {book_name}, Chapters: {book_chap}')

#                 if book_chap  > max_chap:
#                     max_chap = book_chap
#                     max_name = book_name
    
#         print()
#         print(f'The book in the {user_scripture.title()} with the largest number of chapters is: {max_name} chapter {max_chap}')