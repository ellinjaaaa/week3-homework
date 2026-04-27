#A daļa

numbers=[1,2,3,4,5,6,7,8,9]
numbers.append(12)
numbers.pop(5)

tog=0
count=0
for a in (numbers):
    tog+=a
    count+=1
    
mid=tog/count
print("Saraksta summa: ", tog)
print("Vidējā vērtība: ", mid)