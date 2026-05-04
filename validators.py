def is_email(text):
    '''
    Funkcija validē e-pastu - obligāti jābūt @ un .

    Args:
        text: tiek validēts ievadītais e-pasts.

    Atgriež:
        bool: ja e-pastā ir @ un aiz tā ., tad True.

    Piemērs:
    print(is_email("anna@inbox.lv")) #True
    print(is_email("anna@inb")) #False
    '''
    if "@" not in text:
        return False
    local, domain = text.split("@", 1)
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True

#def is_phone_number(text): # Latvijas formāts: +371 XXXXXXXX (8 cipari)


#def is_valid_age(age): # 0–150, vesels skaitlis


#def is_strong_password(text): # Vismaz 8 simboli, satur burtus UN ciparus


#def is_valid_date(text): # YYYY-MM-DD formāts (pamata pārbaude)


if __name__ == "__main__":
    print(is_email("anna@inbox.lv")) #True
    print(is_email("anna@inb")) #False
    print(is_email("inbox.lv")) #False
    print(is_email("")) #False
    print(is_email("inbox.lv@anna")) #False