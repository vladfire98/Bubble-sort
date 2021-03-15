arr = [12,4,1,2,5,75,43,1,3,5,6,7,8,9,100]

for n in range(len(arr)-1):
	for i in range(len(arr)-1):
		if arr[i] > arr[i+1]:
			F = arr[i]
			arr[i] = arr[i+1]
			arr[i+1] = F

print("Способ 1: ", arr)


list = [12,4,1,2,5,75,43,1,3,5,6,7,8,9,100]

for n in range(len(list)-1):
	for i in range(len(list)-1):
		if list[i] > list[i+1]:
			list[i], list[i+1] = list[i+1], list[i]

print("Способ 2: ",list)