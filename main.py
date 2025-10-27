def calculate_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        return regular_pay + overtime_pay

# Worked 40 hours at $20 an hour
print(calculate_pay(40,20))
# Worked 50 hours at $20 an hour
print(calculate_pay(50,20))
# Worked 40 hours at $12 an hour
print(calculate_pay(40,12))
