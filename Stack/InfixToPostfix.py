from Stack.ArrayStack import Stack

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def convert(S):
    opStack = Stack()
    answer = ''

    for c in S:
        if c not in "*/+-()":
            answer += c
        elif c == '(':
            opStack.push(c)
        elif c == ")":
            while opStack.peek() != "(":
                answer += opStack.pop()
            opStack.pop()
        elif (not opStack.is_empty()) and prec.get(c) <= prec.get(opStack.peek()):
            answer += opStack.pop()
            opStack.push(c)
        else:
            opStack.push(c)

    while not opStack.is_empty():
        answer += opStack.pop()

    return answer


def convert_(s):
    stack = []
    re = ''
    for c in s:
        if c not in '()+-*/':
            re += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                re += stack.pop()
            stack.pop()
        elif stack and prec[c] <= prec[stack[-1]]:
            re += stack.pop()
            stack.append(c)
        else:
            stack.append(c)

    while stack:
        re += stack.pop()
    return re


def split_token(expStr):
    tokens = []
    val = 0
    valProcessing = False

    for c in expStr:
        if c == " ":
            continue
        elif c in "0123456789":
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0

            valProcessing = False
            tokens.append(c)

    if valProcessing:
        tokens.append(val)

    return tokens


def convert_postfix(tokens):
    prec = {
        "*": 3, "/": 3,
        "+": 2, "-": 2,
        "(": 1,
    }

    stack = Stack()
    result = []

    for token in tokens:
        if token in prec.keys():
            if token == "(" or stack.is_empty():
                stack.push(token)
            elif prec.get(stack.peek()) < prec.get(token):
                stack.push(token)
            else:
                result.append(stack.pop())
                stack.push(token)
        elif token == ")":
            while stack.peek() != "(":
                result.append(stack.pop())
            stack.pop()
        else:
            result.append(token)

    while not stack.is_empty():
        result.append(stack.pop())

    return result


def test():
    result = []
    test_case = ['1+2 * (3+1)', '1+3*4', "(1 + 2) * (2 *3)", "(3 * 2) - (1 + 2 * 3)", '7 * (9 - (3 + 2))',
                 '5 + 3', '(1 + 2) * (3 + 4)', '7 * (9-(3+2))', '3 + (2 - 3 * (1 + 2 + ( 4 * 2 - 1)))']
    for tc in test_case:
        tokens = split_token(tc)
        result.append("".join(map(str, convert_postfix(tokens))))
    return result


if __name__ == "__main__":
    # test cases
    print(convert('(A+B)*C'))
    print(convert('a+b+c'))
    print(convert('a+b*c'))
    print(convert('a*b-c'))
    print(convert('(A+B*C)+D'))
    print(convert('(A*B-C)-D'))
    print(convert('(A*B)-(D*E+F)'))
    print(test())