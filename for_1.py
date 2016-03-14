"""
#Simple for loop
my_books=['Python','Java','C++','Ruby','Perl']

for x in my_books:
    print(x)
print("Done")
"""

#Simple for loop with counter

my_books=['Python','Java','C++','Ruby','Perl']

book_number=0

for x in my_books:
    book_number=book_number+1
    print("Book number ",book_number,"is",x)
print("All books name with number is printed above")