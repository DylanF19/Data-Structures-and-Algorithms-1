"""Event_Planner.py"""
import itertools

#Brute Force
def best_combo_for_highest_fun_score_brute_force(event_list, max_time, max_budget):
    """
    Docstring for best_combo_for_highest_fun_score
    
    :param Event_List: A brute force approach to finding the best combo of events
    """

    event_combo_list = []
    highest_enjoyment = 0

    for l in range(1, len(event_list) + 1):
        for subset in itertools.combinations(event_list, l):
            event_combo_list += [subset]

    for i in event_combo_list.copy():
        time_cost = 0
        money_cost = 0
        for j in i:
            time_cost += j[1]
            money_cost += j[2]
        if time_cost > max_time or money_cost > max_budget:
            event_combo_list.remove(i)

    for i in event_combo_list:
        enjoyment_sum = 0
        for j in i:
            enjoyment_sum += j[3]
        if enjoyment_sum > highest_enjoyment:
            best_combo = [i]
            highest_enjoyment = enjoyment_sum
        if enjoyment_sum == highest_enjoyment:
            best_combo += [i]
        else:
            continue

    return best_combo, highest_enjoyment

#Name, Time, Cost, Fun_Value
Event_List = {
    ("Welcome-BBQ", 3, 50, 80),
    ("Karaoke-Night", 2, 40, 70),
    ("Film-Screening", 3, 30, 90),
    ("Sports-Tournament", 4, 60, 110),
    ("Art-Workshop", 2, 70, 95),
    ("Pub-Quiz", 2, 25, 60),
    ("Bowling", 3, 80, 100),
    ("Laser-Tag", 2, 90, 130),
    ("Cooking-Class", 3, 75, 105),
    ("Beach-Trip", 6, 120, 180),
    ("Escape-Room", 2, 85, 115),
    ("Open-Mic", 2, 20, 50)
}

print(best_combo_for_highest_fun_score_brute_force(Event_List, 15, 300))
