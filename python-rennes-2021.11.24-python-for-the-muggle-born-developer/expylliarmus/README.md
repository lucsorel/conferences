
# Project creation and installation

## Creation

```sh
# defines the Python version to use
pyenv install 3.8.6
pyenv local 3.8.6

# creates the project
poetry new expylliarmus
mv .python-version expylliarmus
cd expylliarmus

# create a local virtual environment
poetry config virtualenvs.create true --local
poetry config virtualenvs.in-project true --local

poetry add -D pylint

# launches the IDE!
codium .

# add a dependency to see what happens
poetry add matplotlib

# execute expylliarmus/__main__.py
poetry run python -m expylliarmus -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows
```

## Profiling

See [PROFILING.md](PROFILING.md)

# With generators

Once cli_lists and cli_gens modules are written

```sh
poetry run python -m expylliarmus.cli_lists -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows
poetry run python -m expylliarmus.cli_gen -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows

# execute the command 10 times and times the whole execution
bash time.sh poetry run python -m expylliarmus.cli_gen -b 3-azkaban
# execute the command a specified number of times and times the whole execution
EXEC_TIMES=2 bash time.sh poetry run python -m expylliarmus.cli_gen -b 3-azkaban
```

# To try

Pipe spells_by_line iterator into 2 generators:
* one to write the results in the csv file
* one to analyze the distribution

```python
def spells_by_line_from_iter(spells_by_line_iter):
    iterate = True
    while iterate:
        spells_by_line = yield
        if spells_by_line == None:
            iterate = False
        else:
            yield spells_by_line

def spells_by_line_from_file(csv_path: Path):
    with open(csv_path, 'r', encoding='utf8') as spell_by_line_file:
        spell_by_line_csv = reader(spell_by_line_file, delimiter=',')
        # skip headers
        next(spell_by_line_csv)
        for row in spell_by_line_csv:
            yield row[0], row[1]

def analyze_spells_distribution(spell_by_line_iter, book_file_name: str):
    lines, spells = zip(*(
        (int(row[0]), row[1])
        for row in spell_by_line_iter
    ))
    ...
# same for csv dumping
```
