import decorators


dict = {
    'a': 1,
    'b': 21374,
    'c': 6,
}
@decorators.timer
def k_maxOfDict(dict: dict[int], k:int):

    keys = [key for key in dict.keys()]
    keys.sort(key = lambda value: dict[value], reverse = True)

    return keys[:k]


print(k_maxOfDict(dict, 2))