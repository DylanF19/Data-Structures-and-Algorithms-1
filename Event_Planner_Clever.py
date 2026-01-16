import numpy
import copy

#Name, Time, Cost, Fun_Value
Event_List_2 = [
    [[1],["Welcome-BBQ"],[3, 50, 80]],
    [[2],["Karaoke-Night"],[2, 40, 70]],
    [[3],["Film-Screening"],[3, 30, 90]],
    [[4],["Sports-Tournament"],[4, 60, 110]],
    [[5],["Art-Workshop"],[2, 70, 95]],
    [[6],["Pub-Quiz"],[2, 25, 60]],
    [[7],["Bowling"],[3, 80, 100]],
    [[8],["Laser-Tag"],[2, 90, 130]],
    [[9],["Cooking-Class"],[3, 75, 105]],
    [[10],["Beach-Trip"],[6, 120, 180]],
    [[11],["Escape-Room"],[2, 85, 115]],
    [[12],["Open-Mic"],[2, 20, 50]]
]

#Name, Time, Cost, Fun_Value
Event_List_3 = [
    [[1],["Orientation-Walk"],[1, 10, 30]],  
    [[2],["Ice-Breaker-Games"],[2, 20, 50]],
    [[3],["Movie-Marathon"],[5, 60, 140]],
    [[4],["City-Tour"],[4, 80, 120]],
    [[5],["Charity-Run"],[3, 15, 70]],
    [[6],["Trivia-Night"],[2, 30, 65]],
    [[7],["Wine-Tasting"],[2, 100, 150]],
    [[8],["Rock-Climbing"],[4, 110, 160]],
    [[9],["Theatre-Trip"],[4, 90, 130]],
    [[10],["Pottery-Class"],[3, 85, 125]],
    [[11],["Campus-Scavenger-Hunt"],[3, 25, 75]],
    [[12],["Photography-Walk"],[3, 40, 85]],
    [[13],["Poetry-Slam"],[2, 20, 55]],
    [[14],["Dance-Workshop"],[2, 50, 90]],
    [[15],["Baking-Competition"],[3, 55, 95]],
    [[16],["Outdoor-Cinema"],[4, 70, 115]],
    [[17],["Kayaking"],[5, 130, 190]],
    [[18],["Board-Game-Cafe"],[3, 45, 80]],
    [[19],["Comedy-Show"],[3, 80, 135]],
    [[20],["Volunteering-Event"],[4, 10, 60]],
    [[21],["Yoga-Session"],[2, 35, 70]],
    [[22],["Park-Picnic"],[3, 30, 65]],
    [[23],["Museum-Evening"],[3, 75, 110]],
    [[24],["Stargazing-Trip"],[4, 50, 100]],
    [[25],["Crafts-Fair"],[2, 40, 75]]
]


def sumofTwoArrays(arr_1, arr_2):
    return numpy.add(arr_1, arr_2).tolist()


def differenceofTwoArrays(arr_1, arr_2):
    return numpy.subtract(arr_1, arr_2).tolist()


def goDownALevel(node, event_list, node_index):
    branch = event_list[node_index-1]
    temp_event_index = node[0]+branch[0]
    temp_event_list = node[1]+branch[1]
    temp_event_sum = sumofTwoArrays(node[2],branch[2])
    product_set = [temp_event_index,temp_event_list,temp_event_sum]
    return product_set


def goUpALevel(node, event_list):
    temp_event_index = node[0]
    temp_event_list = node[1]
    branch_inverse = event_list[temp_event_index[-1]-1]
    temp_event_list.pop(-1) # Remove last value
    temp_event_index.pop(-1)
    temp_event_sum = differenceofTwoArrays(node[2],branch_inverse[2])
    product_set = [temp_event_index,temp_event_list,temp_event_sum]
    return product_set


def isValid(node, max_time, max_budget):
    if node[2][0] <= max_time and node[2][1] <= max_budget:
        return True
    return False


def isUnderBudget(node, max_time, max_budget):
    if node[2][0] < max_time and node[2][1] < max_budget:
        return True
    return False


def doesEndWithLastEvent(node, event_list):
    last_event = event_list[-1][0][0]
    node_end = node[0][-1]
    if node_end == last_event:
        return True
    return False


def isLengthOne(Node):
    if len(Node[0]) <= 1:
        return True
    return False


def Event_Planner_Itterative_Tree_Search(event_list, max_time, max_budget):

    print("==================Start====================")

    Legal_Event_Combinations = []
    Node = [[],[],[0,0,0]]
    Legal_Event_Combinations += [Node]
    Node_index = 1
    solutionsFound = False

    while solutionsFound is False:
        Node = goDownALevel(Node, event_list, Node_index)
        Valid = isValid(Node, max_time, max_budget)
        underBudget = isUnderBudget(Node, max_time, max_budget)
        endsWithLastEvent = doesEndWithLastEvent(Node, event_list)
        lengthIsOne = isLengthOne(Node)


        if Valid:
            Legal_Event_Combinations.append(copy.deepcopy(Node))
            if not endsWithLastEvent:
                Node_index = Node[0][-1]+1
                if not underBudget:
                    Node = goUpALevel(Node, event_list)

        elif not endsWithLastEvent:
            Node_index = Node[0][-1]+1
            Node = goUpALevel(Node, event_list)

        if endsWithLastEvent:
            if not lengthIsOne:
                Node = goUpALevel(Node, event_list)
                Node_index = Node[0][-1]+1
                Node = goUpALevel(Node, event_list)
            else: # if lengthIsOne is True {and endsWithLastEvent is True}
                solutionsFound = True
        # To fail: must be not Valid, end with last event and not end with last event

    best_combo = []
    j = None
    for i in sorted(Legal_Event_Combinations, key=lambda x: x[2][2], reverse=True):
        if i[2][2] == j or j == None:
            best_combo += [i]
            j = i[2][2]
        else:
            break
    print("==================End====================")
    return best_combo

print(Event_Planner_Itterative_Tree_Search(Event_List_3, 20, 500))