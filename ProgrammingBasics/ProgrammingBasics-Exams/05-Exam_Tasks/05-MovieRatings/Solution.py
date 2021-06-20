import sys
movies_count = int(input())
max_rating = -sys.maxsize
max_movie = ""
min_rating = sys.maxsize
min_movie = ""
all_ratings = 0
for i in range(movies_count):
    movie_name = input()
    movie_rating = float(input())
    all_ratings += movie_rating
    if movie_rating > max_rating:
        max_rating = movie_rating
        max_movie = movie_name
    if movie_rating < min_rating:
        min_rating = movie_rating
        min_movie = movie_name
    all_ratings += movie_rating
print(f"{max_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {(all_ratings / (movies_count * 2)):.1f}")
