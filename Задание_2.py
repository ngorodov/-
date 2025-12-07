# TODO Найдите количество книг, которое можно разместить на дискете
diskette_size_mb = 1.44
book_pages = 100
sheets = 50
symbools = 25
bytes_in_char = 4
bytes_in_kb = 1024
kb_per_mb = 1024
book_size_ = book_pages * sheets * symbools * bytes_in_char
diskette_size_bytes = diskette_size_mb * kb_per_mb * bytes_in_kb
books_count = int(diskette_size_bytes // book_size_)
print("Количество книг, помещающихся на дискету:", books_count)