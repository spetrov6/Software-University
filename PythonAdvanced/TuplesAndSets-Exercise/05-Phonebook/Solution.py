ranges_count = int(input())
ranges = []
best_intersection = []
for _ in range(ranges_count):
    ranges.append(input().split("-"))
for line in ranges:
    first_range = [int(x) for x in line[0].split(",")]
    second_range = [int(x) for x in line[1].split(",")]
    intersection = set(range(first_range[0], first_range[1] + 1)).intersection(set(range(second_range[0], second_range[1] + 1)))
    if len(intersection) > len(best_intersection):
        best_intersection = intersection
print(f"Longest intersection is {list(best_intersection)} with length {len(best_intersection)}")