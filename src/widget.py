from src import masks


def mask_account_card(account_card: str) -> str:
    """Функция маскировки номера карты/счёта"""

    # Если первые пять символов - "Счет" -> на входе номер счёта, применяем функцию маскировки номера счёта
    if account_card[0:4] == "Счет":
        account_id = "Счет " + masks.get_mask_account(account_card[-20:])
        return account_id

    # Если первые пять символов - не "Счет" -> на входе номер карты, применяем функцию маскировки номера счёта
    else:
        card_id = account_card[0:-16] + masks.get_mask_card_number(account_card[-16:])
        return card_id


def transaction_date(transaction_id: str) -> str:
    """функция определения даты транзакции"""
    return transaction_id[8:10] + "." + transaction_id[5:7] + "." + transaction_id[0:4]
