from .base import BaseParser

class CategoryParser(BaseParser):
    def get_categories(self):
        soup = self.get_soup()
        nav_row = soup.find('div', class_='nav_row').find('ul')
        # NoneType object has no attribute find
        result = []
        for item in nav_row.find_all('a'):
            name = item.get_text()
            href = self.URL + item.get('href')  # https://upl.uz + /world/
            if name in ['Реклама', 'Контакты']:
                continue
            result.append({
                'name': name,
                'url': href
            })
        return result


