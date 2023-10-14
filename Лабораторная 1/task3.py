diskette_size_bytes = 1.44 * 1024 * 1024

pages = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4


bytes_per_book = pages * lines_per_page * characters_per_line * bytes_per_character

num_books = diskette_size_bytes // bytes_per_book

print("Количество книг, помещающихся на дискету:", int(num_books))