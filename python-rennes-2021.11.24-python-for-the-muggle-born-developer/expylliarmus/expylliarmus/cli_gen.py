'''
Alternative of cli_lists.py: a fully-implemented CLI based on generators
'''

from typing import Dict, Iterator, Tuple
from argparse import ArgumentParser, Namespace
from pathlib import Path

from expylliarmus.dump import save_spells_as_csv
from expylliarmus.match import SPELL_MATCHER, SPELLS
from expylliarmus.illustrate import analyze_spells_distribution
from expylliarmus.pymp import report_memory_usage

from tests.data import TESTS_DATA_INPUTS_PATH

SPELLS_DICT: Dict[str, str] = {
    spell.lower(): spell
    for spell in SPELLS
}

def yield_spells_of_line(line: str) -> Iterator[str]:
    for match in SPELL_MATCHER.finditer(line):
        yield match.group(1)

def filter_valid_spells(
    spell_by_line_iter: Iterator[Tuple[int, str]]
) -> Iterator[Tuple[int, str]]:
    for index, spell in spell_by_line_iter:
        valid_spell = SPELLS_DICT.get(spell.lower(), None)
        if valid_spell is not None:
            yield index, valid_spell

def find_spell_candidates(book_lines) -> Iterator[Tuple[int,str]]:
    return (
        (index, spell)
        for index, line in book_lines
        for spell in yield_spells_of_line(line)
    )

def lowercase_spell_candidates(spell_candidates) -> Iterator[Tuple[int,str]]:
    return (
        (index, spell.lower())
        for index, spell in spell_candidates
    )

def validate_spell(spell: str) -> str:
    return SPELLS_DICT.get(spell.lower(), None)

def filter_valid_spells_by_line(lowercased_spell_candidates) -> Iterator[Tuple[int,str]]:
    for index, spell in lowercased_spell_candidates:
        valid_spell = validate_spell(spell)
        if valid_spell is not None:
            yield index, valid_spell

def fetch_book_lines_by_index(book_path: Path) -> Iterator[Tuple[int, str]]:
    with open(book_path, 'r', encoding='utf8') as text_file:
        for index, line in enumerate(text_file):
            if len(line) > 0:
                yield index + 1, line

def analyze_book_spells(book_file_name: str):
    book_path = TESTS_DATA_INPUTS_PATH / f'{book_file_name}.txt'
    print(f'processing {book_path}...')
    # gets book content
    book_lines_iter = fetch_book_lines_by_index(book_path)

    # searches spell occurrences
    # 1. get spell candidates
    spell_candidates_iter = find_spell_candidates(book_lines_iter)
    # 2. standardize candidates
    lowercased_spell_candidates_iter = lowercase_spell_candidates(spell_candidates_iter)
    # 3. filter valid spells
    spells_by_line_iter = filter_valid_spells_by_line(lowercased_spell_candidates_iter)

    report_memory_usage(
        book_lines_iter=book_lines_iter,
        spell_candidates_iter=spell_candidates_iter,
        lowercased_spell_candidates_iter=lowercased_spell_candidates_iter,
        spells_by_line_iter=spells_by_line_iter,
    )

    # saves results in a csv file
    csv_path = book_path.parent / f'{book_file_name}.csv'
    save_spells_as_csv(spells_by_line_iter, csv_path)
    # dataviz from csv file
    analyze_spells_distribution(csv_path, book_file_name)


def cli():
    cli_parser = ArgumentParser('Spell analysis CLI based on generators')
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
