from young_tableaus import YoungTableau
size_of_yt =  input("Enter value of m and n space separated : \n")
m,n = size_of_yt.split(" ")
m = int(m)
n = int(n)
yt = YoungTableau(m,n)
array_l = input("Enter an array space separated less than m * n : \n")
array_l = array_l.split(" ")
i,j= 0,0
for (idx,val) in enumerate(array_l) :
	yt.insert_key(i,j,int(val))
	j = j + 1
	if (idx + 1) % n == 0 and idx != 0:
		i = i + 1
		j = 0

yt.display()

print('Extracting minimum from young_tableaus ')

print(f'Minimum element: {yt.extract_min()}' )

print(f'Displaying new young_tableau')

yt.display()

print('Sorting Array ... Please Wait... ')
print(f'Sorted Array: {yt.sort()}')

print('Finding Elements in YoungTableau ...... :')
print(f'Find element 4 in : {yt.find_elem(4)}')
print(f'Find element 100 in : {yt.find_elem(100)}')

# find_elem = input('Enter value to be found in young_tableau : \n')
