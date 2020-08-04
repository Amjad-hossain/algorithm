# Given a string containing just the characters '(', ')', '{', '}', '[' and ']'
# Write a function in Java or C++ to check if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not


def is_valid(parentheses):
    stack = []
    for val in parentheses:
        if val == '(' or val == '{' or val == '[':
            stack.append(val)
        elif val == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif val == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
        elif val == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False

    if len(stack) == 0:
        return True
    return False


assert is_valid("()[]{}") == True
assert is_valid("(()[]{}") == False
assert is_valid("()[]{}}") == False
assert is_valid("{()[]{}}") == True
assert is_valid("{(){[]}{}}") == True
assert is_valid("[{(){[()]}{}}]") == True
assert is_valid("[{(){[())]}{}}]") == False
assert is_valid("[{(){[(a+b)+5*6]}{}}]") == True
