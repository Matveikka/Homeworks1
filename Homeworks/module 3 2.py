def send_email(message, recipient,*,sender = "university.help@gmail.com"):
    if '@' not in recipient or '@' not in sender:
        is_find = True
        if is_find:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    if (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) is False:
        print(f'Невозможно отправить письмо с адреса {sender}, на адрес {recipient}')
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender}, на адрес, {recipient}')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
send_email('@', 'mama@mail.ru')

