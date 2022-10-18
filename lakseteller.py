godkjent = False;
laks = 0;
while godkjent == False:
    laks = float(input("Skriv et positivt heltall: "))
    if laks % 1 == 0 and laks > 0:
        godkjent = True

laks = int(laks)
for i in list(range(1,laks+1)):
    if i == 1:
        print(i, " laks")
    else: 
        print(i, " laksar")
        