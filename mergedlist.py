def merge_lists(my_list, alices_list):
           # set up our merged_list
           merged_list_size = len(my_list) + len(alices_list)
           merged_list = [0] * merged_list_size

           current_index_alices = 0
           current_index_mine = 0
           current_index_merged = 0

           while current_index_merged < merged_list_size:
                    is_my_list_exhausted = current_index_mine >= len(my_list)
                    is_alices_list_exhausted = current_index_alices >= len(alices_list)

                    if not is_my_list_exhausted:
                            merged_list[current_index_merged] = my_list[current_index_mine]
                            current_index_merged += 1
                            current_index_mine += 1

                    # case: next comes from Alice's list
                    else:
                            merged_list[current_index_merged] = alices_list[current_index_alices]
                            current_index_merged += 1
                            current_index_alices += 1



           return merged_list

print("Test Case 1:")
list1= [6,4,1]
list2=[14,5,10,2,20]

print("List 1: ")
print(list1)
print("List 2: ")
print(list2)
print("\n")
print("merged lists: ")
print(merge_lists(list1,list2))

print("\n")


print("Test Case 2:")
list1= [15,11]
list2=[10,14,7,3,6,12,18,19,4]

print("List 1: ")
print(list1)
print("List 2: ")
print(list2)
print("\n")
print("merged lists: ")
print(merge_lists(list1,list2))

print("\n")


print("Test Case 3:")
list1= [12,20,11,6,15,1,10,7,2,13]
list2=[14]

print("List 1: ")
print(list1)
print("List 2: ")
print(list2)
print("\n")
print("merged lists: ")
print(merge_lists(list1,list2))

print("\n")

print("Test Case 4:")
list1= [17,20,9,6,14,7]
list2=[18,5,15,8]

print("List 1: ")
print(list1)
print("List 2: ")
print(list2)
print("\n")
print("merged lists: ")
print(merge_lists(list1,list2))

print("\n")

print("Test Case 5:")
list1= [2,14,10,15,18,20,8,9]
list2=[3,17,4,13,19,12,6]

print("List 1: ")
print(list1)
print("List 2: ")
print(list2)
print("merged lists: ")
print(merge_lists(list1,list2))
