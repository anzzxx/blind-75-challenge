def contain_duplicate(arr):
    duplicate=set()
    for i in arr:
        if i not in duplicate:
            duplicate.add(i)
        else:
            return True
    return True



arr=[1,2,3,1]
print(contain_duplicate(arr))                