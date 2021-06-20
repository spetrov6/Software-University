movie_name = input()
standard = 0
student = 0
kid = 0
ticket_count = 0
total_tickets = 0
while movie_name != "Finish":
    spaces = int(input())
    for i in range(spaces):
        ticket = input()
        if ticket == "End":
            break
        elif ticket == "standard":
            standard += 1
        elif ticket == "student":
            student += 1
        elif ticket == "kid":
            kid += 1
        ticket_count += 1
    print(f"{movie_name} - {(ticket_count / spaces) * 100:.2f}% full.")
    total_tickets += ticket_count
    ticket_count = 0
    movie_name = input()
print(f"Total tickets: {total_tickets}")
print(f"{(student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid / total_tickets) * 100:.2f}% kids tickets.")
