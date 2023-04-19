account = int(input('Put numbers of account: '))
interest_rate = float(input('Put % of interest rate: '))
years = int(input('Put number of years: '))

print(f'Initial amount: {account}')

counter = 1
while counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f'year {counter}: {account}')
    counter += 1

