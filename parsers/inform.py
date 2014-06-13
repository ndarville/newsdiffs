from baseparser import BaseParser
from BeautifulSoup import BeautifulSoup

# DATE_FORMAT = '%-d. %B %Y'

class InformationParser(BaseParser):
    # Doesn't work; returns empty list
    feeder_pat = '^http://www.information.dk/\d+/'  # ?(\w+)
    feeder_base = 'http://www.information.dk'

    # Works
    # python parsers/test_parser.py inform.InformationParser
    #     http://www.information.dk/500604
    def _parse(self, html):
        """Retrieve and serve the required fields to create an entry."""
        soup = BeautifulSoup(html,
            convertEntities=BeautifulSoup.HTML_ENTITIES,
            fromEncoding='utf-8')

        self.meta = soup.findAll('meta')
        self.title = soup.find('h1').getText()
        self.date = soup.find('div', 'article-date').next.next.getText()
        self.byline = soup.find('div', 'field-name-byline').next.next.next.getText()
        self.body = soup.find('div', 'field-name-body').getText()
