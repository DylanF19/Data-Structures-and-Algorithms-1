
import copy
import numpy

def sum_of_two_arrays(arr_1, arr_2):
    return numpy.add(arr_1, arr_2).tolist()


def difference_of_two_arrays(arr_1, arr_2):
    return numpy.subtract(arr_1, arr_2).tolist()


def go_down_a_level(node, event_list, node_index):
    branch = event_list[node_index-1]
    temp_event_index = node[0]+branch[0]
    temp_event_list = node[1]+branch[1]
    temp_event_sum = sum_of_two_arrays(node[2],branch[2])
    product_set = [temp_event_index,temp_event_list,temp_event_sum]
    return product_set


def go_up_a_level(node, event_list):
    temp_event_index = node[0]
    temp_event_list = node[1]
    branch_inverse = event_list[temp_event_index[-1]-1]
    temp_event_list.pop(-1) # Remove last value
    temp_event_index.pop(-1)
    temp_event_sum = difference_of_two_arrays(node[2],branch_inverse[2])
    product_set = [temp_event_index,temp_event_list,temp_event_sum]
    return product_set


def is_valid(node, max_time, max_budget):
    if node[2][0] <= max_time and node[2][1] <= max_budget:
        return True
    return False


def is_under_budget(node, max_time, max_budget):
    if node[2][0] < max_time and node[2][1] < max_budget:
        return True
    return False


def does_end_with_last_event(node, event_list):
    last_event = event_list[-1][0][0]
    node_end = node[0][-1]
    if node_end == last_event:
        return True
    return False


def is_length_one(Node):
    if len(Node[0]) <= 1:
        return True
    return False


def event_planner_itterative_search(file_name=None, input_details=None):

    #print("==================Start====================")
    if not file_name is None:
        max_time, max_budget, event_list = text_document_to_internal_array_translator(str(file_name))
    elif len(input_details) == 3:
        max_time, max_budget, event_list = input_details
    else:
        raise NameError("InputError: input details cannot be read")
    #print("Max Time: ",max_time)
    #print("Man Budget: ",max_budget)
    #print("Size of Event Pool: ",len(event_list))

    legal_event_combinations = []
    node = [[],[],[0,0,0]]
    legal_event_combinations += [node]
    node_index = 1
    all_solutions_found = False

    while all_solutions_found is False:
        node = go_down_a_level(node, event_list, node_index)
        valid = is_valid(node, max_time, max_budget)
        under_budget = is_under_budget(node, max_time, max_budget)
        ends_with_last_event = does_end_with_last_event(node, event_list)
        length_is_one = is_length_one(node)


        if valid:
            legal_event_combinations.append(copy.deepcopy(node))
            if not ends_with_last_event:
                node_index = node[0][-1]+1
                if not under_budget:
                    node = go_up_a_level(node, event_list)

        elif not ends_with_last_event:
            node_index = node[0][-1]+1
            node = go_up_a_level(node, event_list)

        if ends_with_last_event:
            if not length_is_one:
                node = go_up_a_level(node, event_list)
                node_index = node[0][-1]+1
                node = go_up_a_level(node, event_list)
            else: # if lengthIsOne is True {and endsWithLastEvent is True}
                all_solutions_found = True
        # To fail: must be not Valid, end with last event and not end with last event

    #print("Length of solution list: ",len(legal_event_combinations))


    best_combo = []
    j = None
    for i in sorted(legal_event_combinations, key=lambda x: x[2][2], reverse=True):
        if i[2][2] == j or j is None:
            best_combo += [i]
            j = i[2][2]
        else:
            break
    #print("===================End=====================")
    return best_combo

def text_document_to_internal_array_translator(file_name):

    import os
    file_path = os.path.join(r"Input_Files",file_name)
    #print(f" :- File path: {file_path}")
    try:
        if os.path.exists(file_path):

            os.chmod(file_path, 0o666)
            #print(" :- File permissions modified successfully!")
            pass
        else:
            #print(" !! File not found:", file_path)
            pass
    except PermissionError:
        print(" !! Permission denied: You don't have the necessary permissions to change the permissions of this file.")

    with open(file_path, "r", encoding="utf-8") as file:
        event_index = int(file.readline())
        time_limit, money_limit = ((file.readline().strip("\n")).split(" "))
        time_limit = int(time_limit)
        money_limit = int(money_limit)
        ID_index = 1
        event_list_translated = []
        for x in file:
            event_name, time_value, money_value, enjoyment_value = x.strip("\n").split(" ")
            event_list_translated += [[[ID_index],[event_name],[int(time_value), int(money_value), int(enjoyment_value)]]]
            ID_index += 1

    #print(" :- File content accessed successfully!")

    return time_limit, money_limit, event_list_translated
