from expylliarmus.match import SPELL_MATCHER

from pytest import mark

def test_SPELL_MATCHER_Pascal_Case_spell():
    assert 'Expylliarmus!' == SPELL_MATCHER.match('Expylliarmus!').group(0)
    assert 'Youpi!' == SPELL_MATCHER.match('Youpi!').group(0)
    assert 'Mischief managed!' == SPELL_MATCHER.match('Mischief managed!').group(0)
    assert 'Wingardium Leviosa!' == SPELL_MATCHER.match('Wingardium Leviosa!').group(0)

@mark.parametrize('source_text,expected_text', [
    ['EXPELLIARMUS!', 'EXPELLIARMUS!'],
    ['WINGARDIUM LEVIOSA!', 'WINGARDIUM LEVIOSA!']
])
def test_SPELL_MATCHER_UPPER_CASE_spell(source_text, expected_text):
    assert expected_text == SPELL_MATCHER.match(source_text).group(0)

def test_SPELL_MATCHER_do_not_match():
    assert SPELL_MATCHER.match('hello!') is None
    assert SPELL_MATCHER.match('expelliarmus') is None
