def findKthPositive(self, arr: List[int], k: int) -> int:
    list_missing = []
    result = False

    for i in range(1, arr[-1] + 1):
        if i not in arr:
            list_missing.append(i)

    if (k - 1) < len(list_missing):
        result = list_missing[k - 1]
    else:
        if len(list_missing) > 0:
            if list_missing[-1] < arr[-1]:
                max_val_missing = arr[-1] + 1
                result = max_val_missing

            if (k - 1) > len(list_missing):
                for i in range(k - 1 - len(list_missing)):
                    max_val_missing += 1
                result = max_val_missing

        else:
            max_val_missing = arr[-1]
            for i in range(1, k + 1):
                max_val_missing += 1
            result = max_val_missing

    return result
