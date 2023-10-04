'''
Initial skeleton of a CLI dedicated to counting the occurrences of the magic spells cast in a list of books
During the demo, it will be renamed into cli_lists.py
'''

from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Dict, List, Tuple

from tests.data import TESTS_DATA_INPUTS_PATH

def fetch_book_lines_by_index(book_path: Path) -> List[Tuple[int, str]]:
    with open(book_path, 'r', encoding='utf8') as text_file:
        book_lines = []
        index = 1
        for line in text_file:
            if len(line) > 0:
                book_lines.append((index, line))
            index += 1
        return book_lines

def yield_spells_of_line(line: str) -> List[str]:
    return [
        match.group(1)
        for match in SPELL_MATCHER.finditer(line)
    ]

def yield_spells_of_line(line: str) -> List[str]:
    return [
        match.group(1)
        for match in SPELL_MATCHER.finditer(line)
    ]

def find_spell_candidates(book_lines) -> List[Tuple[int,str]]:
    return [
        (index, spell)
        for index, line in book_lines
        for spell in yield_spells_of_line(line)
    ]

def analyze_book_spells(book_file_name):
    book_path = TESTS_DATA_INPUTS_PATH / f'{book_file_name}.txt'
    print(f'processing {book_path}...')
    # gets book content
    book_lines: Tuple[int, str] = fetch_book_lines_by_index(book_path)
    print(book_lines)

    # searches spell occurrences
    # 1. get spell candidates
    # 2. standardize candidates
    # 3. filter valid spells

def cli():
    cli_parser = ArgumentParser('Spell analysis CLI')
    cli_parser.add_argument(
        '-b', '--book', action='append',
        dest='books', help='filename of a book to process'
    )
    args: Namespace = cli_parser.parse_args()
    # print('args', args)
    for book in args.books:
        analyze_book_spells(book)

if __name__ == '__main__':
    cli()