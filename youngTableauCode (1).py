import pdb
class YoungTableau:
	def __init__(self,m,n):
		self.m = m
		self.n = n
		self.young_T = [[float("inf") for i in range(m)] for j in range(n)]

	def extract_min(self):
		x = self.young_T[0][0]
		self.young_T[0][0] = float("inf")
		self.youngify(0,0);
		return x

	def find_elem(self,elem):
		i = 0
		j = self.n-1
		while( i < self.m and  j >= 0) :
			if self.young_T[i][j] < elem :
				i += 1
			elif self.young_T[i][j] > elem:
				j -= 1
			else : 
				return True
		return False

	def youngify(self,i,j):
		x=i
		y=j
		if(i+1 < self.m):
			if (self.young_T[i][j] > self.young_T[i+1][j]) :
				x = x+1
				y=j
		if(j+1 < self.n):
			if(self.young_T[x][y] > self.young_T[i][j+1]):
				x=i
				y=j+1
		if(x!=i or y != j) :
			self.young_T[i][j],self.young_T[x][y] = self.young_T[x][y],self.young_T[i][j]
			self.youngify(x,y)

	def insert_key(self,i,j,key):
		if(self.young_T[i][j] < key):
			print('No more insertion possible')
			return
		# print(f'{i} {j} ')
		self.young_T[i][j] = key
		x =i
		y= j
		max_v = float("inf")
		while(i > 0 or j > 0 ) and (max_v > self.young_T[i][j]) :
			self.young_T[i][j],self.young_T[x][y] = self.young_T[x][y],self.young_T[i][j]
			i = x
			j = y
			if ( i - 1 >= 0 and (self.young_T[i][j] < self.young_T[i-1][j] )):
				x = i-1
				y = j
			if ( j - 1 >= 0 and (self.young_T[x][y] < self.young_T[i][j-1]) ) :
				x = i  
				y = j - 1
			max_v = self.young_T[x][y]
		# self.display()

	def sort(self):
		n_indexes = [0]*self.n
		result = []
		for i in range(self.n*self.m):
			min_val = float("inf")
			min_index = 0
			# pdb.set_trace()
			for j in range(self.m):
				if (n_indexes[j] < self.n and self.young_T[n_indexes[j]][j] < min_val) :
					min_val = self.young_T[n_indexes[j]][j]
					min_index = j
			if min_val != float("inf"):
				result.append(min_val)
			n_indexes[min_index] += 1
				# print(n_indexes)
		return result

	def display(self):
		print('\n \n ************ OUTPUT ***************')
		for (i,_i) in enumerate(self.young_T) :
			for (j,_j) in enumerate(self.young_T[i]):
				print(str(self.young_T[i][j]),end = " ")
			print("\n")
		# print(self.young_T)