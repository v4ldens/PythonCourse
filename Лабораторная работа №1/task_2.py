# TODO Найдите количество книг, которое можно разместить на дискете

I = round(1.44 * 1024 * 1024) # Информационный объём в байтах
pages_quantity = 100
strings_quantity = 50
symbols_quantity = 25
k = 4

one_book = 4 * 25 * 50 * 100 # Одна книга в байтах
books_quantity = I // one_book

print("Количество книг, помещающихся на дискету:", books_quantity)
