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

'''Šķelšana - noteiktas daļas saraksta tiek atlasītas, atdalītas, idzēstas.'''
print(numbers[:3]) #Izdrukā pirmos 3 elementus - no 0. līdz 2.indeksam; 3. netiek iekļauts, tā kā end vērtība - neiekļaujoša.
print(numbers[-2:])   #Izdrukā pēdējos 2 elementus - no 2.elementa no beigām līdz saraksta beigām; -2 neiekļauts indekss.
print(numbers[::2]) #Izdrukā katru 2.elementu.