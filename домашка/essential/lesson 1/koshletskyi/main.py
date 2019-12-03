#!/usr/bin/python3
# -*- coding: utf-8 -*_

import review
import book
import author

def main():
    rev = review.Review("Horosho")
    rev2 = review.Review("Ploho")

    autor_Tolstoy = author.Author("Leo", "Tolstoy", 1828)
    boo = book.Book(autor_Tolstoy, "WAR Pease", "1488", "War")
    boo1 = book.Book(autor_Tolstoy, "Anna K", "1489", "Drama")
    boo.add_review(rev)
    boo.add_review(rev2)
    autor_Tolstoy.add_book(boo)
    autor_Tolstoy.add_book(boo1)
    print(autor_Tolstoy)
    print(boo)
    print(boo1)
    # print(boo == boo1)
    # print(autor_Tolsto == autor_Tolstoy)
    # boo.add_review(rev)
    # boo.get_review()




if __name__ == '__main__':
    main()
