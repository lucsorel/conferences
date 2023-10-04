# Expylliarmus

## Project creation

```sh
poetry new expylliarmus
cd expylliarmus

poetry config virtualenvs.create true --local
poetry config virtualenvs.in-project true --local
poetry config virtualenvs.prefer-active-python true --local

poetry add matplotlib
poetry add pre-commit --group lint
```

## Project installation

```sh
poetry install
```

## Project execution

You need to create a .local/ folder with some sample 1-philosopher_stone.txt and 3-azkaban.txt files.
Being able to run the project is completely optional for this presentation.

```sh
# execute expylliarmus/__main__.py
poetry run python -m expylliarmus -b 1-philosopher_stone -b 3-azkaban
```

## Run the pre-commit hooks

```sh
# add git support to the project
git init -b demo
git config user.name "Harry Cover"
git config user.email "harry.cover@hogwarts.bzh"

# create the first commit
git add -A && git commit -m "state without hooks"

# boilerplate with git (generate the .git/hooks/pre-commit hook file)
poetry run pre-commit install

# runs a specific hook on all files
git add -A && poetry run pre-commit run end-of-file-fixer --all-files

# runs all the hooks on all files
git add -A && poetry run pre-commit run --all-files
# -> nothing should change

# to see the effects of pre-commit hooks
# 1. copy-paste the code contents from expylliarmus/__main__do_not_hook.py into expylliarmus/__main__.py
#    the `exclude: __main__do_not_hook.py` line in .pre-commit-config.yaml avoids formatting this file
# 2. commit the changes without triggering the pre-commit hook
git add -A && git commit -m "state without quality hooks" --no-verify
# 3. run a selection of hooks at a time; see/show how the files are modified
git add -A && poetry run pre-commit run --all-files
# 4. set fix = true in pyproject.toml#[tool.ruff] to enable ruff autofixing and run the hook
```

At the end of the demo, set the ground clear before committing unwanted changes:
* set `fix = false` back in `pyproject.toml#[tool.ruff]`
* `rm -fr .git` to remove the git subproject of the presentation
