airline_name = input()
adult_tickets_count = int(input())
children_tickets_count = int(input())
adult_ticket_price = float(input())
service_fee = float(input())
adult_tickets_total = adult_ticket_price * adult_tickets_count + adult_tickets_count * service_fee
children_tickets_total = children_tickets_count * (adult_ticket_price - (adult_ticket_price * 0.70)) + children_tickets_count * service_fee
income_total = adult_tickets_total + children_tickets_total
print(f"The profit of your agency from {airline_name} tickets is {income_total * 0.20:.2f} lv.")