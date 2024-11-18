import copy

def Extend_Type_I(k, res):
	Type_I_state_vector_extend = []
	for i in range (len(res)):
		if (k > len(Type_I_state_vector[res[i]])-1):
			Type_I_state_vector_extend.append(Type_I_state_vector[res[i]][-1])
		else:
			Type_I_state_vector_extend.append(Type_I_state_vector[res[i]][k])
	return Type_I_state_vector_extend

def Extend_Type_II(k, res):
	Type_II_state_vector_extend = []
	for i in range (len(res)):
		if (k > len(Type_II_state_vector[res[i]])-1):
			Type_II_state_vector_extend.append(Type_II_state_vector[res[i]][-1])
		else:
			Type_II_state_vector_extend.append(Type_II_state_vector[res[i]][k])
	return Type_II_state_vector_extend

def Find_Type_I(SS_K_I_TEMP):
	res = []

	MAX_0 = len(SS_K_I_TEMP[0])
	for i in range (1, len(SS_K_I_TEMP)):
		MAX_0 = min(MAX_0, len(SS_K_I_TEMP[i]))

	for j in range (MAX_0):
		MAX_1 = SS_K_I_TEMP[0][j][0]
		for i in range (1, len(SS_K_I_TEMP)):
			MAX_1 = max(MAX_1, SS_K_I_TEMP[i][j][0])

		temp = []
		for i in range (len(SS_K_I_TEMP)):
			if (SS_K_I_TEMP[i][j][0] == MAX_1):
				temp.append(SS_K_I_TEMP[i][j])

		MAX_2 = temp[0][1]
		for i in range (1, len(temp)):
			MAX_2 = max(MAX_2, temp[i][1])

		res.append([MAX_1,MAX_2])
	return(res)

def Find_Type_II(SS_K_II_TEMP):
	res = []

	MAX_0 = len(SS_K_II_TEMP[0])
	for i in range (1, len(SS_K_II_TEMP)):
		MAX_0 = min(MAX_0, len(SS_K_II_TEMP[i]))

	for j in range (MAX_0):
		MAX_2 = SS_K_II_TEMP[0][j][1]
		for i in range (1, len(SS_K_II_TEMP)):
			MAX_2 = max(MAX_2, SS_K_II_TEMP[i][j][1])

		temp = []
		for i in range (len(SS_K_II_TEMP)):
			if (SS_K_II_TEMP[i][j][1] == MAX_2):
				temp.append(SS_K_II_TEMP[i][j])

		MAX_1 = temp[0][0]
		for i in range (1, len(temp)):
			MAX_1 = max(MAX_1, temp[i][0])

		res.append([MAX_1,MAX_2])
	return(res)

def Themore_1(i, k, res, temp_2):
	Type_I_state_vector_extend = Extend_Type_I(k, res)
	Type_II_state_vector_extend = Extend_Type_II(k, res)

	if (i == 0):
		p = min(Type_I_state_vector_extend[1][0] - Type_I_state_vector_extend[0][0], Type_I_state_vector_extend[1][1], k - 1)
		q = min((k - 1) - p, Type_I_state_vector_extend[0][1], Type_I_state_vector_extend[1][1] - p)
		pp = Type_I_state_vector_extend[0][0] + 1 + p
	elif (i == 1):
		p = min(Type_II_state_vector_extend[1][0] - Type_I_state_vector_extend[0][0], Type_II_state_vector_extend[1][1], k - 1)
		q = min((k - 1) - p, Type_I_state_vector_extend[0][1], Type_II_state_vector_extend[1][1] - p)
		pp = Type_I_state_vector_extend[0][0] + 1 + p
	elif (i == 2):
		p = min(Type_I_state_vector_extend[1][0] - Type_II_state_vector_extend[0][0], Type_I_state_vector_extend[1][1], k - 1)
		q = min((k - 1) - p, Type_II_state_vector_extend[0][1], Type_I_state_vector_extend[1][1] - p)
		pp = Type_II_state_vector_extend[0][0] + 1 + p
	else:
		p = min(Type_II_state_vector_extend[1][0] - Type_II_state_vector_extend[0][0], Type_II_state_vector_extend[1][1], k - 1)
		q = min((k - 1) - p, Type_II_state_vector_extend[0][1], Type_II_state_vector_extend[1][1] - p)
		pp = Type_II_state_vector_extend[0][0] + 1 + p
	if (pp > temp_2[-1][0]):
		return ([pp, p + q])
	else:
		return ([temp_2[-1][0]+1, temp_2[-1][1]+1])

def Themore_2(j, k, res, temp_3):
	Type_I_state_vector_extend = Extend_Type_I(k, res)
	Type_I_state_vector_extend_r = Extend_Type_I(k, [len(res)])

	Type_II_state_vector_extend_r = Extend_Type_II(k, [len(res)])

	p = Type_I_state_vector_extend[0][0]
	for i in range (1, len(res)):
		p = min(p, Type_I_state_vector_extend[i][0])

	if (j == 0):
		pp = Type_I_state_vector_extend_r[0][0] + p
	else:
		pp = Type_II_state_vector_extend_r[0][0] + p

	if (pp > temp_3[-1][0]):
		return ([pp, Type_I_state_vector_extend_r[0][1]])
	else:
		return ([temp_3[-1][0]+1, temp_3[-1][1]+1])

def Derived_State_Vector(res, SS_K_I, SS_K_II):
	SS_K_I_TEMP = []
	SS_K_II_TEMP = []
	SS_K_I_TEMP_copy = []
	SS_K_II_TEMP_copy = []

	if (len(res) == 2):
		for i in range (4):
			k = 1
			x = 0
			temp_2 = [[0, 0]]
			while ((x + 1) < K):
				temp_2.append(Themore_1(i, k, res, temp_2))
				x = temp_2[-1][0]
				k = k + 1
			SS_K_I_TEMP.append(temp_2)
			SS_K_II_TEMP.append(temp_2)
			SS_K_I_TEMP_copy.append([[2, i], res, temp_2])
			SS_K_II_TEMP_copy.append([[2, i], res, temp_2])

	if (len(res) > 2):
		for j in range (2):
			k = 1
			x = 0
			temp_3 = [[0, 0]]
			while ((x + 1) < K):
				temp_3.append(Themore_2(j, k, res, temp_3))
				x = temp_3[-1][0]
				k = k + 1
			if (j == 0):
				SS_K_I_TEMP.append(temp_3)
				SS_K_I_TEMP_copy.append([[3, j], res, temp_3])
			else:
				SS_K_II_TEMP.append(temp_3)
				SS_K_II_TEMP_copy.append([[3, j], res, temp_3])

	SS_K_I.append(Find_Type_I(SS_K_I_TEMP))
	SS_K_II.append(Find_Type_II(SS_K_II_TEMP))
	
def Loop_Function(SS_K_I, SS_K_II, R, res, a, b):
	if (a == 1):
		for i in range (b, K+1-R):
			res[R - 1] = i
			temp = 0
			for j in range (R):
				temp = temp + res[j]
			if (temp < K) and ((K-temp) >= res[-1]):
				res_temp = copy.deepcopy(res)
				res_temp.append(K-temp)
				# print(res_temp)
				Derived_State_Vector(res_temp, SS_K_I, SS_K_II)
	else:
		for i in range (b, K+1-R):
			res[R - a] = i
			Loop_Function(SS_K_I, SS_K_II, R, res, a - 1, i)


# def A(SS_K_I, SS_K_II, R, K, B):
# 	res = [0 for i in range (R)]
# 	Loop_Function(SS_K_I, SS_K_II, R, res, R, B)

if __name__ == '__main__':
	Type_I_state_vector = [
	[[0, 0]], # The Type_I_state_vector of 0-XOR algorithm
	[[0, 0]], # The Type_I_state_vector of 1-XOR algorithm
	[[0, 0], [1, 0]], # The Type_I_state_vector of 2-XOR algorithm
	[[0, 0], [1, 0], [2, 1]], # The Type_I_state_vector of 3-XOR algorithm
	]

	Type_II_state_vector = [
	[[0, 0]], # The Type_II_state_vector of 0-XOR algorithm
	[[0, 0]], # The Type_II_state_vector of 1-XOR algorithm
	[[0, 0], [1, 0]], # The Type_II_state_vector of 2-XOR algorithm
	[[0, 0], [1, 0], [2, 1]], # The Type_II_state_vector of 3-XOR algorithm
	]

	for K in range (4, 30): #Search for Type_I/Type_II state vectors of the k-XOR algorithms, where 4 \leq k < 30.
		SS_K_I = []
		SS_K_II = []
		Begin_point = 1
		for r in range (2, K-1):
			res = [0 for i in range (r)]
			Loop_Function(SS_K_I, SS_K_II, r, res, r, Begin_point)
		Type_I_state_vector.append(Find_Type_I(SS_K_I))
		Type_II_state_vector.append(Find_Type_II(SS_K_II))

		print("The type_I_state_vector of the %d-XOR algorithm is :" % K, Type_I_state_vector[K])
		print("The type_II_state_vector of the %d-XOR algorithm is :" % K, Type_II_state_vector[K] )

# [[0, 0], [2, 0], [3, 1]]
# [[0, 0], [2, 0], [3, 1]]
# [[0, 0], [2, 0], [3, 1], [4, 2]]
# [[0, 0], [2, 0], [3, 1], [4, 2]]
# [[0, 0], [2, 0], [3, 1], [4, 2], [5, 3]]
# [[0, 0], [2, 0], [3, 1], [4, 2], [5, 3]]
# [[0, 0], [2, 0], [4, 1], [5, 2], [6, 3]]
# [[0, 0], [2, 0], [4, 1], [5, 2], [6, 3]]
# [[0, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4]]
# [[0, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4]]
# [[0, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5]]
# [[0, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5]]
# [[0, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6]]
# [[0, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8], [13, 9]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8], [13, 9]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8], [13, 9], [14, 10]]
# [[0, 0], [3, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8], [13, 9], [14, 10]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11], [17, 12]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11], [17, 12]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11], [17, 12], [18, 13]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11], [17, 12], [18, 13]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11], [17, 12], [18, 13], [19, 14]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11], [17, 12], [18, 13], [19, 14]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11], [17, 12], [18, 13], [19, 14], [20, 15]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [8, 3], [9, 4], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [15, 10], [16, 11], [17, 12], [18, 13], [19, 14], [20, 15]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15]]
# [[0, 0], [4, 0], [6, 1], [7, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15]]
# [[0, 0], [4, 0], [6, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16]]
# [[0, 0], [4, 0], [6, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16]]
# [[0, 0], [4, 0], [6, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17]]
# [[0, 0], [4, 0], [6, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17]]
# [[0, 0], [4, 0], [6, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17], [24, 18]]
# [[0, 0], [4, 0], [6, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17], [24, 18]]
# [[0, 0], [4, 0], [6, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17], [24, 18], [25, 19]]
# [[0, 0], [4, 0], [6, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17], [24, 18], [25, 19]]
# [[0, 0], [4, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17], [24, 18], [25, 19], [26, 20]]
# [[0, 0], [4, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17], [24, 18], [25, 19], [26, 20]]
# [[0, 0], [4, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17], [24, 18], [25, 19], [26, 20], [27, 21]]
# [[0, 0], [4, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5], [12, 6], [13, 7], [14, 8], [15, 9], [16, 10], [17, 11], [18, 12], [19, 13], [20, 14], [21, 15], [22, 16], [23, 17], [24, 18], [25, 19], [26, 20], [27, 21]]
# [[0, 0], [4, 0], [7, 1], [8, 2], [10, 3], [11, 4], [12, 5], [13, 6], [14, 7], [15, 8], [16, 9], [17, 10], [18, 11], [19, 12], [20, 13], [21, 14], [22, 15], [23, 16], [24, 17], [25, 18], [26, 19], [27, 20], [28, 21]]
# [[0, 0], [4, 0], [7, 1], [8, 2], [10, 3], [11, 4], [12, 5], [13, 6], [14, 7], [15, 8], [16, 9], [17, 10], [18, 11], [19, 12], [20, 13], [21, 14], [22, 15], [23, 16], [24, 17], [25, 18], [26, 19], [27, 20], [28, 21]]