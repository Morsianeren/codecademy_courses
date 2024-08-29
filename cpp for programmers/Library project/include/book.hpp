#include <string>

class Book{
    public:
        Book();
        Book(std::string title, std::string author, int year);
        std::string getTitle();
        std::string getAuthor();
        int getYear();
        void setTitle(std::string title);
        void setAuthor(std::string author);
        void setYear(int year);
        void print();
    private:
        std::string title;
        std::string author;
        int year;
};