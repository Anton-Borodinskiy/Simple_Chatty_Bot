# put your python code here
duration_in_days = int(input(""))
food_cost = int(input(""))
one_way_flight = int(input(""))
one_night = int(input(""))

total_cost = one_way_flight*2 + one_night*(duration_in_days-1) + food_cost*duration_in_days
print(total_cost)