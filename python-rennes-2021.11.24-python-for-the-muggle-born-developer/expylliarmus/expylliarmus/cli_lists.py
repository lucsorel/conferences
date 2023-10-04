'''
Evolution of __main__.py: fully-implemented CLI based on lists, with graphics and memory usage reporting
'''
from typing import Dict, List, Tuple
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

def lowercase_spell_candidates(spell_candidates) -> List[Tuple[int,str]]:
    return [
        (index, spell.lower())
        for index, spell in spell_candidates
    ]

def validate_spell(spell: str) -> str:
    return SPELLS_DICT.get(spell, None)

def filter_valid_spells_by_line(lowercased_spell_candidates) -> List[Tuple[int,str]]:
    valid_spells_by_line: List[Tuple[int, str]] = []
    for index, spell in lowercased_spell_candidates:
        valid_spell = validate_spell(spell)
        if valid_spell is not None:
            valid_spells_by_line.append((index, valid_spell))

    return valid_spells_by_line

def fetch_book_lines_by_index(book_path: Path) -> List[Tuple[int, str]]:
    with open(book_path, 'r', encoding='utf8') as text_file:
        # book_lines = []
        # index = 1
        # for line in text_file:
        #     if len(line) > 0:
        #         book_lines.append((index, line))
        #     index += 1
        # return book_lines
        return [
            (index + 1, line)
            for index, line in enumerate(text_file)
            if len(line) > 0
        ]

def analyze_book_spells(book_file_name: str):
    book_path = TESTS_DATA_INPUTS_PATH / f'{book_file_name}.txt'
    print(f'processing {book_path}...')
    # gets book content
    book_lines = fetch_book_lines_by_index(book_path)

    # searches spell occurrences
    # 1. get spell candidates
    spell_candidates = find_spell_candidates(book_lines)
    # 2. standardize candidates
    lowercased_spell_candidates = lowercase_spell_candidates(spell_candidates)
    # 3. filter valid spells
    spells_by_line = filter_valid_spells_by_line(lowercased_spell_candidates)

    report_memory_usage(
        book_lines=book_lines,
        spell_candidates=spell_candidates,
        lowercased_spell_candidates=lowercased_spell_candidates,
        spells_by_line=spells_by_line,
    )

    # saves results in a csv file
    csv_path = book_path.parent / f'{book_file_name}.csv'
    save_spells_as_csv(spells_by_line, csv_path)

    # dataviz from csv file
    analyze_spells_distribution(csv_path, book_file_name)


def cli():
    cli_parser = ArgumentParser('Spell analysis CLI based on lists')
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
