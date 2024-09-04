
"""
Case 1: dictionary, ex: {14:'N'},
    Case 1.2 if key not integer, check what's inside {'hah,trick':{4:'G'}},
Case 2: tuple, ex: (5,'R'),
Case 3: list, ex: [3,'N'],
Case 4: integer ex: ,7,'T',
Case 5: set, ex: {6,'A'}
"""

a = [{6, 'A'}, (5, 'R'), {2: 'O'}, {1: 'C'}, [3, 'N'],
     {'hah,trick': {4: 'G'}},
     7, 'T', 8, 'U', 9, 'L', 10, 'A', {15: 'S'}, {14: 'N'}, {11: 'T'}, {12: 'I'}]

i = 0
output = []
while i < len(a):
    checked = a[i]
    type_checked = type(checked)
    pair = [-1,-1]
    if type_checked == type(set()):
        for j in checked:

            if type(j) == type(int()):
                pair[0] = j
            else:
                pair[1] = j

    if type_checked == type(tuple()):
        pair[0], pair[1] = checked[0], checked[1]
    if type_checked == type(list()):
        pair[0], pair[1] = checked[0], checked[1]
    if type_checked == type(int()):
        pair = [checked, a[i + 1]]
        i += 1
    if type_checked == type(dict()):
        for key in checked.keys():
            print(key)
            if key == type(int()):
                pair[0], pair[1] = key, checked[key]
            else:
                measures = checked[key]
                print(measures)
                for deep_key in measures.keys():
                    pair[0], pair[1] = deep_key, checked[deep_key]
    output.append(pair)
    i += 1

print(output)
#lambda func to sort list of value/index pairs