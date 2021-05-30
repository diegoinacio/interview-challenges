
# ! Problem

# {[()]} is balanced.
# {[(])} is not balanced.
# {{[[(())]]}} is balanced.

# ? Function Description

# It must return a string: YES if the sequence is balanced
# or NO if it is not.

# "isBalanced" has the following parameter(s):
# - input_string: a string of brackets


def isBalanced(input_string: str) -> bool:
    # * Define valid bracket pairs
    brackets = [r'()', r'[]', r'{}']
    # * Remove extra information from input string
    input_string = "".join(e for e in input_string if e in "".join(brackets))
    # * Loop while exist any pair in the input string
    while any(b in input_string for b in brackets):
        for b in brackets:
            input_string = input_string.replace(b, '')
    return "NO" if input_string else "YES"
