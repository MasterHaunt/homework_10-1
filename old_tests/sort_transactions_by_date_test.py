from src import processing

example_transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sorted_downwards_transactions = processing.sort_by_date(example_transactions)

print("order = True -> from first to last:")
print(sorted_downwards_transactions)

sorted_upwards_transactions = processing.sort_by_date(example_transactions, descending=False)

print("\norder = False -> from last to first:")
print(sorted_upwards_transactions)
