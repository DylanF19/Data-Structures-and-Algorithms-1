"""Dynamic Event Planner"""
#=====Imports=====
import time
try:
    from Utilities import function_port_money_only, array_to_readable_output_money_only
except ImportError:
    from Code.Utilities import function_port_money_only, array_to_readable_output_money_only
#======Code=======
def event_planner_dynamic_search_money_only(file_name=None, input_details=None, quiet=False):
    """
    This is the main engine of the dynamic approach. It takes the lists of events
    and parameters and prints the solution. Note: does not return a result, printing
    directly to the command line.
    
    :param file_name: The desired input file
    :param input_details: An array of details that can be 
                          used to overwrite the pre-existing
                          file values. Usefull for debugging
    :param quiet: Controls the verbosity of the function
                  (whether it outputs details regarding 
                  the solution or not)
    """

    # Starts performance counter, a highly accurate timer.
    start = time.perf_counter()
    # Gets the starting conditions and event set
    n, max_budget, event_list, name_list = function_port_money_only(file_name, input_details)
    # Creates the nunber_of_events(n) by max_time(t) by max_budget(b) 3D grid filled with 0s.
    data_field_2d = [[0 for _ in range(max_budget + 1)] for _ in range(n+1)]

    for i in range(n+1):
        #print(i)
        for m in range(max_budget+1):
            # itterates through ever cell in the 3D grid
            if i == 0 or m == 0:
            # if i or m is zero, no enjoyment could ever be gained
            # so such cells are set to 0(no enjoyment)
                data_field_2d[i][m] = 0

            elif event_list[i-1][1] <= m:
                # if the considered event can fit in the cell's constraints,
                # set the cell to the cell above the current cell or the sum
                # of the considered event and the cell above that fits the event,
                # which ever is greater.
                data_field_2d[i][m] = max(
                    data_field_2d[i-1][m],
                    event_list[i-1][2] + data_field_2d[i-1][m-event_list[i-1][1]]
                        )
                # essentially gets the greatest enjoyment a cell can be with a
                # given max time, max budget and event list.
            else:
            # else, set the cell to the value of the cell above
                data_field_2d[i][m] = data_field_2d[i-1][m]

    # From the 2D grid, we can derive what the greatest enjoyment can be by
    # reading the value in the bottom corner where the solution limits are.
    # From this enjoyment value, we can work backwards to deduce the sequence
    # could've made it.
    # Note, there could be multiple solutions but only one will be given.
    i = n
    k = max_budget
    solution = [[0,0,0]]
    while i > 0 and k > 0:
        if data_field_2d[i][k] != data_field_2d[i-1][k]:
            # checks the value of the cell i and compares it to the cell above it.
            # The cell i shows the enjoyment value considering the first i events
            # The cell i-1 shows the enjoyment value considering the first i-1 events
            # If they have the same value, it means that they have the same set of events so,
            # since event i couldn't have been included in cell i-1, then event i cant be in cell i either.
            # Otherwise, it counts event i as part of the solution.
            solution += [event_list[i-1]]
            k = k - event_list[i-1][1]
            # The loop then repeats, reducing the number of considered events from the first i events to the 
            # first i-1 events, selecting a new cell in the board. 
            # This new cell will have a new max budget equaling the old max budget minus the 
            # cost of the removed event ONLY IF the event was a part of the solution.
        i -= 1
        # The loop fully concludes once it runs out of events of the max budget reaches 0
        # suggesting that the solution list uses up all of the budget.
        # At that point, the list is returned, except if no event could fit within the constraints
        # In which case, the placeholder value of event 0 (signifying no event) is used.

    # since the derived solution is in reverse order, this put's it back in forward order
    solution_sorted = sorted(solution, key=lambda x: x[0])
    # this converts the solution from arrays of numbers to a list of events and key information
    best_combo, details = array_to_readable_output_money_only(solution_sorted, name_list)

    end = time.perf_counter()
    #===============result================
    # Finally, the results of the solution finder are printed.
    if quiet == False:
        print(" =========Dynamic========= \n")
        print(f"Input: {file_name}")
        print("\n ---------Solution-------- \n")
        for i in best_combo:
            print(f" - {i}")
        print("\n ----------Stats---------- \n")
        print(f"Money used:      {details[1]} Pounds")
        print(f"Total enjoyment: {details[2]} Enjoyment")
        print(f"Time to Compute: {end-start} Seconds")
        print("\n ======================== \n")


