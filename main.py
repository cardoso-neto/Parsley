
from multiprocessing import Pool

from args_parser import parse_args
from http_parser.master_parser import MasterParser
from tools.general import create_dir, text_file_to_set, get_url_slug_tuples


def download(info):
    filename, url = info
    MasterParser.parse(url, OUTPUT_DIR, filename)


def main(txt_file_path, num_workers):
    links = text_file_to_set(txt_file_path)
    try:
        filenames_urls = get_url_slug_tuples(links)
    except NotImplementedError:
        indices_as_strings = map(str, range(len(links)))
        filenames_urls = zip(indices_as_strings, links)

    with Pool(num_workers) as p:
        p.map(download, filenames_urls)


if __name__ == '__main__':
    args = parse_args()
    OUTPUT_DIR = args.output_dir

    create_dir(OUTPUT_DIR)
    main(args.input, args.workers)
