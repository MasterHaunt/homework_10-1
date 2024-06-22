from src import generators


def test_card_number_generator():
    card_numbers = generators.card_number_generator(100, 105)
    assert next(card_numbers) == "0000 0000 0000 0100"
    assert next(card_numbers) == "0000 0000 0000 0101"
    assert next(card_numbers) == "0000 0000 0000 0102"
    assert next(card_numbers) == "0000 0000 0000 0103"
    assert next(card_numbers) == "0000 0000 0000 0104"
    assert next(card_numbers) == "0000 0000 0000 0105"


def test_filter_by_currency(adv_transactions_list):
    rub_transactions = generators.filter_by_currency(adv_transactions_list, "RUB")
    assert next(rub_transactions)["id"] == 873106923
    assert next(rub_transactions)["id"] == 594226727
    usd_transactions = generators.filter_by_currency(adv_transactions_list, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941


def test_transaction_descriptions(adv_transactions_list):
    transactions_descriptions = generators.transaction_descriptions(adv_transactions_list)
    assert next(transactions_descriptions) == "Перевод организации"
    assert next(transactions_descriptions) == "Перевод со счета на счет"
    assert next(transactions_descriptions) == "Перевод со счета на счет"
    assert next(transactions_descriptions) == "Перевод с карты на карту"
    assert next(transactions_descriptions) == "Перевод организации"
