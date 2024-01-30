import requests
from bs4 import BeautifulSoup
import json
 
def scrape_books():
    url = 'http://books.toscrape.com/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
 
    books = []
 
    # Ищем все ссылки на книги на главной странице
    book_links = soup.find_all('h3')
 
    for link in book_links:
        book = {}
 
        # Получаем ссылку на страницу книги
        book_url = link.a['href']
        book_response = requests.get(f'http://books.toscrape.com/catalogue/{book_url}')
        book_soup = BeautifulSoup(book_response.text, 'html.parser')
 
        # Извлекаем информацию о книге
        book['Title'] = book_soup.find('h1').text.strip()
        book['Price'] = book_soup.find('p', class_='price_color').text.strip()[1:]
        book['Availability'] = int(book_soup.find('p', class_='instock availability').text.strip().split()[2])
        book['Description'] = book_soup.find('article', class_='product_page').find_all('p')[3].text.strip()
 
        books.append(book)
 
    return books
 
def save_books_to_json(books):
    with open('books.json', 'w', encoding='utf-8') as json_file:
        json.dump(books, json_file, ensure_ascii=False, indent=4)
 
# Входная точка программы
if __name__ == '__main__':
    books_data = scrape_books()
    save_books_to_json(books_data)

    print('Информация о книгах сохранена в файле books.json.')