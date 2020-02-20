
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
    # Define valid bracket pairs
    brackets = [r'()', r'[]', r'{}']
    # Remove extra information from input string
    input_string = ''.join(
        filter(lambda x: x in ''.join(brackets), input_string)
    )
    # Loop while exist any pair in the input string
    while any(x in input_string for x in brackets):
        for bracket in brackets:
            input_string = input_string.replace(bracket, '')
    return 'YES' if not input_string else 'NO'
