def loading_bar(number):
    loading = ["."] * 10
    for i in range(number):
        loading[i] = "%"
    if number < 10:
        print(f"{number * 10}% [{''.join(loading)}]")
        print("Still loading...")
    else:
        print(f"100% Complete!")
        print(f"[{''.join(loading)}]")
loading_bar(int(input())//10)