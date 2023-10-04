
from re import compile

# SPELL_MATCHER = compile(r'([A-Z]{1}[a-z]+(\s[A-Z]{0,1}[a-z]+)?)!')
SPELL_MATCHER = compile(r'((?:[A-Z]{5,})(?:\s[A-Z]{5,})?|(?:[A-Z]{1}[a-z]+(?:\s[A-Z]{0,1}[a-z]+)?))!')

# immutable 👍
SPELLS = (
    'Accio',
    'Aguamenti',
    'Alohomora',
    'Avada Kedavra',
    'Colloportus',
    'Confringo',
    'Confundo',
    'Crucio',
    'Descendo',
    'Diffindo',
    'Dissendium',
    'Engorgio',
    'Episkey',
    'Evanesco',
    'Expecto Patronum',
    'Expelliarmus',
    'Homenum Revelio',
    'Impedimenta',
    'Imperio',
    'Impervius',
    'Incendio',
    'Levicorpus',
    'Liberacorpus',
    'Locomotor',
    'Lumos',
    'Mobiliarbus',
    'Mischief managed',
    'Morsmordre',
    'Muffliato',
    'Nox',
    'Obliviate',
    'Petrificus Totalus',
    'Portus',
    'Priori Incantato',
    'Protego',
    'Reducto',
    'Relashio',
    'Rennervate',
    'Reparo',
    'Revelio',
    'Rictusempra',
    'Riddikulus',
    'Scourgify',
    'Sectumsempra',
    'Silencio',
    'Sonorus',
    'Stupefy',
    'Taboo',
    'Tergeo',
    'Waddiwasi',
    'Wingardium Leviosa'
)

# mutable! 👎
SPELLS_DICT = {
    'accio': 'Accio',
    'mischief managed': 'Mischief managed',
    'wingardium leviosa': 'Wingardium Leviosa',
    # ...
}
