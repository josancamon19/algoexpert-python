def balancedBrackets(string):
    # Write your code here.
    stack = []
    for bracket in string:
        if len(stack) == 0:
            stack.append(bracket)
        elif bracket in '()[]{}':
            stack.pop(-1) if is_reversed(stack[-1], bracket) else stack.append(bracket)

    return len(stack) == 0


def is_reversed(b1, b2):
    if b1 == '(' and b2 == ')':
        return True
    elif b1 == '[' and b2 == ']':
        return True
    elif b1 == '{' and b2 == '}':
        return True
    else:
        return False
