age= float(input('What is your age?'))

days_remaining = (90-age)*365
weeks_reamining = (90-age)*52
months_remining = (90-age)*12
message = f"You have {days_remaining} days, {weeks_reamining} weeks, {months_remining} months left"
print(message)
