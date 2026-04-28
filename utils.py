def capitalize(text):
    '''Funkcija nodrošina vārdam pirmo lielo burtu.

    Args:
        text(str): str, kas tiks modificēts.

    Atgriež:
        tekstu ar lielo sākumburtu.'''
    if not text:
        return text #ja nav str vai tukšs str, atgriezīs tekstu tādu, kāds ir.
    return text[0].upper() + text[1:]

#Piemērs:
#print(capitalize("hello")) izvade: Hello

def truncate(text, max_len=20):
    '''
    Funkcija nodrošina, ka pēc norādītās max_len vērtības vai arī noklusējuma vērtības/rakstzīmes, vārds nepārsniedz doto garumu.
    Ja tas pārsniedz, tiek pierakstīta daudzpunkte.

    Args:
        text(str): str, kam atkarībā no situācijas, var tikt ierobežots garums un pievienota daudzpunkte.
        max_len: noklusējuma vērtība 20 vai arī var tikt ievadīta. Pēc norādītās vērtības rakstzījmu skaits beidzas un tiek
        pievienota daudzpunkte.

    Atgriež:
        Tādu pašu tekstu, ja nepārsniedz rakstzīmju skaitu, vai arī ierobežotu tekstu ar daudzpunkti.
    '''
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text

'''Piemēri
print(truncate("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind."))
izvade: Be who you are and sa... - max_len netika norādīts, tādēļ tika ierobežots pēc 20.rakstzīmes (noklusējuma vērtība).

print(truncate("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.", 50))
izvade: Be who you are and say what you feel, because thos... - max_len tika norādīts, tādēļ tika ierobežots pēc 50.rakstzīmes.

print(truncate("Be who you are."))
izvade: Be who you are. - max_len netika norādīts, taču arī noklusējuma vērtība netika pārsniegta.'''

def count_words(text=None):   #Lai programma necrashotu, textam ir noklusējuma vērtība.
    '''
    Funkcija nodrošina vārdu saskaitīšanu.

    Args:
        text: tekstam tiks saskaitīts vārdu skaits. Ja netiek nekas vispār uzrakstīts, tad noklusējuma vērtība None iedarbojas,
        kurai, tāpāt kā tukšam tekstam ("")", piešķirta 0. Tālāk jau gan pārveido par string, lai saskaitītu vārdu skaitu.

    Atgriež:
        vārdu skaitu.
    '''
    if text is None or text=="":
        return 0   #Lai neuztvertu pēc string pārveidojuma kā 1 vārdu, tiek pirms tam piešķirta 0.
    else:
        text_str=str(text)
        count=len(text_str.split())
        return count

'''
print(count_words())
izvade: 0 - piešķirta noklusējuma vērtība None, kura, savukārt, atgriež 0.

print(count_words(13))
izvade: 1 - int paliekot par str, viens vārds.

print(count_words("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind."))
izvade: 21
'''

def clamp(num, low=0, high=50):
    '''
    Ierobežo skaitli noteiktajā intervālā - vai nu pēc noklusējuma vērtībām, vai nu pēc sevis ntoeiktā. Ja pārsniedz
    intervālu zemākajā vai augstākajā galā, tad tas gals tiek atgriezts. Ja ir intervāla vidū, skaitlis tiek atgriezts.

    Args:
        num: skaitlis, kurš tiek ierobežots intervālā.
        low: zemākā vērtība, kas varētu būt skaitlim. Ja skaitlis zemāks, tad zemākā vērtība pēc noklusējuma 0 vai arī
        lietotāja noteiktā tiks atgriezta.
        high: augstākā vērtība, kas varētu būt skaitlim. Ja skaitlis augstāks, tad augstākā vērtība pēc noklusējuma 50 vai arī
        lietotāja noteiktā tiks atgriezta.

    Atgriež:
        intervālā esošu skaitli vai ar kādu intervāla galu (ierobežojumu).
    '''
    try:
        n=float(num) #Ja tiek ievadīti decimālskaitļi, programma spēs tos apstrādāt.
        l=float(low)
        h=float(high)
        return max(l, min(n, h))
    except (ValueError, TypeError):
        return low #Lai necrashotu, atgriež mazāko noklusējuma vērtību.

'''
print(clamp(-5))
izvade: 0.0 - vērtība tiek ierobežota ar mazāko noklusējuma vērtību.

print(clamp(5.3))
izvade: 5.3 - vērtība ietilpst intervālā un programma spēj apstrādāt decimālskaitli.

print(clamp(97))
izvade: 50.0 - vērtība tiek ierobežota ar lielāko noklusējuma vērtību.

print(clamp("Mimi"))
izvade: 0 - lai necrashotu Erroram programma piešķir mazāko noklusējuma vērtību.

print(clamp(30,10,20))
izvade: 20.0 - programma piešķir lietotāja noteikto augstāko vērtību, tā kā num ri ārpus noteiktā intervāla.
'''