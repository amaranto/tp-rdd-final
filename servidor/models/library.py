import json
from typing import List
from models.book import Book
from config import BOOKS_DESTINATION

class Library():
    def __init__(self, books: List[Book]=[]) -> None:
        self.books : list[Book] = books

    def add_book(self, book : Book) -> None:
        self.books.append(book)
    
    def get_book(self, title : str) -> Book:
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def get_all_books(self) -> List[Book]:
        return self.books
    
    def get_books_by_language(self, language : str) -> List[Book]:
        books = []
        for book in self.books:
            if book.language == language:
                books.append(book)
        return books
    
    def get_books_by_author(self, author : str) -> List[Book]:
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        return books

    def get_books_by_country(self, country : str) -> List[Book]:
        books = []
        for book in self.books:
            if book.country == country:
                books.append(book)
        return books
    
    def get_books_by_title(self, title : str) -> List[Book]:
        books = []
        for book in self.books:
            if book.title == title:
                books.append(book)
        return books
    
    def delete_book(self, book : Book) -> None:
        self.books.remove(book)
    
    def delete_book_by_title(self, title : str) -> None:
        book = self.get_book(title)
        self.delete_book(book)
        
    def delete_books_by_author(self, author : str) -> None:
        books = self.get_books_by_author(author)
        for book in books:
            self.delete_book(book)
    
    def delete_books(self, author : str, title : str) -> None:
        books_author = self.get_books_by_author(author)
        books_title = self.get_books_by_title(title)
        for book in books_title:
            if book in books_author:
                self.delete_book(book)
    
    def to_json(self) -> List[dict]:
        return [book.to_json() for book in self.books]

    def from_json(self, json : List[dict]) -> None:
        self.books += [Book().from_json(book) for book in json]
        return self.books
    
    def save_library(self, path = BOOKS_DESTINATION ) -> None:
        with open(path, "w") as f:
            json.dump(self.to_json(), f)
    
    def set_books(self, books: List[Book]):
        self.books = books