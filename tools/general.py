import json
import os
from pathlib import Path
from collections import Counter
from collections import defaultdict
from dataclasses import dataclass

from slugify import slugify


@dataclass
class ElementInfo:
    count: int = 0
    index: list = []


def get_repeated_elements(elements):
    element_counter = defaultdict(ElementInfo)
    for i, elem in enumerate(elements):
        element_counter[elem].count += 1
        element_counter[elem].index.append(i)
    repeated_elements = {
        element: info
        for element, info in element_counter.items()
        if info.count > 1
    }
    return repeated_elements


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def filenames_to_set(dir_path):
    dir_path = Path(dir_path)
    files_in_dir = {item.stem for item in dir_path.iterdir() if item.is_file()}
    return files_in_dir


def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def text_file_to_set(file_name):
    with open(file_name, 'rt') as f:
        lines = [line.replace('\n', '') for line in f]
    repeated_links = get_repeated_elements(lines)
    if repeated_links:
        print(
            'Some URLs appear more than once.',
            'However, they are going to be downloaded only once.',
        )
    return set(lines)


def get_url_slug_tuples(urls):
    slugs = [slugify(url) for url in urls]
    repeated_slugs = get_repeated_elements(slugs)
    if repeated_slugs:
        raise NotImplementedError('Some links translate to the same slug.')
    return zip(slugs, urls)


def write_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)
