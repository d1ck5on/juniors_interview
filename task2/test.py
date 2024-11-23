import unittest
from bs4 import BeautifulSoup
from solution import (
    parse_current_html,
    find_next_page,
    create_storage
)


class CheckParseTitles(unittest.TestCase):
    def test_one_letter_on_page(self):
        storage = create_storage()
        with open("test_pages/one_letter_on_page.html", "r") as f:
            text = f.read()
        soup = BeautifulSoup(text, "lxml")
        parse_current_html(soup, storage)
        for alpha, count in storage.items():
            if alpha == 'А':
                self.assertEqual(count, 200)
            else:
                self.assertEqual(count, 0)

    def test_two_letters_on_page(self):
        storage = create_storage()
        with open("test_pages/two_letters_on_page.html", "r") as f:
            text = f.read()
        soup = BeautifulSoup(text, "lxml")
        parse_current_html(soup, storage)
        for alpha, count in storage.items():
            if alpha == 'А':
                self.assertEqual(count, 1)
            elif alpha == 'Б':
                self.assertEqual(count, 199)
            else:
                self.assertEqual(count, 0)


class CheckFindNextPage(unittest.TestCase):
    def test_next_page_exists(self):
        next_page_url = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B5+%D1%82%D0%BE%D0%BA%D0%B8#mw-pages"
        with open("test_pages/next_page_exists.html", "r") as f:
            text = f.read()
        soup = BeautifulSoup(text, "lxml")
        url = find_next_page(soup)
        self.assertEqual(url, next_page_url)

    def test_next_page_does_not_exists(self):
        with open("test_pages/next_page_does_not_exists.html", "r") as f:
            text = f.read()
        soup = BeautifulSoup(text, "lxml")
        url = find_next_page(soup)
        self.assertIsNone(url)


if __name__ == "__main__":
    unittest.main()
