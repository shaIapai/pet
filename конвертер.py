# Определяем курсы обмена относительно российского рубля (RUB)
exchange_rates = {
    "RUB": {
        "RUB": 1.0,
        "CNY": 1 / 10.4823,
        "USD": 1 / 71.2090,
        "EUR": 1 / 82.5445,
        "KZT": 6.62,
    },
    "CNY": {
        "RUB": 10.4823,
        "CNY": 1.0,
        "USD": 10.4823 / 71.2090,
        "EUR": 10.4823 / 82.5445,
        "KZT": 10.4823 * 6.62,
    },
    "USD": {
        "RUB": 71.2090,
        "CNY": 71.2090 / 10.4823,
        "USD": 1.0,
        "EUR": 71.2090 / 82.5445,
        "KZT": 71.2090 * 6.62,
    },
    "EUR": {
        "RUB": 82.5445,
        "CNY": 82.5445 / 10.4823,
        "USD": 82.5445 / 71.2090,
        "EUR": 1.0,
        "KZT": 82.5445 * 6.62,
    },
    "KZT": {
        "RUB": 1 / 6.62,
        "CNY": (1 / 6.62) * (1 / 10.4823),
        "USD": (1 / 6.62) * (1 / 71.2090),
        "EUR": (1 / 6.62) * (1 / 82.5445),
        "KZT": 1.0,
    },
}

# Добавляем словарь синонимов для валют
currency_aliases = {
    "рубль": "RUB",
    "руб": "RUB",
    "rub": "RUB",
    "юань": "CNY",
    "yuan": "CNY",
    "cny": "CNY",
    "доллар": "USD",
    "бакс": "USD",
    "dollar": "USD",
    "usd": "USD",
    "евро": "EUR",
    "еврик": "EUR",
    "euro": "EUR",
    "eur": "EUR",
    "тенге": "KZT",
    "тенг": "KZT",
    "тэнге": "KZT",
    "тенгэ": "KZT",
}

# Доступные валюты для конвертации (используем только основные коды для отображения)
available_currencies = list(exchange_rates.keys())
print(
    f"Здравствуйте, пользователь! Доступные валюты: {', '.join(available_currencies)}"
)


def convert_currency(amount, from_currency_input, to_currency_input):
    """Конвертирует сумму из одной валюты в другую, используя синонимы."""
    # Преобразуем ввод пользователя в стандартный код валюты
    from_currency = currency_aliases.get(
        from_currency_input.lower(), from_currency_input.upper()
    )
    to_currency = currency_aliases.get(
        to_currency_input.lower(), to_currency_input.upper()
    )

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return (
            None,
            f"Недействительный код валюты или синоним. Доступные валюты: {', '.join(available_currencies)}. Попробуйте ввести, например: {', '.join(currency_aliases.keys())}",
        )

    if from_currency == to_currency:
        return amount, None

    try:
        # Получаем курс конвертации
        rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
        return converted_amount, None
    except KeyError:
        return None, "Курс конвертации недоступен."


# Получаем ввод от пользователя в цикле до успешного выполнения
while True:
    try:
        amount_str = input("Введите сумму для конвертации: ")
        amount = float(amount_str)

        from_currency_input = input(
            "Введите валюту, из которой конвертировать (например, USD, EUR, CNY, RUB): "
        )
        to_currency_input = input(
            "Введите валюту, в которую конвертировать (например, USD, EUR, CNY, RUB): "
        )

        converted_value, error = convert_currency(
            amount, from_currency_input, to_currency_input
        )

        if error:
            print(
                f"Ошибка: {error}\n"
            )  # Добавляем перенос строки для лучшей читаемости
            continue  # Если есть ошибка от функции конвертации, повторяем весь цикл ввода
        else:
            # Используем исходный ввод для более понятного вывода, но отображаем стандартные коды
            actual_from_currency = currency_aliases.get(
                from_currency_input.lower(), from_currency_input.upper()
            )
            actual_to_currency = currency_aliases.get(
                to_currency_input.lower(), to_currency_input.upper()
            )
            print(
                f"{amount:.2f} {actual_from_currency} равно {converted_value:.2f} {actual_to_currency}"
            )
            break  # Если конвертация успешна, выходим из цикла

    except ValueError:
        print(
            "Неверная сумма. Пожалуйста, введите числовое значение.\n"
        )  # Добавляем перенос строки
        # Цикл продолжится, чтобы запросить сумму снова
    except Exception as e:
        print(
            f"Произошла непредвиденная ошибка: {e}. Пожалуйста, попробуйте еще раз.\n"
        )  # Добавляем перенос строки
        continue  # В случае других непредвиденных ошибок, повторяем весь процесс
