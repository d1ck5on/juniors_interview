import requests
import csv
from bs4 import BeautifulSoup
from collections import Counter


def parse_current_html(soup: BeautifulSoup, storage: Counter[str]):
    list_links = soup.find_all(
        "div",
        class_="mw-category-columns"
    )[0].find_all("a")
    for list_link in list_links:
        title = list_link.get("title")
        storage[title[0].upper()] += 1


def find_next_page(soup: BeautifulSoup) -> str | None:
    next_page = soup.find("a", string="Следующая страница")
    if not next_page:
        return None
    next_page_link = next_page.get("href")
    return "https://ru.wikipedia.org" + str(next_page_link)


def create_csv():
    with open("beasts.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "alpha",
            "beasts_count"
        ])


def write_csv(data: Counter[str]):
    with open("beasts.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        for alpha, count in data.items():
            writer.writerow([
                alpha,
                count
            ])


def create_storage() -> Counter[str]:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper() + \
                "abcdefghijklmnopqrstuvwxyz".upper()
    storage = Counter(alphabet)
    for alpha in alphabet:
        storage[alpha] = 0
    return storage


def main():
    storage = create_storage()
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    while url:
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        parse_current_html(soup, storage)
        url = find_next_page(soup)

    create_csv()
    write_csv(storage)


if __name__ == "__main__":
    main()
