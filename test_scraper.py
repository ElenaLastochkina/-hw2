import json
import pytest
from scraper import scrape_books
 
def test_scrape_books():
    books = scrape_books()
 
    assert len(books) > 0
 
    for book in books:
        assert 'Title' in book
        assert 'Price' in book
        assert 'Availability' in book
        assert 'Description' in book
 
def test_save_books_to_json(tmpdir):
    tmp_file_path = tmpdir.join('test_books.json')
 
    books = [{'Title': 'Book 1', 'Price': '10', 'Availability': 5, 'Description': 'Book 1 description'},
             {'Title': 'Book 2', 'Price': '15', 'Availability': 10, 'Description': 'Book 2 description'}]
 
    save_books_to_json(tmp_file_path, books)
 
    with open(tmp_file_path, 'r') as json_file:
        saved_books = json.load(json_file)
 
    assert saved_books == books
