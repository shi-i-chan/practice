def move_zeros(lst):
	new_lst = [value for value in lst if value != 0]
	zero_lst = [0 for value in lst if value == 0]
	return new_lst + zero_lst
