"""
Problem:Four Friends want to attend a concert in Lugogo.Each ticket costs 15 and they 
must pay an additional 12 for transport.calculate their total expenditure
Decoposition:
ticket_price (int), number_of_friends(int),transport_cost(int)
"""
ticket_price=15
number_of_friends=4
transport_cost=12
total_ticket_cost = ticket_price * number_of_friends
total_cost = total_ticket_cost + transport_cost
#were supposed to print all the data types
print(type(ticket_price))
print(type(number_of_friends))
print(type(transport_cost))
print(type(total_ticket_cost))
print(type(total_cost))