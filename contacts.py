
# ! Problem

# [
# 	["add", "hack"],
# 	["add", "hackerrank"],
# 	["find", "hac"],
# 	["find", "hak"]
# ] -> [2, 0] is the output

# [
# 	["add", "diego"],
# 	["add", "diogo"],
# 	["add", "diogenes"],
# 	["find", "die"],
# 	["find", "dio"]
# ] -> [1, 2] is the output

# ? Function Description

# * Given a 2D input stream of string, containing queries ..
# * which the first position is the operation and the ..
# * second is the name
# 1 - When the operation is "add", include the name to the
#     list of names;
# 2 - When the operation is "find", search for names in the
#     list that matches the partial name given;
# 3 - The output must have the number of names that matches
#     the partial name for each operation "find".


from typing import List, Tuple


def contacts(queries: List[List[str]]) -> List[int]:
    names, result = [], []
    # * Loop through queries
    for operation, name in queries:
        if operation == "add":
            names += [name]
        if operation == "find":
            result += [sum(n.startswith(name) for n in names)]
    return result
