def get_cycle(hash_path, visiteds):

    for index, vals in hash_path.items():
        visiteds = {index: True}

        for el in vals:
            if el in visiteds:
                continue

            if el == index:
                return visiteds
            else:
                visiteds[el] = True
                get_cycle(hash_path, visiteds)


data = [
    [0,1]
    ,[1,2]
    ,[1,4]
    ,[2,3]
    ,[3,4]
]

hash_path = {}

for item in data:
    hash_path[item[0]] = []

for item in data:
    hash_path[item[0]].append(item[1])



