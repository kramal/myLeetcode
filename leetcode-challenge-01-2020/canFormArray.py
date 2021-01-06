def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    has_been_changed = 0
    for item_list in pieces:
        for i in range(len(arr)):
            if arr[i] == item_list[0]:
                has_been_changed += 1
                size_item_list = len(item_list)

                if size_item_list == 1:
                    continue

                if i + size_item_list > len(arr):
                    return False

                for j in range(1, size_item_list):
                    if arr[i + j] != item_list[j]:
                        return False

    return True if has_been_changed == len(pieces) else False
