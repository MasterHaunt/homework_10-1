def filter_by_state(transactions: list, state: str = 'EXECUTED') -> list:
    '''Функция принимает на вход список словарей с информацией о транзакциях и возвращает список словарей с информацией
    о транзакциях, которые были исполнены ("state" = "EXECUTED"). Если помимо списка словарей в функцию передан второй
    параметр в значении "CANCELED" - возвращается список словарей с информацией об отменённых транзакциях'''

    filtered_transactions = []
    for transaction in transactions:
        if transaction['state'] == state:
            filtered_transactions.append(transaction)
    return filtered_transactions