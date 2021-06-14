name = input()
points = float(input())
jury_count = int(input())
final_points = points
point_from_jury = 0
for i in range(1, jury_count + 1):
    jury_name = input()
    points_jury = float(input())
    point_from_jury = (len(jury_name) * points_jury) / 2
    final_points += point_from_jury
    if final_points > 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {final_points:.1f}!")
        break
if final_points <= 1250.5:
    print(f"Sorry, {name} you need {1250.5 - final_points:.1f} more!")

