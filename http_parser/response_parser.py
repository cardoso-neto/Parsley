
from http.client import HTTPResponse
from typing import Dict


class ResponseParser:

    def __init__(self, response: HTTPResponse):
        self.response = response
        self.headers = self.parse()

    def parse(self) -> Dict[str, str]:
        '''
        Return a dict with the response headers of the page along with other metadata.

        The utility of this function is that urlopen.info() returns these information
            as a mime tools.Message instance which isn’t as easy to use an dictionary.
        Each item from an .info() call is split and added to a dictionary as a key value pair.

        :param response: The response object from a urlopen call to the URL of the webpage
        :type response: HTTPresponse object

        :returns a dictionary with response headers and other meta-information depending on the webpage.
        '''
        results = {}
        header_info = str(self.response.info()).split('\n')
        for item in header_info:
            row = item.split(':', 1)
            try:
                key = ' '.join(row[0].split())
                value = ' '.join(row[1].split())
                results[key] = value
            except IndexError:
                pass
        return results
