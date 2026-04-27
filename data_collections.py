#A daļa

'''Izveidots skaitļu saraksts, kas pievieno jaunu elementu, un tad atņem noteiktu elementu (pēc indeksa).'''
numbers=[1,2,3,4,5,6,7,8,9]
numbers.append(12)   #Pievienota jauna vērtība.
numbers.pop(5)    #Atņemta specifiska vērtība (pēc indeksa).

'''Cikls, kas aprēķina saraksta skaitļu summu un tad arī vidējo vērtību, neizmantojot sum() un len(), bet gan pakāpeniski
aprēķinot.'''
tog=0   #Sākotnējā vērtība summai, pirms sākam skaitīt.
count=0    #Sākotnējā vērtība skaitīšanas reizei, pirms sākam skaitīt.
for a in (numbers):  #Cikls - tik reižu, cik sarakstā elementu.
    tog+=a    #Katru reizi summai tiek pievienots skaitlis no saraksta - sum() vietā.
    count+=1   #Katru reizi skaitīšanas reizei tiek pievienots 1 - len() vietā.

mid=tog/count    #Vidējā vērtība.
print("Saraksta summa: ", tog)
print("Vidējā vērtība: ", mid)

'''Izveidots tukšs un jauns saraksts, kuram caur ciklu ar noteiktu reižu skaitu, tiek pievienoti skaitļi no 
numbers saraksta, ja tie ir pāra skaitļi jeb dalās ar 2 bez atlikuma.'''
even_n=[]   #Pievienots tukšs saraksts, lai veidotos JAUNS saraksts, nevis tiktu ietekmēts oriģinālais.
for b in (numbers):   #Cikls - tik reižu, cik sarakstā elementu.
    if b%2==0:
        even_n.append(b)  #Ja skaitlis ir pāra, tad tiek PIEVIENOTS tukšajam sarakstam.

print("Jaunais saraksts ar pāra skaitļiem:", even_n)

'''Šķelšana - noteiktas daļas saraksta tiek atlasītas, atdalītas.'''
print(numbers[:3]) #Izdrukā pirmos 3 elementus - no 0. līdz 2.indeksam; 3. netiek iekļauts, tā kā end vērtība - neiekļaujoša.
print(numbers[-2:])   #Izdrukā pēdējos 2 elementus - no 2.elementa no beigām līdz saraksta beigām; -2 neiekļauts indekss.
print(numbers[::2]) #Izdrukā katru 2.elementu.

#B daļa
'''Izveidota vārdnīca, kur vārdam piešķirta atzīme. Turpmāk notiek jauna studenta pievienošana, kā arī jau esoša
studenta atzīmes maiņa.'''
students={"Anna":85,
          "Jānis":72,
          "Līga":95,
          "Kristīne":43,
          "Jāzeps":67}

students["Arvis"]=56 #Pievienots jauns students, uzrakstot jaunu atslēgu un piešķirot vērtību.
students["Līga"]=76 #Mainīta esošā atzīme, pie atslēgas pierakstot citu vērtību.

'''Ar for ciklu izvadīts katra skolēna vārds un atzīme.'''
for name, grade in students.items():
    print(f"{name}: {grade}")

'''Ar for cikla palīdzību tiek atrasts augstākais vērtējums. Pašā sākumā atzīme tiek pielīdzināta 0, tā kā tā ir pati zemākā
atzīme. For ciklā noteikti iterācijas mainīgie - name un grade. Ejot caur vārdnīcu, ja skolēna grade ir lielāks par iepriekš
noteikto mark (0), tad tas pārtop par turpmāk izmantojamo mark. Arī studenta vārds pamainās uz labāko rezultātu. Šādi katru
reizi tiek veikta pārbaude katram iterācijas mainīgajam - vai katrs nākamais grade ir lielāks par iepriekš noteikto augstāko
mark.Arī studenta vārds pamainās atbilstoši labākajam rezultātam.'''
mark=0
for name, grade in students.items():
    if grade>mark:
        mark=grade
        student=name

print(f"Students ar augstāko vērtējumu ir {student} ar atzīmi {mark}.")