import pytest


@pytest.fixture
def parser():
    from math_expression_parser import Parser
    return Parser()

@pytest.mark.parametrize('test_input, expected', [
    ('3 + 8', '3 8 +'),
    ('( 3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3 )', '3 4 2 * 1 5 - 2 3 ^ ^ / +'),
])
def test_eval(test_input, expected, parser):
    assert parser.infix_to_rpn(test_input) == expected
