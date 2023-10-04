
from pathlib import Path

def save_spells_as_csv(spells_by_line, csv_path: Path):
    with open(csv_path, 'w', encoding='utf8') as spells_file:
        spells_file.write('line,spell\n')
        spells_file.writelines((
            f'{index},{spell}\n'
            for index, spell in spells_by_line
        ))
    print(f'wrote {csv_path}')