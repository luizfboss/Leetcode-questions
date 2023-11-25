# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

def isValid(s: str) -> bool:
        stack = []
        # only use isEmpty() -> len(stack), pop(), append()
        possibilities = {"(": ")", "[": "]", "{": "}"}
        closing = '}])'

        for char in s:
            # if stack is empty and it is a closing one
            if len(stack) == 0:
                if char in possibilities.values():
                    return False
                else:
                    stack.append(char)
                    continue
            else:
                peek = stack[-1]
                # if last in stack is associated to the current one, push into the stack
                if possibilities[peek] == char:
                    stack.pop()
                    continue
                # if element is an opening one, push it into the stack
                elif char in possibilities.keys():
                    stack.append(char)
                    continue
                return False
        return len(stack) == 0