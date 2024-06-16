from src import widget

test_number_1 = 'Счет 73654108430135874305'

print(widget.mask_account_card(test_number_1))

test_number_2 = 'Maestro 1596837868705199'

print(widget.mask_account_card(test_number_2))

test_number_3 = 'MasterCard 7158300734726758'

print(widget.mask_account_card(test_number_3))

test_number_4 = 'Visa Platinum 8990922113665229'

print(widget.mask_account_card(test_number_4))

transaction_1 = '2018-07-11T02:26:18.671407'

print(widget.transaction_date(transaction_1))

transaction_2 = '2024-06-12T15:10:18.582647'

print(widget.transaction_date(transaction_2))
