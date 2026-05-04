def is_email(text):
    '''
    Funkcija validē e-pastu - obligāti jābūt @ un .

    Args:
        text: tiek validēts ievadītais e-pasts.

    Atgriež:
        bool: ja e-pastā ir @ un aiz tā ., tad True.

    Piemēri:
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

def is_phone_number(text):
    '''
    Funkcija validē telefona numuru pēc LV nr. standartiem - +371 priekšā, tad vēl 8 cipari aiz tā.

    Args:
        text: validējamais tel. nr.

    Atgriež:
        bool: True, ja sākas ar +371, un pēc tam, neatkarīgi no atstarpēm, ievadīti 8 CIPARI. Citādāk - False.

    Piemēri:
    print(is_phone_number("+27755667788")) #False
    print(is_phone_number("+371 22334455")) #True
    '''
    if not text.startswith("+371"): #.startswith() nodrošina, ka numurs sākas ar valsts kodu
        return False
    number=text[len("+371"):].strip() #tiek atstāts numurs bez valsts koda, kā arī tā sākuma un beigās noņemtas atstarpes
    number=number.replace(" ","") #noņem visas atstarpes - tās, kuras numura vidū
    return number.isdigit() and len(number) == 8 #.isdigit() nodrošina, ka tikai cipari; len() nodrošina, ka 8 cipari numurā (LV)

def is_valid_age(age):
    '''
    Funkcija validē vecumu, kam jābūt veselam skaitlim, no 0 līdz 150.

    Args:
        age: validējamais skaitlis.

    Atgriež:
        bool: True, ja skaitlis ir no int klases (vesels skaitlis) un intervālā no 0 līdz 150 (abus galus ieskaitot).

    Piemēri:
    print(is_valid_age(150)) #True
    print(is_valid_age("abe")) #False
    print(is_valid_age(-1)) #False
    '''
    if not isinstance(age, int):
        return False
    if not 0<=age<=150:
        return False
    return True

#def is_strong_password(text): # Vismaz 8 simboli, satur burtus UN ciparus


#def is_valid_date(text): # YYYY-MM-DD formāts (pamata pārbaude)


if __name__ == "__main__":
    print(is_email("anna@inbox.lv")) #True
    print(is_email("anna@inb")) #False
    print(is_email("inbox.lv")) #False
    print(is_email("")) #False
    print(is_email("inbox.lv@anna")) #False
    print(is_phone_number("+37122334455")) #True
    print(is_phone_number("+3712233")) #False
    print(is_phone_number("22334455")) #False
    print(is_phone_number("")) #False
    print(is_phone_number("+27755667788")) #False
    print(is_phone_number("+371 22334455")) #True
    print(is_valid_age(-1)) #False
    print(is_valid_age(0)) #True
    print(is_valid_age(58)) #True
    print(is_valid_age(150)) #True
    print(is_valid_age(203)) #False
    print(is_valid_age("abe")) #False