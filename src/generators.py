def card_number_generator(start_index: int, stop_index: int):
    while start_index <= stop_index:
        free_digits = 16 - len(str(start_index))
        new_card_number = ''
        for i in range(free_digits):
            new_card_number += '0'
        new_card_number += str(start_index)
        new_card_number = (new_card_number[0:4] + ' ' + new_card_number[4:8] + ' ' +
                           new_card_number[8:12] + ' ' + new_card_number[12:])
        start_index += 1
        yield new_card_number


def filter_by_currency(transactions: list[dict], currency: str):
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction
