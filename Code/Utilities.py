"""
    Common utility functions used in both brute force and dynamic algorithms
"""
import os
import numpy as np

def function_port_money_only(file_name=None, input_details=None):
    """
    This is utility function, used to set the initial conditions of the the main function
    
    :param file_name: The desired input file
    :param input_details: An array of details that can be 
                          used to overwrite the pre-existing
                          file values. Usefull for debugging
    """
    # Default values set for  the sake of redundancy
    event_list = None
    name_list = None
    max_budget = 0

    # a tree of conditionals to set the starting conditions, allowing for some
    # customisability, useful for testing and debugging.
    #
    # if a given parameter is set to something other than None, it overwrites the initial state
    if file_name is not None:
        max_budget, event_list, name_list = text_document_to_internal_array_translator_money_only(str(file_name))
    if input_details is not None and len(input_details) == 3:
        if input_details[0] is not None:
            max_budget = input_details[0]
        if input_details[1] is not None:
            event_list = input_details[1]
    if file_name is None and input_details is None:
        raise NameError("Input cannot be interprteted")
    if event_list is None and file_name is None:
        raise NameError("Input cannot be interprteted")
    n = len(event_list)
    return n, max_budget, event_list, name_list

def function_port(file_name=None, input_details=None):
    """
    This is utility function, used to set the initial conditions of the the main function
    
    :param file_name: The desired input file
    :param input_details: An array of details that can be 
                          used to overwrite the pre-existing
                          file values. Usefull for debugging
    """
    # Default values set for  the sake of redundancy
    event_list = None
    name_list = None
    max_time = 0
    max_budget = 0

    # a tree of conditionals to set the starting conditions, allowing for some
    # customisability, useful for testing and debugging.
    #
    # if a given parameter is set to something other than None, it overwrites the initial state
    if file_name is not None:
        max_time, max_budget, event_list, name_list = text_document_to_internal_array_translator(str(file_name))
    if input_details is not None and len(input_details) == 3:
        if input_details[0] is not None:
            max_time = input_details[0]
        if input_details[1] is not None:
            max_budget = input_details[1]
        if input_details[2] is not None:
            event_list = input_details[2]
    if file_name is None and input_details is None:
        raise NameError("Input cannot be interprteted")
    if event_list is None and file_name is None:
        raise NameError("Input cannot be interprteted")
    n = len(event_list)
    return n, max_time, max_budget, event_list, name_list

def text_document_to_internal_array_translator_money_only(file_name):
    """
    This finds the text file, reads it and converts the contents of that
    file into it's key data and arrays.
    
    :param file_name: The desired input file
    """
    file_path = os.path.join(r"Input_Files",file_name)
    #print(f" :- File path: {file_path}")
    try:
        if os.path.exists(file_path):

            os.chmod(file_path, 0o666)
            #print(" :- File permissions modified successfully!")
        else:
            print(" !! File not found:", file_path)
    except PermissionError:
        print(" !! Permission denied: You don't have the necessary permissions to change the permissions of this file.")

    with open(file_path, "r", encoding="utf-8") as file:
        _ = int(file.readline())
        time_limit, money_limit = ((file.readline().strip("\n")).split(" "))
        _ = int(time_limit)
        money_limit = int(money_limit)
        id_index = 1
        event_list_translated = []
        name_list= []
        for x in file:
            event_name, _, money_value, enjoyment_value = x.strip("\n").split(" ")
            event_list_translated += [[id_index, int(money_value), int(enjoyment_value)]]
            name_list += [event_name]
            id_index += 1
        name_list += ["No Event"]

    #print(" :- File content accessed successfully!")

    return money_limit, event_list_translated, name_list


def text_document_to_internal_array_translator(file_name):
    """
    This finds the text file, reads it and converts the contents of that
    file into it's key data and arrays.
    
    :param file_name: The desired input file
    """
    file_path = os.path.join(r"Input_Files",file_name)
    #print(f" :- File path: {file_path}")
    try:
        if os.path.exists(file_path):

            os.chmod(file_path, 0o666)
            #print(" :- File permissions modified successfully!")
        else:
            print(" !! File not found:", file_path)
    except PermissionError:
        print(" !! Permission denied: You don't have the necessary permissions to change the permissions of this file.")

    with open(file_path, "r", encoding="utf-8") as file:
        event_index = int(file.readline())
        time_limit, money_limit = ((file.readline().strip("\n")).split(" "))
        time_limit = int(time_limit)
        money_limit = int(money_limit)
        id_index = 1
        event_list_translated = []
        name_list= []
        for x in file:
            event_name, time_value, money_value, enjoyment_value = x.strip("\n").split(" ")
            event_list_translated += [[id_index, int(time_value), int(money_value), int(enjoyment_value)]]
            name_list += [event_name]
            id_index += 1
        name_list += ["No Event"]

    #print(" :- File content accessed successfully!")

    return time_limit, money_limit, event_list_translated, name_list

def array_to_readable_output(array, name_list):
    """
    Converts the internal solution array into a form that can be
    reduced to the names of the events ad its details.
    
    :param array: internal array(only consists of numbers)
    :param name_list: the ordered list of event names for lookup
    """
    translated_list = []
    stats = [0,0,0]
    stats = np.sum(array, axis=0, dtype=int).tolist()
    for i in array:
        translated_list += [name_list[i[0]-1]]
    return translated_list, stats

def array_to_readable_output_money_only(array, name_list):
    """
    Converts the internal solution array into a form that can be
    reduced to the names of the events ad its details.
    
    :param array: internal array(only consists of numbers)
    :param name_list: the ordered list of event names for lookup
    """
    translated_list = []
    stats = [0,0]
    stats = np.sum(array, axis=0, dtype=int).tolist()
    for i in array:
        translated_list += [name_list[i[0]-1]]
    return translated_list, stats
