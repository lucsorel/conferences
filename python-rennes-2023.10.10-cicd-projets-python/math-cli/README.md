# Math-cli

Un projet de démo utilisant les Github actions

## Création et configuration du projet

```sh
# création de la structure du projet
poetry new math-cli

cd math-cli

# spécification de la version de Python utilisée
pyenv install 3.8.16
pyenv local 3.8.16

# configuration de poetry pour le projet
# 1. demander à poetry d'utiliser un environnement virtuel
poetry config virtualenvs.create true --local

# 2. placer l'environnement virtual dans un sous-dossier .venv
poetry config virtualenvs.in-project true --local

# 3. initialiser l'environnement virtuel avec la version de Python dans .python-version
poetry config virtualenvs.prefer-active-python true --local

# installation de dépendances
poetry add fire
poetry add pytest pytest-cov --group dev
poetry add pre-commit --group lint
```

## À faire lors de la création du dépôt de ce projet de démo

```sh
# configuration git
git init -b main

git config user.name "{nom complet}"
git config user.email "{adresse email}"
git config push.default matching
git config pull.rebase true
git config mergetool.keepBackup false
git config core.editor "codium --wait" # optionnel

# adapter l'url à votre cas
git remote add origin git@github.com:lucsorel/math-cli.git
git branch -M main

# installation des dépendances
poetry install

# cablage de pre-commit avec les hooks git, 1re vérification pour installer
poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg
poetry run pre-commit run --all-files

# 1er commit (exclut les actions et test_math_cli.py)
git add -A -- ':!.github/*' ':!tests/test_math_cli.py'
git commit -m "feat(math_cli): implement factorial and fibonacci with tests" --no-verify
git push -u origin main

# 2e commit : ajout des Github actions
git add .github
git commit -m "ci(math_cli): add the CI workflow" --no-verify
git push

# 3e commit
git add tests/test_math_cli.py
git commit -m "test(math_cli): test the CLI controller" --no-verify
git push
```

Faire l'intégration avec le service https://pre-commit.ci/.

Suppression du dossier .git

```sh
rm -fr .git
```

## Commandes de l'outil math_cli

```sh
# affiche l'aide
poetry run python -m math_cli

# calcule la factorielle d'un nombre
poetry run python -m math_cli factorial 3
# -> 6

# calcule la série de Fibonacci au rang donné
poetry run python -m math_cli fibonacci 3
# -> 2
```

## Commandes de vérification de la qualité de code

```sh
# tests automatisés
poetry run pytest -v

# tests automatisés avec couverture de code
poetry run pytest -v --cov=math_cli --cov-branch --cov-report term-missing --cov-fail-under 97

# lance tous les hooks sur tous les fichiers
poetry run pre-commit run --all-files

# lance un hook sur tous les fichiers
poetry run pre-commit run end-of-file-fixer --all-files
```
