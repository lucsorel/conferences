---
theme : "moon"
customTheme : "assets/python-theme"
transition: "slide"
highlightTheme: "solarized-dark"
slideNumber: true
title: "Python for the Muggle-born developer"
revealjs.controls: false
enableChalkboard: false

---


# Python for the Muggle-born developer

<img width="20%" src="assets/python_rennes.png" />


<div class="parseltongue">

Python Rennes - 24 novembre 2021 - Lucius Malforel

</div>


---

## Presentation & disclaimer

<img src="assets/luc-halloween.jpg" />

* @Zenigwarts 2016 (green advocate 2020+)
* OWL in <strong>Care of magical creatures - 🐍</strong> +3 years
* `@lucsorel`

<br />

<br />

<div class="fragment">

* This is NOT an introductory talk to the language
* This is about how to <del>tame</del> *play with* the beast

</div>


---


## Lesson 1 - tame the right snake


<div class="parseltongue">
choose your dialect
</div>


--

First tamer: **Guido van Rossum** released Python 1 in 1991

<figure>
    <img src="assets/1024px-Guido-portrait-2014-drc.jpg" alt="Guido van Rossum portrait" />
    <figcaption><i>"Code is read much more often than it is written"</i></figcaption>
</figure>

* Python 3 released in 2008
* Python 2 ended in 2020


--

<div class="harry-potter">

Why do I have an obsolete beast alive in my syssSStem?

</div>

```sh
~ python2 --version
Python 2.7.18
```

<div class="fragment">

```sh
~ sudo apt-get purge python2
Construction de l'arbre des dépendances...
```

</div>

<div class="fragment">

```sh
...
Les paquets suivants seront ENLEVÉS :
  gimp-plugin-registry* inkscape* jackd2* jackd2-firewire*
  libjack-jackd2-0* python-backports.functools-lru-cache* python-bs4*
  python-cffi-backend* python-chardet* python-cryptography*
  python-dbus* python-enum34* python-gi* python-html5lib*
  python-ipaddress* python-lxml* python-numpy* python-openssl*
  python-pkg-resources* python-six* python-soupsieve* python-tk*
  python-webencodings* python2* scribus* scribus-data*
  ubuntustudio-controls* ubuntustudio-default-settings*
  ubuntustudio-desktop* ubuntustudio-desktop-core*
  ubuntustudio-installer* ubuntustudio-menu* ubuntustudio-menu-add*
Souhaitez-vous continuer ? [O/n]
```

</div>

--

<div class="harry-potter">

My Python 3 beast is also rather old...

</div>

```sh
~ python3 --version
Python 3.8.6
```

<div class="fragment">

```sh
~ sudo apt-get purge python3
Les paquets suivants seront ENLEVÉS (sélection):
  apparmor* chromium-browser* firefox*
  gnome-software-plugin-snap* language-selector-common*
  printer-driver-foo2zjs-common* printer-driver-m2300w*
  [...]
  python3* [...]
  software-properties-common* software-properties-gtk*
  system-config-printer* system-config-printer-common*
  system-config-printer-udev* ubuntu-advantage-tools*
  ubuntu-drivers-common* ubuntu-minimal*
  ubuntu-release-upgrader-core* ubuntu-release-upgrader-gtk*
  ubuntu-standard* ubuntustudio-controls*
  ubuntustudio-default-settings* ubuntustudio-desktop*
  ubuntustudio-desktop-core* ubuntustudio-installer*
  ubuntustudio-menu* ubuntustudio-menu-add*
  [...]
  update-manager* update-manager-core* update-notifier*
  xfce4-panel-profiles* xfpanel-switch* xorg* xserver-xorg*

Souhaitez-vous continuer ? [O/n]
```

</div>

--

<div class="parseltongue">

📜✅ Don't mess around with your Python system installation

</div>

<img src="assets/Web-feature-jim-kay-goblet-main-banner.jpg" alt="dragon" />


--

<div class="parseltongue">
Define a 🐍 version at the project level
</div>

[pyenv](https://github.com/pyenv/pyenv/) (🐧, 🍏), [pyenv-win](https://github.com/pyenv-win/pyenv-win) (🔲)

<br />

* downloads specific 🐍 versions (including `anaconda`'s)
  ```text
  ~ pyenv install 3.9.3
  ```

* specifies the version to use at the folder scale
  ```text
  ~ cd Documents
  ~ pyenv local 3.9.3
  
  ~ cat .python-version
  3.9.3
  ```

--

<!-- .slide: style="text-align: left;" -->

* adds *shims* to your `$PATH` that:
  * intercept calls to 🐍 binaries (`python`, `pip`, etc.)
  * search for a `.python-version` file (iteratively towards `∕`)


Example: `cat ~/.pyenv/shims/python`:

```sh
#!/usr/bin/env bash
set -e
[ -n "$PYENV_DEBUG" ] && set -x

program="${0##*/}"

export PYENV_ROOT="~/.pyenv"
exec "~/.pyenv/libexec/pyenv" exec "$program" "$@"
```

---


## Lesson 2 - isolate your snake's environment


<div class="parseltongue">
room of requirement
</div>

<img src="assets/room_of_hidden_things_by_ancientking-d91ru4r.jpg" />

--

<div class="harry-potter">

~150 *"Python 3"* sSSpells are already installed in my sysSStem...&nbsp;😱

</div>

```sh
sudo apt list --installed | grep python3  | wc -l

151
```

<img src="assets/the_leaky_cauldron.jpg" />

* versions set by your (local) distribution
* your projects may involve different ones

--

<div class="parseltongue">

📜✅✅ Don't mess around with your Python system installation

</div>

<img src="assets/Web-feature-jim-kay-goblet-main-banner.jpg" alt="dragon" />


--

<div class="parseltongue">
Use a virtual environment
</div>


```sh
~ python -m venv my-project # 📜 thanks to pyenv, python version is now 3.x
~ cd my-project
```

<div class="fragment">

```sh
my-project/
  ┣ bin/       # available binaries
  ┃ ┣ activate
  ┃ ┣ pip
  ┃ ┗ python
  ┣ lib/       # project dependencies
  ┗ pyvenv.cfg # env settings & paths to python binaries

~ source bin/activate
~ (my-project) ➜  pip install matplotlib
```

</div>

<div class="fragment">

```sh
~ (my-project) ➜  pip freeze > requirements.txt
```

```ini
cycler==0.11.0
fonttools==4.28.2
kiwisolver==1.3.2
matplotlib==3.5.0
numpy==1.21.4
[...]
six==1.16.0
tomli==1.2.2
```

</div>

--

<div class="parseltongue">

📜 pip (python package manager)

</div>

* 🙂 huge `Python Package Index` ([pypi.org](https://pypi.org/))

* 🙂 `pip freeze `versions transitive dependencies too

* 😕 `pip un⋅install` does not update `requirements.txt`

* ☹️ does not distinguish `production` from `development` dependencies

--

<div class="parseltongue">

Associate an image to a concept

</div>

|  A  |  B  |  C  |
|:---:|:---:|:---:|
| <img src="assets/quiz/room_of_requirements.jpg" width="100%" /> | <img src="assets/quiz/invisibility.gif" width="100%" /> | <img src="assets/quiz/accio.gif" width="100%" /> |

<br />

1. `pip install`
1. `python -m venv`
1. `pip freeze`

---


## Lesson 3 - 🐍 breeding


<div class="parseltongue">
daily care & industrialization
</div>

--

<div class="harry-potter">

How should I sSStructure & sSSpecify my project?

</div>

Think about your code as a library:
* production code is expected in a sub-folder
* it is the package name that will be installed via PyPI
* other folders (eg `tests/`) and root contents will be discarded when installed from PyPI

<div class="fragment">

Project configuration root file:
* <span class="magic-owl">obliviate</span>(<del>`setup.py`</del>): obsolete, imperative
* 💙💛 `pyproject.toml`: new standard ([PEP-518](https://www.python.org/dev/peps/pep-0518/), 2016), declarative
</div>

--

<div class="parseltongue">

[poetry](https://python-poetry.org/docs/): spells for dependency management and packaging

</div>

* abstraction layer over `venv` & `pip`
* provides life-cycle commands for projects

```sh
~ poetry new expylliarmus
~ cd expylliarmus

# virtual environment in a `.venv` sub-folder
~ poetry config virtualenvs.create true --local
~ poetry config virtualenvs.in-project true --local

~ poetry install
```

<div class="fragment">

```sh
expylliarmus/         # root folder of the codebase (version its contents)
  ┣ .venv/            # virtual environment folder (bin/activate, etc.)
  ┣ expylliarmus/     # package production code
  ┃ ┗ __init__.py     # exposes the package main contents
  ┣ tests/            # testing resources
  ┃ ┣ __init__.py     # defines the tests package
  ┃ ┗ expylliarmus.py # contains a basic unit test
  ┣ poetry.lock       # dependencies lock file
  ┣ poetry.toml       # poetry configuration
  ┣ pyproject.toml    # package configuration
  ┗ README.rst        # empty root documentation file
```

</div>

--


Install some production & developement dependencies:

```sh
poetry add matplotlib
poetry add -D pylint
```

<div class="fragment">

Inside the `pyproject.toml` file:

```ini
[tool.poetry]
name = "expylliarmus"
version = "0.1.0"
description = "Put a spell on you"
# populated from your git config
authors = ["Lucius Malforel <l**.****l@z***a.c*m>"]

[tool.poetry.dependencies]
python = "^3.8"
matplotlib = "^3.5.0"

[tool.poetry.dev-dependencies]
pytest = "^5.2"
pylint = "^2.11.1"
```

See other [optional keys](https://python-poetry.org/docs/pyproject/) (repo, bug-tracker, licence, etc.)

</div>


---

## Lesson 4 - spell-book and wands


<div class="parseltongue">
Intently Dangerous Equipment
</div>

<img src="assets/deathly-hallows-python.png" />

--

<!-- .slide: style="text-align: left;" -->


* [Codium](https://vscodium.com/) (vsCode without MS telemetry) & extensions
  * [ms-python.python](https://github.com/Microsoft/vscode-python): Python tooling
  * [bungcip.better-toml](https://github.com/bungcip/better-toml): `toml` file syntax highlighting
  * [coenraads.bracket-pair-colorizer-2](https://github.com/CoenraadS/Bracket-Pair-Colorizer-2): brackets, braces & parentheses highlighting

<div class="fragment">

* [Pycharm](https://www.jetbrains.com/pycharm/)

</div>

<div class="fragment">

* Spyder
* Sublime Text, Atom
* Vim, Emacs

*Use your favorite !*

</div>

---

<div class="parseltongue">

Pensieve takeaways

</div>

<img src="assets/Pensieve_merged_black-blueish.png" />


1. Don't mess around with your Python system installation
1. Isolate project in a virtual environment
1. Production code inside a dedicated folder
1. Project configuration in `pyproject.toml`
1. Codium / vsCode + 3 extensions is a good start

💙💛 pyenv + poetry + pytest

---

## ThanksSSs !

<img src="assets/Nagini.png" />


---

## Extra 1 - accio application!


<div class="parseltongue">
portkeys
</div>

<img src="assets/portkey.jpg" />

--

<!-- .slide: style="text-align: left;" -->

[pyinstaller](https://pyinstaller.readthedocs.io/en/stable/) (<del>installer</del> -> packager)
* distributable file containing Python binaries, imported libraries & application code 

```sh
# package the application as a single file
poetry run pyinstaller --onefile --name="expylliarmus" \
  --specpath="$(pwd)/pyinstaller" --distpath="$(pwd)/dist"  \
  "$(pwd)/expylliarmus/__main__.py"
```

<div class="fragment">

🐳 fully-configurable image
* install `pyenv`
* install the python version (`cat .python-version`)
* install `poetry` and app dependencies
* copy app production folder

</div>

---

## Extra 2 - conceal shameful experiments


<div class="parseltongue">
jupyter horcruxes
</div>

<img src="assets/Horcruxes-notebook.png" />

--

<!-- .slide: style="text-align: left;" -->

<div class="parseltongue">

📜 install & customize [jupyter](https://jupyter.org/) in a 🐳 image

</div>

```sh
docker run -p 8888:8888 -v "$(pwd)/shared:/home/jovyan/work" \
    -e JUPYTER_TOKEN=horcrux -e JUPYTER_ENABLE_LAB=yes jupyter/scipy-notebook
```

<div class="fragment">

<hr />

```dockerfile
# Dockerfile
FROM jupyter/scipy-notebook
ENV JUPYTER_ENABLE_LAB=yes
# install custom libraries
RUN pip install bokeh==2.2.2 holoviews
```

```yaml
# docker-compose.yml
version: "3"
services:
  jupyterlab:
    build: .
    environment:
      - JUPYTER_TOKEN=horcrux
    volumes:
      - "./shared:/home/jovyan/work"
    ports:
      - "8888:8888"
```

http://localhost:8888?token=horcrux

</div>
