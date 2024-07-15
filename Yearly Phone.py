X = int(input().strip())
last_two_digits = X % 100
phone_model = f'K{last_two_digits:02d}'
print(phone_model)
