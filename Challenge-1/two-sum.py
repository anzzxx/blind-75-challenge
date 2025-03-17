arr=[6,7,8,9,7]

target=14
map=dict()

for i in range(len(arr)-1):
    if target-arr[i] not in map:
        map[arr[i]]=i
    else:
        print(map[target-arr[i]],i)

    
