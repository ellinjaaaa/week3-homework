def capitalize(text):
    '''Funkcija nodrošina vārdam pirmo lielo burtu.

    Args:
        text(str): str, kas tiks modificēts.

    Atgriež:
        tekstu ar lielo sākumburtu.
        
    Piemērs:
    print(capitalize("hello")) izvade: Hello
    '''
    if not text:
        return text #ja nav str vai tukšs str, atgriezīs tekstu tādu, kāds ir.
    return text[0].upper() + text[1:]

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

    Piemēri:
    print(truncate("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind."))
    izvade: Be who you are and sa... - max_len netika norādīts, tādēļ tika ierobežots pēc 20.rakstzīmes (noklusējuma vērtība).

    print(truncate("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.", 50))
    izvade: Be who you are and say what you feel, because thos... - max_len tika norādīts, tādēļ tika ierobežots pēc 50.rakstzīmes.

    print(truncate("Be who you are."))
    izvade: Be who you are. - max_len netika norādīts, taču arī noklusējuma vērtība netika pārsniegta.
    '''
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text

def count_words(text=None):   #Lai programma necrashotu, textam ir noklusējuma vērtība.
    '''
    Funkcija nodrošina vārdu saskaitīšanu.

    Args:
        text: tekstam tiks saskaitīts vārdu skaits. Ja netiek nekas vispār uzrakstīts, tad noklusējuma vērtība None iedarbojas,
        kurai, tāpāt kā tukšam tekstam ("")", piešķirta 0. Tālāk jau gan pārveido par string, lai saskaitītu vārdu skaitu.

    Atgriež:
        vārdu skaitu.

    Piemēri:
    print(count_words())
    izvade: 0 - piešķirta noklusējuma vērtība None, kura, savukārt, atgriež 0.

    print(count_words(13))
    izvade: 1 - int paliekot par str, viens vārds.

    print(count_words("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind."))
    izvade: 21
    '''
    if text is None or text=="":
        return 0   #Lai neuztvertu pēc string pārveidojuma kā 1 vārdu, tiek pirms tam piešķirta 0.
    else:
        text_str=str(text)
        count=len(text_str.split())
        return count

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

    Piemēri:
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
    try:
        n=float(num) #Ja tiek ievadīti decimālskaitļi, programma spēs tos apstrādāt.
        l=float(low)
        h=float(high)
        return max(l, min(n, h))
    except (ValueError, TypeError):
        return low #Lai necrashotu, atgriež mazāko noklusējuma vērtību.

def is_prime(num):
    '''
    Nosaka ar bool vērtībām (True/False). vai skaitlis ir pirmskaitlis. Ja skatlis mazāks par 2 - uzreiz False, tā kā, tikai
    sākot ar 2, sākas pirmskaitļi. Tad pārbauda, vai dalās ar skaitli intervālā no 2 līdz pat kvadrātsaknei no mūsu 
    skaitļa (+1, lai range ieskaitītu arī kvadrātsakni) - pietiek ar kvadrātsakni, tā kā dalītāji bieži vien sadalās pāros,
    kur viens dalītājs ir mazāks par kvadrātsakni no mūsu skaitļa, savukārt, otrs - lielāks. Piem., skaitlis 36 - kvadrātsakne
    no tā ir 6, dalītāju pāri (1,36), (2,18), (3, 12), (4,9), (6,6) -, katram pārim ir dalītājs mazāks par skaitļa kvadrātsakni.
    Ja šis izpildās, tad False. Ja nekas no šī neizpildās - True, skaitlis ir pirmskaitlis.

    Args:
        num: skaitlis, kuram tiek pārbaudīts, vai tas ir pirmskaitlis.

    Atgriež:
        bool vērtību: False, ja skaitlis nav pirmskaitlis, True - ja tas ir.

    Piemēri:
    print(is_prime(9))
    izvade: False

    print(is_prime(-2))
    izvade: False

    print(is_prime(17))
    izvade: True
    '''
    if num<2:
        return False
    for p in range (2, int(num**0.5)+1):
        if num % p==0:
            return False
    return True

def factorial(n):
    '''
    Funkcija aprēķina skaitļa faktoriālu.

    Args:
        n: skaitlis, kuram rēķina faktoriālu.

    Atgriež:
        Ja skaitlis decimālskaitlis, atgriež None, tā kā tiem nav faktoriāla. Ja skaitlis mazāks par 0, atgriež None - jo
        negatīviem skaitļiem nav faktoriāla. Ja skaitlis ir 0, faktoriāls ir 1. Ja lielāks par 0, tiek aprēķināts faktoriāls.

    Piemēri:
    print(factorial(0))
    izvade: 1

    print(factorial(-2))
    izvade: None

    print(factorial(6))
    izvade: 720

    print(factorial(3.5))
    izvade: None
    '''
    if not isinstance(n, int): #Decimālskaitlim nevar būt faktoriāls.
        return None
    elif n<0:
        return None
    elif n==0:
        return 1
    else:
        fac=1
        for a in range(1,n+1):
            fac*=a
        return fac
        
def total(*numbers):
    '''
    Funkcija sasummē skaitļus kopā.

    Args:
        *numbers: skaitļi; neatkarīgi no skaitļu skaita, tie visi tiks sasummēti.

    Atgriež:
        Ja skaitļi nav int vai float klasē, tiks atgriezts None. Bool vērtības arī netiek 
        ieskaitītatas, jo tās ir int apakšklase, None=0, True=1. Lai tie netiktu pieskaitīti,
        atgriež vienkārši None. Ja skaitļiem iepriekš noteiktie nosacījumi ievēroti - tie ir
        int vai float klasē -, tiek sasummēti visi kopā.

    Piemēri:
    print(total("abe"))
    izvade: None

    print(total(True, 2))
    izvade: None

    print(total(9, 3.4, 15.7654))
    izvade: 28.165399999999998

    print(total(9,5,4,6,4,7))
    izvade: 35
    '''
    tog=0
    for c in (numbers):
        if not isinstance (c, (int, float)) or isinstance(c, bool):
            return None
        else:
            tog+=c
    return tog
    
def average(*numbers):
    '''
    Funkcija aprēķina vidējo aritmētisko, izmantojot iepriekš definēto funkciju, kas aprēķina
    skaitļu summu, kā arī izmantojot len().

    Args:
        *numbers: skaitļi, kas, neatkarīgi no skaitļu skaita, tiks sasummēti, un tad izdalīti
        ar to skaitu.

    Atgriež:
        None, ja tuksš saraksts vai nav int/float klases vērtības (ja bool, tad arī None). Citādāk:
        skaitļi tiek sasummēti ar iepriekšējās funkcijas total(*numbers) palīdzību, tad izdalīti ar
        to skaitu (len(numbers)).

    Piemēri:
    print(average())
    izvade: None

    print(average(True, "lin", 4))
    izvade: None

    print(average(9,4,5,6,7))
    izvade: 6.2
    '''
    tot=total(*numbers)
    if len(numbers)==0:
        return None
    elif tot is None:
        return None
    else:
        return tot/len(numbers)
    
if __name__ == "__main__":
    print(capitalize("hello"))
    print(truncate("Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.", 50))
    print(count_words(13))
    print(clamp(-5))
    print(is_prime(17))
    print(factorial(0))
    print(total(9, 3.4, 15.7654))
    print(average(9,4,5,6,7))