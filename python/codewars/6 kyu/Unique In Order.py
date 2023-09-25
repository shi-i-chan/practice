def unique_in_order(lst):
    if len(lst) > 0:
        unique = [lst[0]]
        for index in range(len(lst) - 1):
            if lst[index] != lst[index + 1]:
                unique.append(lst[index + 1])
        return unique
    else:
        return []
