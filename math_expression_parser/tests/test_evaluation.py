import pytest


@pytest.fixture
def parser():
    from math_expression_parser import Parser
    return Parser()

@pytest.mark.parametrize('test_input, expected', [
    ('3+8', 11),
    ('8*(1+2)', 24),
    ('1-(((100-100)))', 1),
])
def test_eval(test_input, expected, parser):
    assert parser.parse_infix(test_input) == expected
