
from typing import List

import bs4
from more_itertools import ilen

from models.tag import Tag


class PageParser:
    """
    Return a list of dictionaries comprising of all the HTML tags in the webpage.

    Each dictionary has the keys: attributes, content and name of the tags.
    The attributes would be of the tags such as content and name
        whereas as the name listed above is the name of the tag.

    """
    def __init__(self, html_string):
        """
        :param html_string: the HTML data of the requested webpage
        """
        self.soup = bs4.BeautifulSoup(html_string, 'html5lib')
        self.html = self.soup.find('html')
        self.all_tags = self.parse()

    def parse(self) -> List[dict]:
        """
        :return: list of dictionaries with all the tags
        """
        results: List[dict] = []
        for tag in self.html.descendants:

            if isinstance(tag, bs4.element.Tag):

                # look for global.document.metadata
                if tag.name == 'script' and tag.string:
                    position = tag.string.find('global.document.metadata=')
                    if position == -1:
                        continue
                    else:
                        a = 'global.document.metadata='
                        t = Tag('global.document.metadata')

                        s = tag.string[position + len(a):]
                        s = s[:s.find('\n')-1]

                        t.add_content(s)
                        results.append(t.get_data())

                t = Tag(tag.name.lower())

                # Find tags with no children (base tags)
                if tag.contents and ilen(tag.descendants) == 1:
                    # Because it might be None (<i class="fa fa-icon"></i>)
                    if tag.string:
                        t.add_content(tag.string)

                    if tag.attrs:
                        for a in tag.attrs:
                            t.add_attribute(a, tag[a])

                    results.append(t.get_data())

                else:
                    # Self enclosed tags (hr, meta, img, etc...)
                    if tag.attrs:
                        for a in tag.attrs:
                            t.add_attribute(a, tag[a])

                    results.append(t.get_data())

        return results
