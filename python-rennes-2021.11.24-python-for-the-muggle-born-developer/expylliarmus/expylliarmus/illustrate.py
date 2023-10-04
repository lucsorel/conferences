
from csv import reader
from collections import Counter
from pathlib import Path

from matplotlib import pyplot


def analyze_spells_distribution(csv_path: Path, book_file_name: str):
    with open(csv_path, 'r', encoding='utf8') as spell_by_line_file:
        spell_by_line_csv = reader(spell_by_line_file, delimiter=',')
        # skip headers
        next(spell_by_line_csv)

        # lines = []
        # spells = []
        # for row in spell_by_line_csv:
        #     lines.append(row[0])
        #     spells.append(row[1])
        lines, spells = zip(*(
            (int(row[0]), row[1])
            for row in spell_by_line_csv
        ))

        fig, (spells_bar_axes, spell_lines_axes) = pyplot.subplots(nrows=2, ncols=1, figsize=(5*2, 10))
        spell_counter = Counter(spells)
        # spell_names = spell_counter.keys()
        # spell_occurrences = spell_counter.values()
        spell_names, spell_occurrences = zip(*spell_counter.most_common()[::-1])
        spell_ticks = range(len(spell_names))
        spells_bar_axes.barh(spell_ticks, spell_occurrences)
        spells_bar_axes.set(xlabel='spell occurrences', ylabel='spells', title=f'Occurrences of spells cast in {book_file_name}')
        spells_bar_axes.set_yticks(spell_ticks, spell_names)
        spells_bar_axes.set_xticks(range(0, max(spell_occurrences) + 1))
        nb_lines_per_page = 50
        nb_pages_per_bin = 20
        nb_lines_per_page = nb_lines_per_page * nb_pages_per_bin
        max_spell_line = max(lines)
        max_bin_border = max_spell_line - (max_spell_line % nb_lines_per_page) + (2 * nb_lines_per_page)
        bins = list(range(0, max_bin_border, nb_lines_per_page))
        spell_lines_axes.hist(lines, bins=bins)
        spell_lines_axes.set_xticks(bins)
        spell_lines_axes.set(
            xlabel='line index', ylabel='number of cast spells', title=f'Distribution of spells cast in {book_file_name}'
        )
        spell_lines_axes.tick_params(axis='x', which='major', labelsize=6)
        fig.tight_layout()
        fig.savefig(
            str(csv_path.parent / f'{csv_path.name}.png'),
            format='png'
        )
        # removes figure from RAM
        pyplot.close(fig)

if __name__ == '__main__':
    spell_by_line_filename = 'spell_by_line.csv'
    analyze_spells_distribution('spell_by_line.csv', 'spell_book')
