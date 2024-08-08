# cook your dish here
X, Y = map(int, input().strip().split())
time_for_first_Y_minutes = Y / 2
time_for_remaining_minutes = X - Y
total_time = time_for_first_Y_minutes + time_for_remaining_minutes
print(int(total_time))

