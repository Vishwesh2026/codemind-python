N = int(input())
array = list(map(int, input().split()))
average = sum(array) / N
decimal_places = 2
formatted_average = "{:.{}f}".format(average, decimal_places)
print(formatted_average)