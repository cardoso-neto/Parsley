
from urllib.request import Request, urlopen

from http_parser.page_parser import PageParser
from http_parser.response_parser import ResponseParser
from tools.general import write_json


class MasterParser:

    @staticmethod
    def parse(url, output_dir: str, output_file: str) -> None:
        """
        Call ResponseParser to parse the headers from the urlopen object retrieved from the URL.
        Call the PageParser method to parse the content.
        Decode bytes using UTF-8.
        Store results in JSON with the attributes: url, status, headers and tags.

        :param url: The URL of webpage to be parsed to JSON
        :param output_dir: Root directory where the JSON is to be stored
        :param output_file: The name the JSON file is to be given
        """
        print('Crawling ' + url)
        # TODO error handling
        # urllib.error.URLError: <urlopen error [Errno 101] Network is unreachable>
        # urllib.error.URLError: <urlopen error [Errno 110] Connection timed out> # url that no longer exists
        # urllib.error.HTTPError: HTTP Error 504: Gateway Time-out
        # urllib.error.URLError: <urlopen error [Errno -3] Temporary failure in name resolution> # this one happened when I pulled the ethernet cable
        resp = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        resp_bytes = resp.read()
        resp_parser = ResponseParser(resp)
        try:
            page_parser = PageParser(resp_bytes.decode('utf-8'))
        except UnicodeDecodeError:
            return
        json_results = {
            'url': url,
            'status': resp.getcode(),
            'headers': resp_parser.headers,
            'tags': page_parser.all_tags
        }
        write_json(output_dir + '/' + output_file + '.json', json_results)
