
# ! Problem

# Suggests words from a repository based on a customer query.
# The suggestion will consider only the query from the second letter.

# ? Function Description

# * Given a repository with a list of distinct words
# * .. and a customer query, perform the following tasks:
# 1 - Convert all words on the repository to lowercase and sort
#     them to alphabetical order;
# 2 - Get all the possible ranges of the customer query, starting
#     from the second letter;
# 3 - Return a list of lists of words that start with each range
#     of the custom query.

# * customerQuery: bags
# * repository: ["baggage", "bags", "banner", "box", "cloths"]
# * Output:
# * [
# *     ["baggage", "bags", "banner"] <- "ba"
# *     ["baggage", "bags"]           <- "bag"
# *     ["bags"]                      <- "bags"
# * ]


from typing import List


def searchSuggestions(repository: List[str], customerQuery: str, limit: int = 3) -> List[List[str]]:
    # * Sort and guarantee only lowercase words in the repository
    repository_ = sorted(map(lambda e: e.lower(), repository))
    # * Find the proper range for the customer query
    # * .. in the case that its length is bigger than the
    # * .. buggest word in the repository.
    N = min(len(customerQuery), max([len(e) for e in repository]))
    # * Define list of queries
    customerQuery_ = [customerQuery.lower()[:i] for i in range(2, N + 1)]
    # * Return the filtered list of words
    return [list(filter(lambda e: e.startswith(e2), repository_))[:limit] for e2 in customerQuery_]
