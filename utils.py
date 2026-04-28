'''Funkcija nodrošina vārdam pirmo lielo burtu.

Args:
    text(str): str, kas tiks modificēts.

Atgriež:
    tekstu ar lielo sākumburtu.'''

def capitalize(text):
    if not text:
        return text #ja nav str vai tukšs str, atgriezīs tekstu tādu, kāds ir
    return text[0].upper() + text[1:]

#Piemērs:
#print(capitalize("hello"))




