import threading
from queue import Queue

from args_parser import parse_args
from http_parser.master_parser import MasterParser
from tools.general import create_dir, text_file_to_set, get_url_slug_tuples


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        filename, url = queue.get()
        MasterParser.parse(url, OUTPUT_DIR, filename)
        queue.task_done()


def create_jobs():
    links = text_file_to_set(INPUT_FILE)
    try:
        filenames_urls = get_url_slug_tuples(links)
    except NotImplementedError:
        filenames_urls = zip(range(len(links)), links)

    for filename_url in filenames_urls:
        queue.put(filename_url)
    queue.join()


if __name__ == '__main__':
    args = parse_args()
    INPUT_FILE = args.input
    OUTPUT_DIR = args.output
    NUMBER_OF_THREADS = args.threads

    queue = Queue()
    create_dir(OUTPUT_DIR)

    create_workers()
    create_jobs()
