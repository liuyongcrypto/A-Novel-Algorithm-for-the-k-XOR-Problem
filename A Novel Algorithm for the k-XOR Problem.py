import copy

def Extend_Type_I(k, res):
	Type_I_state_vector_extend = []
	for i in range (len(res)):
		if (k > len(Type_I_state_vector[res[i]])-1):
			Type_I_state_vector_extend.append(Type_I_state_vector[res[i]][-1])
		else:
			Type_I_state_vector_extend.append(Type_I_state_vector[res[i]][k])
	return Type_I_state_vector_extend

def Find_Type_I_MODE_1(SS_K_I_TEMP):
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

def Find_Type_I_MODE_2(SS_K_I_TEMP, SS_K_I_copy, RES_INDEX, k):
	res = []

	MAX_0 = len(SS_K_I_TEMP[0])
	for i in range (1, len(SS_K_I_TEMP)):
		MAX_0 = min(MAX_0, len(SS_K_I_TEMP[i]))

	RES_MAX = []
	for j in range (MAX_0):
		MAX_1 = SS_K_I_TEMP[0][j][0]
		for i in range (1, len(SS_K_I_TEMP)):
			MAX_1 = max(MAX_1, SS_K_I_TEMP[i][j][0])
		RES_MAX.append(MAX_1)

		temp = []
		for i in range (len(SS_K_I_TEMP)):
			if (SS_K_I_TEMP[i][j][0] == MAX_1):
				temp.append(SS_K_I_TEMP[i][j])

		MAX_2 = temp[0][1]
		for i in range (1, len(temp)):
			MAX_2 = max(MAX_2, temp[i][1])

		res.append([MAX_1,MAX_2])

	count_all = 0
	INDEX = 0
	while (count_all < MAX_0):
		
		RES_INDEX[k].append([])
		
		count_max = 0
		for i in range (len(SS_K_I_TEMP)):
			if ((INDEX == 0) and (len(SS_K_I_TEMP[i]) == MAX_0)) or (INDEX > 0):
				count_i = 0
				for j in range (0, MAX_0-count_all):
					
					if (SS_K_I_TEMP[i][MAX_0-1-count_all-j][0] == RES_MAX[MAX_0-1-count_all-j]):
						count_i += 1
					else:
						break
				if (count_i > count_max):
					count_max = count_i		

		for i in range (len(SS_K_I_TEMP)):
			if ((INDEX == 0) and (len(SS_K_I_TEMP[i]) == MAX_0)) or (INDEX > 0):
				count_i = 0
				for j in range (0, MAX_0-count_all):
					# print(i, SS_K_I_copy[i][0], SS_K_I_TEMP[i][MAX_0-1-count_all-j][0], RES_MAX[MAX_0-1-count_all-j])
					if (SS_K_I_TEMP[i][MAX_0-1-count_all-j][0] == RES_MAX[MAX_0-1-count_all-j]):
						count_i += 1
					else:
						break
				if (count_i == count_max):
					RES_INDEX[k][INDEX].append([SS_K_I_copy[i][0], count_i, INDEX, i])
		INDEX += 1
		count_all += count_max
	return(res)

def Themore_1(k, res, temp_2):
	Type_I_state_vector_extend = Extend_Type_I(k, res)

	p = min(Type_I_state_vector_extend[1][0] - Type_I_state_vector_extend[0][0], Type_I_state_vector_extend[1][1], k - 1)
	q = min((k - 1) - p, Type_I_state_vector_extend[0][1], Type_I_state_vector_extend[1][1] - p)
	pp = Type_I_state_vector_extend[0][0] + 1 + p

	if (pp > temp_2[-1][0]):
		return ([pp, p + q])
	else:
		return ([temp_2[-1][0]+1, temp_2[-1][1]+1])

def Themore_2(k, res, temp_3):
	Type_I_state_vector_extend = Extend_Type_I(k, res)
	Type_I_state_vector_extend_r = Extend_Type_I(k, [len(res)])

	p = Type_I_state_vector_extend[0][0]
	for i in range (1, len(res)):
		p = min(p, Type_I_state_vector_extend[i][0])

	pp = Type_I_state_vector_extend_r[0][0] + p

	if (pp > temp_3[-1][0]):
		return ([pp, k-1])
	else:
		return ([temp_3[-1][0]+1, k-1])

def Derived_State_Vector(res, SS_K_I):
	SS_K_I_TEMP = []
	SS_K_I_TEMP_copy = []

	if (len(res) == 2):
		k = 1
		x = 0
		temp_2 = [[0, 0]]
		while ((x + 1) < K):
			temp_2.append(Themore_1(k, res, temp_2))
			x = temp_2[-1][0]
			k = k + 1
		SS_K_I_TEMP.append(temp_2)
		SS_K_I_TEMP_copy.append([res, temp_2])

	if (len(res) > 2):
		k = 1
		x = 0
		temp_3 = [[0, 0]]
		while ((x + 1) < K):
			temp_3.append(Themore_2(k, res, temp_3))
			x = temp_3[-1][0]
			k = k + 1
		SS_K_I_TEMP.append(temp_3)
		SS_K_I_TEMP_copy.append([res, temp_3])

	SS_K_I.append(Find_Type_I_MODE_1(SS_K_I_TEMP))
	SS_K_I_copy.append([res, SS_K_I[-1]])
	
def Loop_Function(SS_K_I, R, res, a, b):
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
				Derived_State_Vector(res_temp, SS_K_I)
	else:
		for i in range (b, K+1-R):
			res[R - a] = i
			Loop_Function(SS_K_I, R, res, a - 1, i)

if __name__ == '__main__':
	Type_I_state_vector = [
	[[0, 0]], # The Type_I_state_vector of 0-XOR algorithm
	[[0, 0]], # The Type_I_state_vector of 1-XOR algorithm
	[[0, 0], [1, 0]], # The Type_I_state_vector of 2-XOR algorithm
	]

	default_k = 7
	default_Model = 1

	print("#######################################################################################")
	Model = int(input("Please select a model:\n"
			   "Enter 1 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula.\n"
			   "Enter 2 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula and the corresponding decomposition of k.\n"
			   "Enter 3 to obtain the state vector of the k-XOR algorithm with the optimal TMTO formula and the corresponding decomposition of k. Additionally, the state vector of the k-XOR algorithm can be derived for any given decomposition of k.\n"
			   "Pressing Enter directly will use the default parameter 'Model = 1'.\n"
			   "Enter your choice (1 - 3): ") or default_Model)
	print("\n")

	if Model == 1:
		print("You selected Model 1: Design the k-XOR algorithm with an optimal TMTO formula.")
	elif Model == 2:
		print("You selected Model 2: Design the k-XOR algorithm with an optimal TMTO formula and obtain the decomposition of k.")
	elif Model == 3:
		print("You selected Model 3: Design the k-XOR algorithm with an optimal TMTO formula and obtain the decomposition of k. You can also obtain the state vector of the k-XOR algorithm corresponding to any decomposition of k.")
	else:
		print("Invalid input. Please enter 1 - 3.\n")
		exit()
	print("\n")

	print("#######################################################################################")
	kk = int(input("Please enter the parameter k (k >= 3) of the k-XOR algorithm to be designed:\n"
			"If you choose Model 1, you can obtain results in just a few minutes for k not exceeding 30.\n"
			"If you choose Model 2, you can obtain results in just a few minutes for k not exceeding 29.\n"
			"If you choose Model 3, you can obtain results in just a few minutes for k not exceeding 27.\n"
			"Pressing Enter directly will use the default parameter 'k = 7'.") or default_k)
	print("\n")
	print("You have entered k as %d. We will provide the state of the optimal %d-XOR algorithm with the TMTO formula." %(kk, kk))
	print("\n")

	for K in range (3, kk + 1):
		SS_K_I = []
		SS_K_I_copy = []

		if (Model <= 2):
			if (K == 3):
				Starting_point = 1
			elif (K > 3) and (K <= 7):
				Starting_point = 2
			else:
				Starting_point = 4
		else:
			if (K == 3):
				Starting_point = 1
			else:
				Starting_point = 1
		
		for r in range (1, K-1):
			RES_INDEX = [[] for i in range (kk+1)]
			res = [0 for i in range (r)]
			Loop_Function(SS_K_I, r, res, r, Starting_point)

		if (Model == 1):
			Type_I_state_vector.append(Find_Type_I_MODE_1(SS_K_I))
		else:
			Type_I_state_vector.append(Find_Type_I_MODE_2(SS_K_I, SS_K_I_copy, RES_INDEX, kk))

	Type_I_state_vector_k = []
	for i in range (1, len(Type_I_state_vector[-1])):
		Type_I_state_vector_k.append([Type_I_state_vector[-1][i][0]-Type_I_state_vector[-1][i][1], Type_I_state_vector[-1][i][1], 1])

	print("#######################################################################################")
	print("The state of the %d-XOR algorithm with the optimal TMTO formula is:\n" % kk, Type_I_state_vector_k)
	print("\n")

	if (Model >= 2):
		print("The decomposition of k corresponding to the k-XOR algorithm with the optimal TMTO formula is as follows.\n"
			"If multiple decompositions are available, any one of them can be selected.\n")

		for i in range (len(RES_INDEX[kk])):
			A = RES_INDEX[kk][len(RES_INDEX[kk])-1][0][2]
			B = [1, min(RES_INDEX[kk][len(RES_INDEX[kk])-1][0][1], len(Type_I_state_vector[-1])-1)]
			B_copy = B.copy()
			if (i == 0):
				print("\n################################### M^%d <= T <= M^%d ###################################\n"% (B[0], min(B[1], len(Type_I_state_vector[-1])-1) ))
			for j in range (len(RES_INDEX[kk][len(RES_INDEX[kk])-1-i])):
				if (RES_INDEX[kk][len(RES_INDEX[kk])-1-i][j][2] == A):
					pass
				else:
					A = RES_INDEX[kk][len(RES_INDEX[kk])-1-i][j][2]
					B = [B_copy[1], min(RES_INDEX[kk][len(RES_INDEX[kk])-1-i][j][1]+B_copy[1], len(Type_I_state_vector[-1])-1)]
					print("\n################################### M^%d <= T <= M^%d ###################################\n"% (B[0], min(B[1], len(Type_I_state_vector[-1])-1) ))
				
				if ((K > 3) and (RES_INDEX[kk][len(RES_INDEX[kk])-1-i][j][0][0] == 1)):
					pass
				else:

					if (SS_K_I_copy[RES_INDEX[kk][len(RES_INDEX[kk])-1-i][j][3]][1][min(B[1], len(Type_I_state_vector[-1])-1)][0] == Type_I_state_vector[-1][min(B[1], len(Type_I_state_vector[-1])-1)][0]):
						print("When M^%d <= T <= M^%d, the decomposition of %d can be: %d = " % (B[0], B[1], kk, kk), " + ".join(map(str, RES_INDEX[kk][len(RES_INDEX[kk])-1-i][j][0])))
					else:
						pass
		print("\nPlease derive the TMTO formula for the %d-XOR algorithm based on the definition of the state of the k-XOR algorithm presented in the manuscript.\n" % kk)

	if (Model == 3):
		print("#######################################################################################\n")
		print("If you want to print the state corresponding to any decomposition of %d.\n" % kk)
		user_input = input("Please enter multiple numbers separated by spaces (press Enter to exit).\n"
			"Please enter numbers k_i from smallest to largest (e.g., 4 4 6 9).\n").strip()

		if not user_input:
		    print("No input provided. Exiting...")
		    exit()

		Decomposition = [int(num) for num in user_input.split()]
		if (len(Decomposition) == 1):
			print("Invalid decomposition. Exiting...")
			exit()

		if (sum(Decomposition) != kk):
			print("%d is not equal to " % kk, " + ".join(map(str, Decomposition)), "...\n")
			exit()

		print("The state vector corresponding to decomposition %d = " % kk, " + ".join(map(str, Decomposition)), "is:\n")

		Type_I_state_vector_copy_k = []
		for i in range (len(SS_K_I_copy)):
			if (SS_K_I_copy[i][0] == Decomposition):
				for j in range (1, len(SS_K_I_copy[i][1])):
					Type_I_state_vector_copy_k.append([SS_K_I_copy[i][1][j][0]-SS_K_I_copy[i][1][j][1], SS_K_I_copy[i][1][j][1], 1])
				print(Type_I_state_vector_copy_k)
		exit()
	else:
		exit()

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