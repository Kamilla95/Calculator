def split_fare(fare, passengers, feature_cost):
    share = fare / passengers
    print(f'Splitting the ${fare_cost} fare between {passengers} passengers...')

    shared_cost = share + feature_cost
    print(f'Adding a ${feature_cost} feature cost...')

    return shared_cost

fare_cost = int(input('Type cost: '))
passengers = int(input('How many passengers? '))
feature_cost = float(input('Add feature cost: '))

shared_cost = split_fare(fare_cost, passengers, feature_cost)

print(f'Each pays: ${shared_cost}')


































