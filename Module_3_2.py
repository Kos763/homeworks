
def send_email(message, recipient, *, sender = "university.help@gmail.com"):


    if "@" not in recipient or "@" not in sender or not sender.endswith \
                ((".com", ".ru", ".net")) or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}.")

    elif sender == recipient:
        print("Нельзя отправить письмо самому себе")

    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: {sender} на адрес: {recipient}")

    else:
        print(f"Письмо успешно отправлено от: {sender} на адрес: {recipient} с сообщением: {message}")





send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print()
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print()
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print()
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
