#ifndef LIBRARY_HPP
#define LIBRARY_HPP

#include <string>
#include <unordered_set>
#include "book.hpp"

class Library {
public:
    Library();
    void AddBook(Book book);
    void DestroyBook(std::string title);
    Book LoanBook(std::string title, std::string borrower);
    void ReturnBook(std::string title);
    void PrintBooks();

private:
    std::unordered_set<Book> _books;
    

};

#endif // LIBRARY_HPP