from collections import deque


class Parser:
    """Evaluates basic mathematical expressions.
    """
    def __init__(self):
        # in order of precedence
        self.operators = [
            '^', '*', '/', '+', '-',
        ]

    def parse_infix(self, _input):
        """Returns value of an expression, written in infix form.
        """
        rpn = self.infix_to_rpn(_input)
        return self.eval_rpn(rpn)

    def infix_to_rpn(self, _input):
        """Translates infix form to reverse polish notation.
        """
        output = []
        operators = []
        tokens = _input.split()

        for token in tokens:
            if token.isdigit():
                output.append(token)
            if token in self.operators:
                precedence = self.operators.index(token)
                for operator in reversed(operators):
                    if operator == '(' or operator == ')':
                        break
                    elif self.operators.index(operator) < precedence:
                        output.append(operators.pop())
                    else:
                        break
                operators.append(token)
            if token == '(':
                operators.append(token)
            if token == ')':
                for operator in reversed(operators):
                    if operator is '(':
                        operators.pop()
                        break
                    else:
                        output.append(operators.pop())
        for operator in operators:
            output.append(operators.pop())

        return ' '.join(output)

    def eval_rpn(self, _input):
        """Computes an expression, written in reverse polish notation.
        """
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

        stack = deque()

        for token in _input.split():
            if token in operations:
                arguments = [stack.pop(), stack.pop()][::-1]
                stack.append(operations[token](*arguments))
            else:
                stack.append(float(token))

        return stack[0]
