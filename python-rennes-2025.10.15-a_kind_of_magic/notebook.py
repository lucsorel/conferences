import marimo

__generated_with = "0.16.5"
app = marimo.App(
    width="columns",
    app_title="A kind of magic : méthodes spéciales, metaclasse, pattern matching",
    layout_file="layouts/notebook.slides.json",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pytest
    return mo, pytest


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Méthodes spéciales, métaclasse, pattern matching
    ## Datawalk : une mini-syntaxe de récupération de données

    <img src="public/2025.10.15-python_rennes-a_kind_of_magic.png" width="40%" style="display: block; margin-left: auto; margin-right: auto"></img>
    Python Rennes - mercredi 15 octobre 2025 - Hellowork

    [@lucsorelgiffo@floss.social](https://floss.social/@lucsorelgiffo) (tech-lead full-stack chez [See you sun](https://www.seeyousun.fr) 🌞⚡)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Au programme

    Retour d'expérience sur l'élaboration d'une syntaxe de parcours de données : [github.com/lucsorel/datawalk](https://github.com/lucsorel/datawalk) (-> ⭐)

    - découverte de sujets "bas niveau"
      - méthodes ~~magiques~~ spéciales
      - métaclasse
      - pattern matching structurel
    - détourer ces notions pour vous donner des idées
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Une mini-syntaxe de récupération de données - pourquoi ?

    Besoin : construire un rapport allant piocher des valeurs dans un dictionnaire très arborescent (~100 Mo).

    1. syntaxe expressive de récupération des valeurs
    2. décoreller la récupération de valeurs de la construction du rapport
    3. message d'erreur informatif lors d'un échec de récupération de valeur
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Quelques exemples de récupération de données""")
    return


@app.cell
def _():
    from dataclasses import dataclass
    from typing import NamedTuple

    class Pet:
        def __init__(self, name: str, type: str):
            self.name = name
            self.type = type

        def __repr__(self) -> str:
            return f'Pet(name={self.name}, type={self.type})'

    @dataclass
    class PetDataclass:
        name: str
        type: str

    class PetNamedTuple(NamedTuple):
        name: str
        type: str

    data = {
        'name': 'Lucie Nation',
        'org': {
            'title': 'Datawalk',
            'address': {'country': 'France'},
            'phones': ['01 23 45 67 89', '02 13 46 58 79'],
        },
        'friends': [
            {'name': 'Frankie Manning', 'phones': []},
            {'name': 'Harry Cover', 'phones': ['02 34 56 78 91', '06 12 34 57 89']},
            {'name': 'Suzie Q', 'phone': '06 43 15 27 98'},
            {'name': 'Jean Blasin'},
        ],
        'pets': [
            {'name': 'Cinnamon', 'type': 'cat'},
            PetNamedTuple('Caramel', 'dog'),
            Pet('Melody', 'bird'),
            PetDataclass('Socks', 'cat'),
        ],
    }
    cinnamon, caramel, melody, socks = data['pets']
    return caramel, cinnamon, data, socks


@app.cell
def _(cinnamon, data, socks):
    # récupération du pays de l'adresse professionnelle
    def test_raw_retrieve_org_country():
        assert data['org']['address']['country'] == 'France'
        assert data.get('org').get('address').get('country') == 'France'

    # récupération du nom du 3e animal
    def test_raw_retrieve_name_of_3rd_pet():
        assert data.get('pets')[2].name == 'Melody'

    # récupérations par recherche de valeur de clé ou d'attribut
    def test_raw_search_harry_2nd_phone():
        harry = next(friend for friend in data['friends'] if friend['name'] == 'Harry Cover')
        assert harry['phones'][1] == '06 12 34 57 89'

    def test_raw_search_cats():
        cats = [
            pet for pet in data['pets']
            if (getattr(pet, 'type', None) == 'cat') or (isinstance(pet, dict) and pet.get('type') == 'cat')
        ]
        assert cats == [cinnamon, socks]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Erreurs classiques de récupération de valeurs

    Messages pas toujours très explicites (même si ils s'améliorent de version en version de Python 😊)
    """
    )
    return


@app.cell
def _(data):
    # erreur d'index de liste
    phone_number = data.get('friends')[0].get('phones')[1]
    return


@app.cell
def _(data):
    # erreur de clé de dictionnaire
    phone_number_2 = data.get('friends')[2].get('phones')[0]
    return


@app.cell
def _(data):
    # erreur de nom d'attribut
    data['pets'][2]._name
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Datawalk : le [pathlib.Path](https://docs.python.org/3/library/pathlib.html) des données ?

    Expressivité de `pathlib.Path` par rapport à `os.path` :

    ```python
    # obsolète
    from os import path

    schemas_folder = path.join(path.dirname(path.dirname(__file__)), 'schemas', 'user.json')
    if path.isdir(schemas_folder):
        ...

    # recommandé
    from pathlib import Path

    schemas_path = Path(__file__).parent.parent / 'schemas' / 'user.json'
    if schemas_path.is_dir():
        ...
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Décoreller la déclaration du chemin d'accès au données de leur récupération :

    ```python
    melody = data.get('pets')[2].name

    melody_walk = Walk() / 'pets' / 2 / 'name'
    melody = melody_walk.walk(data)
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Comment fonctionne l'utilisation de l'opérateur "`/`" dans `Path` ?
    ```python
    class Path(PurePath):
        ...

    class PurePath(object):
        def __truediv__(self, key):
            try:
                # ajoute le chemin donné aux précédents
                return self._make_child((key,))
            except TypeError:
                return NotImplemented
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Une **méthode "spéciale"** :
    - a un nom en `__dunder__()`
    - n'est généralement pas appelé directement
    - mais appelée "sous le capot" par :
      - d'autres fonctions : `len(obj)` appelle `obj.__len__()`, `print(obj)`
      - des opérateurs : `obj + obj_2`, `ma_liste[::-1]`, `mon_dico['clé']`
      - des mécanismes internes :
        - itération dans une boucle **for**
        - entrée / sortie de contextmanager
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Méthodes spéciales "opérateurs mathématiques"

    Documentation officielle :
    - opérateurs mathématiques et méthodes spéciales : https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
    - priorité des opérateurs : https://docs.python.org/3/reference/expressions.html#operator-precedence

    Synthèse :

    |  Priorité | Opérateur | Méthode spéciale |
    |---|---|---|
    | 1 | ** | `__pow__(self, other[, modulo])` |
    | **2** | /  | `__truediv__(self, other)` |
    | **2** | // | `__floordiv__(self, other)` |
    | **2** | @ | `__matmul__(self, other)` |
    | **2** | % | `__mod__(self, other)` |
    | **2** | * | `__mul__(self, other)` |
    | 3 | + | `__add__(self, other)` |
    | 3 | - | `__sub__(self, other)` |
    | 4 | << | `__lshift__(self, other)` |
    | 4 | >> | `__rshift__(self, other)` |
    | 5 | & | `__and__(self, other)` |
    | 6 | ^ | `__xor__(self, other)` |
    | **7** | `|` | `__or__(self, other)` |
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Choix de conception pour `datawalk`

    - utiliser des opérateurs de même priorité pour exprimer un chemin de donnée sans devoir recourir à des parenthèses (lisibilité)

    -> **priorité 2** (`/`, `//`, `@`, `%`, `*`) : pour avoir le plus de possibilités sémantiques

    - utiliser un opérateur moins prioritaire pour appliquer la recherche de valeurs sur une structure de données

    -> **priorité 7** : `|`, familiarité avec son utilisation dans les shells unix pour "piper" des données

    ```python
    value = my_walk.walk(data)
    value = my_walk | data
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 🧪 TP : squelette de `datawalk.Walk`""")
    return


@app.cell
def _():
    from typing import Any, Iterable, Hashable, Protocol

    class WalkError(LookupError):
        def __init__(self, /, message, *, data_state=None):
            super().__init__(message)
            self.data_state = data_state

    class Selector(Protocol):
        def __call__(self, state: Any) -> Any: ... # sélectionne une valeur dans la structure de données
        def __repr__(self) -> str: ... # affiche le comportement du sélecteur

    class MetaWalk(type):
        '''
        Hériter de type fait de MetaWalk une metaclass
        '''
        def __truediv__(cls, step: Hashable) -> 'Walk':
            return Walk(ByKey(step))

        def __matmul__(cls, filter: tuple[Hashable, Hashable]) -> Any:
            return Walk(First(*filter))

        def __mod__(cls, filter: tuple[Hashable, Iterable]):
            return Walk(All(filter))

    class Walk(metaclass=MetaWalk):
        def __init__(self, *selectors: Selector):
            self.selectors = tuple(selectors)

        def __truediv__(self, step: Hashable | slice) -> 'Walk':
            return Walk(*self.selectors, ByKey(step))

        def walk(self, data) -> Any:
            current_state = data
            passed_selectors = []
            for selector in self.selectors:
                try:
                    current_state = selector(current_state)
                    passed_selectors.append(selector)
                except Exception as error:
                    raise WalkError(
                        f'walked ({" ".join(str(selector) for selector in passed_selectors)}) of ({self}) but could not find {selector} in the current data state',
                        data_state=current_state,
                    ) from error

            return current_state

        def __or__(self, data) -> Any:
            return self.walk(data)

        def __repr__(self) -> str:
            return ' '.join(f'{selector}' for selector in self.selectors)

        def __matmul__(self, filter: tuple[Hashable, Hashable]) -> Any:
            """
            >>> walk @ (key, value)
            """
            match filter:
                case [key, value]:
                    return Walk(*self.selectors, First(key, value))
                case _:
                    raise ValueError(f'unsupported filter: {filter}')

        def __mod__(self, filter: tuple[Hashable, Iterable]):
            """
            >>> walk % (key, [values])
            """
            match filter:
                case [key, [*values]]:
                    return Walk(*self.selectors, All(key, values))

                case [key, value]:
                    raise ValueError(f'unsupported filter: {filter}, value {value} must be a sequence')

                case _:
                    raise ValueError(f'unsupported filter: {filter}')

    class All:
        def __init__(self, key: Hashable, values: Iterable):
            self.key = key
            self.values = values

        def __call__(self, state: Iterable[dict | object]) -> list:
            return [item for item in state if value_getter(item, self.key) in self.values]

        def __repr__(self) -> str:
            return f'%({self.key} in {self.values})'

    _DEFAULT = object()
    def value_getter(item: dict | object, key: Hashable):
        if isinstance(item, dict):
            return item.get(key, _DEFAULT)
        else:
            return getattr(item, key, _DEFAULT)

    class First:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __call__(self, state: list | tuple) -> Any:
            return next(item for item in state if value_getter(item, self.key) == self.value)

        def __repr__(self) -> str:
            return f'@({self.key}=={self.value})'

    class ByKey:
        def __init__(self, key):
            self.key = key

        def __call__(self, state) -> Any:
            # if isinstance(self.key, int) or isinstance(state, dict):
            #     return state[self.key]
            # else:
            #     return getattr(state, self.key)
            match self.key, state:
                case int(), _:
                    return state[self.key]
                case _, {self.key: value}:
                    return value
                case _, _:
                    return getattr(state, self.key)

        def __repr__(self) -> str:
            if isinstance(self.key, int):
                return f'[{self.key}]'
            else:
                return f'.{self.key}'
    return Walk, WalkError


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Support du "/" pour les chemins de données""")
    return


@app.cell
def _(data):
    data
    return


@app.cell
def _(Walk, data):
    # implémentation du chemin des données
    def test_walk_no_selector():
        assert Walk().walk(data) == data

    def test_walk_dict_key_selector():
        assert (Walk() / 'name').walk(data) == 'Lucie Nation'

    def test_walk_list_index_selector():
        assert (Walk() / 'friends' / 0 / 'name').walk(data) == 'Frankie Manning'

    def test_walk_object_attr_selector():
        assert (Walk() / 2 / 'type').walk(data['pets']) == 'bird'

    return


@app.cell
def _(Walk, WalkError, data, pytest):
    # messages d'erreur explicites
    def test_walk_mismatching_steps_empty_list():
        with pytest.raises(WalkError) as error:
            phone_number = Walk() / 'friends' / 0 / 'phones' / 1 | data
        walk_error = error.value
        assert str(walk_error) == (
            'walked (.friends [0] .phones) of (.friends [0] .phones [1]) but could not find [1] in the current data state'
        )
        assert walk_error.data_state == []

    def test_walk_mismatching_steps_dict_without_key():
        with pytest.raises(WalkError) as error:
            phone_number = Walk() / 'friends' / 2 / 'phones' / 0 | data
        walk_error = error.value
        assert str(walk_error) == (
            'walked (.friends [2]) of (.friends [2] .phones [0]) but could not find .phones in the current data state'
        )
        assert walk_error.data_state == {"name": "Suzie Q", "phone": "06 43 15 27 98"}

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ```python
    class Walk:
        # ...
        def __truediv__(self, step: Hashable) -> 'Walk':
            '''
            >>> walk / 'key'
            '''
            return Walk(*self.selectors, ByKey(step))

    class ByKey:
        def __init__(self, key):
            self.key = key

        def __call__(self, state) -> Any:
            if isinstance(self.key, int) or isinstance(state, dict):
                return state[self.key]
            else:
                return getattr(state, self.key)

        def __repr__(self) -> str:
            if isinstance(self.key, int):
                return f'[{self.key}]'
            else:
                return f'.{self.key}'
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Support de l'opérateur "|" pour rechercher une valeur""")
    return


@app.cell
def _(Walk, data):
    # implémentation de l'opérateur "|" pour .walk(...)
    def test_walk_no_selector_with_pipe():
        assert Walk() | data == data

    def test_walk_dict_key_selector_with_pipe():
        assert Walk() / 'name' | data == 'Lucie Nation'

    def test_walk_list_index_selector_with_pipe():
        assert Walk() / 'friends' / 0 / 'name' | data == 'Frankie Manning'

    def test_walk_object_attr_selector_with_pipe():
        assert Walk() / 2 / 'type' | data['pets'] == 'bird'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ```python
    class Walk:
        # ...
       def __or__(self, data) -> Any:
           '''
           >>> walk | data
           '''
           return self.walk(data)
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Support de l'opérateur "@" pour sélectionner une entrée dans une liste""")
    return


@app.cell
def _(Walk, data):
    def test_walk_select_first_by_key_value_friend():
        assert Walk() / 'friends' @ ('name', 'Suzie Q') / 'phone' | data == '06 43 15 27 98'

    def test_walk_select_first_by_key_value_pet():
        assert Walk() / 'pets' @ ('type', 'bird') / 'name' | data == 'Melody'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ```python
    class Walk:
        # ...
        def __matmul__(self, filter: tuple[Hashable, Hashable]) -> Any:
            '''
            >>> walk @ (key, value)
            '''
            match filter:
                case [key, value]:
                    return Walk(*self.selectors, First(key, value))
                case _:
                    raise ValueError(f'unsupported filter: {filter}')

    _DEFAULT = object()
    def value_getter(item: dict | object, key: Hashable):
        if isinstance(item, dict):
            return item.get(key, _DEFAULT)
        else:
            return getattr(item, key, _DEFAULT)

    class First:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __call__(self, state: list | tuple) -> Any:
            return next(item for item in state if value_getter(item, self.key) == self.value)

        def __repr__(self) -> str:
            return f'@({self.key}=={self.value})'
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Support de l'opérateur "%" pour sélectionner des entrées dans une séquence""")
    return


@app.cell
def _(Walk, caramel, data, socks):
    def test_walk_select_all_by_key_in_values_pets():
        assert Walk() / 'pets' % ('name', ['Caramel', 'Socks']) | data == [caramel, socks]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ```python
    class Walk:
        # ...
        def __mod__(self, filter: tuple[Hashable, Iterable]):
            '''
            >>> walk % (key, [values])
            '''
            match filter:
                case [key, [*values]]:
                    return Walk(*self.selectors, All(key, values))

                case [key, value]:
                    raise ValueError(f'unsupported filter: {filter}, value {value} must be a sequence')

                case _:
                    raise ValueError(f'unsupported filter: {filter}')

    class All:
        def __init__(self, key: Hashable, values: Iterable):
            self.key = key
            self.values = values

        def __call__(self, state: Iterable[dict | object]) -> list:
            return [item for item in state if value_getter(item, self.key) in self.values]

        def __repr__(self) -> str:
            return f'%({self.key} in {self.values})'


    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## C'est dommage de commencer les chemins par une instance vide `Walk()` 🙁""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Tutoriel détaillé : https://realpython.com/python-metaclasses/

    > Metaclasses are deeper magic than 99% of users should ever worry about.
    > If you wonder whether you need them, you don’t (the people who actually need them know with certainty that they need them, and don’t need an explanation about why).

        — Tim Peters (auteur du "zen of Python")

    ```python
    a_walk = Walk()
    type(a_walk)                 # <class '__main__.Walk'> Walk est la classe de a_walk 
    a_walk.__class__             # <class '__main__.Walk'>
    type(a_walk.__class__)       # <class 'type'> type est la métaclasse de Walk
    type(type(a_walk.__class__)) # <class 'type'> type est la métaclasse de type
    ```
    """
    )
    return


@app.cell
def _(Walk):
    a_walk = Walk()
    print('a_walk est une instance de', type(a_walk))
    print('a_walk est une instance de', a_walk.__class__)
    print(a_walk.__class__, 'est une instance de', type(a_walk.__class__))
    print(type(a_walk.__class__), 'est une instance de', type(type(a_walk.__class__)))

    # une classe est une instance de sa métaclasse
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ```python
    class MetaWalk(type):
        '''
        Hériter de type fait de MetaWalk une métaclasse
        '''
        def __truediv__(cls, step: Hashable) -> 'Walk':
            return Walk(ByKey(step))

        def __matmul__(cls, filter: tuple[Hashable, Hashable]) -> Any:
            return Walk(First(*filter)) # ou return Walk() @ filter

        def __mod__(cls, filter: tuple[Hashable, Iterable]):
            return Walk(All(filter))    # ou return Walk() % filter

    class Walk(metaclass=MetaWalk):
        ...
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Version de `ByKey` avec du pattern matching structurel

    Documentation :
    - PEP 636 qui en présente le formalisme et utilisations : https://peps.python.org/pep-0636/
    - un tutoriel approfondi : https://realpython.com/structural-pattern-matching/
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ```python
    class ByKey:
        # ...
        def __call__(self, state) -> Any:
            match self.key, state:
                case int(), _:
                    return state[self.key]
                case _, {self.key: value}:
                    return value
                case _, _:
                    return getattr(state, self.key)
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Représentation du chemin de données

    ```python
    class Walk:
        def __repr__(self) -> str:
            return ' '.join(f'{selector}' for selector in self.selectors)
    ```
    """
    )
    return


@app.cell
def _(Walk):
    def test_walk_representation_by_keys():
        assert repr(Walk() / 'pets' / 2 / 'name') == '.pets [2] .name'
        assert str(Walk() / 'pets' / 2 / 'type') == '.pets [2] .type'

    def test_walk_representation_first():
        assert f"{Walk() / 'pets' @ ('type', 'bird') / 'name'}" == '.pets @(type==bird) .name'

    def test_walk_representation_all():
        assert f"{Walk() / 'pets' % ('type', ['bird', 'dog'])}" == ".pets %(type in ['bird', 'dog'])"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Conclusion

    🙏 pour votre attention ; ça va la tête 😬 ?

    - 🧰 les méthodes spéciales permettent d'ajouter du comportement à des instances, déclenché par les opérateurs
    - ⚠️ attention aux priorités des opérateurs
    - 🥴 dissonance entre le nom des méthodes magiques et le rôle qu'on souhaite leur donner
    - une classe est une **instance** de sa métaclasse (`type` par défaut)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Utiliser `datawalk` dans votre projet ? https://github.com/lucsorel/datawalk (-> ⭐ 🫶)

    - concaténation de chemins

    ```python
    friends_walk = Walk / 'friends'
    first_phone_walk = Walk / 'phones' / 0
    friends_walk + first_phone_walk | data
    ```

    - gère aussi les slices

    ```python
    Walk / 'pets' / slice(None, None, -1) # -> pets[::-1], inverse l'ordre
    ```

    - gère les valeurs par défaut

    ```python
    first_lion_walk = Walk / 'pets' / @ ('type', 'lion') / 'name'
    first_lion_walk.walk(data, 'Léo')
    # ou avec l'opérateur "^"
    first_lion_walk ^ (data, 'Léo')
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Si vous vouliez créer une syntaxe, ça serait pour manipuler quoi ?""")
    return


if __name__ == "__main__":
    app.run()
