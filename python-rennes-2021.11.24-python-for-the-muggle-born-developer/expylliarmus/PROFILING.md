
# Profilers comparison

* https://stackify.com/how-to-use-python-profilers-learn-the-basics/
* https://www.blog.pythonlibrary.org/2020/04/14/an-overview-of-profiling-tools-for-python/
* https://pythonspot.com/python-profiling/
* https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script

# Tools

I focused on tools that are not code-intrusive (which do not require to edit the code to profile):

* [pyinstrument](https://github.com/joerick/pyinstrument): statistical profiler (samples the process state, stops the world to perform some inspections, release the process).
* [py-spy](https://github.com/benfred/py-spy): same profiling strategy as pyinstrument (sampling), but can be launched alongside a running application by giving it a process id to monitor.

# Installation

Profiling packages are declared as optional libraries

```sh
poetry add pyinstrument --optional
poetry add py-spy --optional
poetry add pympler --optional
```

Add an `instrument` extra section in `pyproject.toml` file:

```ini
[tool.poetry.extras]
instrument = ["pyinstrument", "py-spy", "Pympler"]
```

To install these profiling tools:

```sh
poetry install --extras instrument
```

However, you cannot just uninstall extra dependencies, you have to remove the virtual environment & the lock file then perform a clean install without extras:

```sh
rm -fr .venv poetry.lock && poetry install
```

## Pyinstrument

```sh
# outputs the analysis in the terminal
poetry run pyinstrument -m expylliarmus.cli_lists -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows
poetry run pyinstrument -m expylliarmus.cli_gen -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows

# exports an analysis report as an html document
poetry run pyinstrument -o "$(date '+%Y-%m-%d_%H%M%S')-lists_profiling.html" -r html -m expylliarmus.cli_lists -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows
poetry run pyinstrument -o "$(date '+%Y-%m-%d_%H%M%S')-gen_profiling.html" -r html -m expylliarmus.cli_gen -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows
```

## Py-spy

```sh
# exports a clickable flamegraph in svg format that can be drag'n'dropped in a browser
poetry run py-spy record -o "$(date '+%Y-%m-%d_%H%M%S')-lists_profiling.svg" -- python -m expylliarmus.cli_lists -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows

# exports a speedscope (see https://github.com/jlfwong/speedscope) in json format that can be drag'n'dropped in https://www.speedscope.app/
poetry run py-spy record --format speedscope -o "$(date '+%Y-%m-%d_%H%M%S')-lists_profiling.json" -- python -m expylliarmus.cli_lists -b 7-deathly_hallows
poetry run py-spy record --format speedscope -o "$(date '+%Y-%m-%d_%H%M%S')-gen_profiling.json" -- python -m expylliarmus.cli_gen -b 7-deathly_hallows
```

## Native tracing profiling

The native cProfile profiler is a tracing profiler: it follows each instruction and times them.

```sh
# outputs in the terminal (saved in text file)
poetry run python -m cProfile -m expylliarmus.cli_lists -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows > cli_lists_cprofiling.txt
# outputs in a .profile file
poetry run python -m cProfile -o cli_list_profiling.profile -m expylliarmus.cli_lists -b 1-philosopher_stone -b 3-azkaban -b 5-order_phenix -b 7-deathly_hallows
# -> the results can be displayed in runsnake (sudo apt install runsnakerun)
runsnake cli_lists_profiling.profile
```

## Pympler

[Pympler](https://pympler.readthedocs.io/en/latest/) is a development tool to measure, monitor and analyze the memory behavior of Python objects in a running Python application.
It is an intrusive library: one has to import the monitoring functions of pympler and apply them on the python variable one wants to monitor.

```python
from pympler.asizeof import asizeof
print('spells_by_line:', asizeof(spells_by_line), 'bytes')

# outputs "spells_by_line: 4145434616 bytes"
```
