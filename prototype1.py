# fungsi buat nyari nilai yang paling dekat ke 24 dalam suatu list
def cari_solusi(listAngka) :
    s = listAngka[0]
    for a in listAngka :
        if abs(24-a) < abs(24-listAngka[0]) :
            s = a
    return s

# fungsi operasi a dioperasikan b
def op(char,a,b):
    if char == '+' :
        return (a+b)
    elif char == '-' :
        return  (a-b)
    elif char == '*' :
        return (a*b)
    elif char == '/' and b != 0:
        return (a/b)
    else :
        return 0

#Memulai input program
v=float(input())
w=float(input())
x=float(input())
y=float(input())


#4 angka yang diinput disimpan dalam list sementara
inputAngka=[v,w,x,y]

operator = ['+', '-', '*','/']

# Traverse through all inputAngka elements
for i in range(4):

    # Last i elements are already in place
    for j in range(0, 4-i-1):

        # traverse the inputAngka from 0 to 4-i-1
        # Swap if the element found is greater than the next element
        if inputAngka[j] < inputAngka[j+1] :
            inputAngka[j], inputAngka[j+1] = inputAngka[j+1], inputAngka[j]
#inputAngka sudah terurut menurun

#tempHasil buat penyimpanan sementara untuk dibandingkan yang mana paling deket ke 24
tempHasil =[0,0,0,0]

#variabel menyimpan sum
sum = inputAngka[0]

#variabel nyimpen string solusi
solusi = str(sum)

for a in range (1,4) :
    i=0
    for b in operator :
        tempHasil[i]=op(b,sum,inputAngka[a])
        i=i+1
    sum = cari_solusi(tempHasil)
    if(sum == tempHasil[0]) :
        solusi = "%s + %s"%(solusi ,inputAngka[a])
    elif(sum == tempHasil[1]) :
        solusi = "%s - %s"%(solusi ,inputAngka[a])
    elif(sum == tempHasil[2]) :
        solusi = "%s * %s"%(solusi ,inputAngka[a])
    elif(sum == tempHasil[3]) :
        solusi = "%s / %s"%(solusi ,inputAngka[a])


print solusi, '=', sum
