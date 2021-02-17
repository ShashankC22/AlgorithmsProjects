#Maximun Subarray Problem

def maximumSum(array, left, middle, right) :

	# entries from left to the middle of the array
	sum = 0; sumLeft = -10000

	for i in range(middle, left-1, -1) :
		sum = sum + array[i]

		if (sum > sumLeft) :
			sumLeft = sum


	# entries from middle to the end of the array
	sum = 0; sumRight = -1000
	for i in range(middle + 1, right + 1) :
		sum = sum + array[i]

		if (sum > sumRight) :
			sumRight = sum


	# returns the sum from the left and right sides of the array
	return sumLeft + sumRight;


def maximunArraySum(array, left, right) :

	# if the array has only one element (base case)
	if (left == right) :
		return array[left]

	# divide the array into two, divide and conquer
	middle = (left + right) // 2

# 3 possible cases here:
# case 1: returns the subarray sum of the left part of the given array
#case 2: returns the subarray sum of the right part of the given array
# case 3: returns the subarray sum of the maxcrossing of the middle part of the array
	return max(maximunArraySum(array, left, middle),
			maximunArraySum(array, middle+1, right),
			maximumSum(array, left, middle, right))


array = [-1,3,4,-5,9,-2]
n = len(array)

maximumsum = maximunArraySum(array, 0, n-1)
print(" The Maximum sum is ", maximumsum)
