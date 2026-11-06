"""
Problem:Three friends each pay 10 for a movie ticket and for snacks.calculate their total.
Decomposition:
number_of_friends(int), ticket_cost(float),snack_cost(float)
"""

number_of_friends = 3
ticket_cost  = 10.0
snack_cost= 5.0
total_cost =(ticket_cost + snack_cost)* number_of_friends
print(total_cost)
#print data type
print(type(number_of_friends))
print(type(ticket_cost))
print(type(snack_cost))
print(type(total_cost))