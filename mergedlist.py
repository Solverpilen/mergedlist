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

list1= [3213,132,2,1,2]
list2=[18,123,43,123,32]
print(merge_lists(list1,list2))
