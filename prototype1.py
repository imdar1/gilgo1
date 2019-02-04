# fungsi buat nyari nilai yang paling dekat ke 24 dalam suatu list
def cari_solusi(listAngka) :
    s = 24-listAngka[0]
    hsl = listAngka[0]
    for a in range(1,4) :
        #26 24 25 25
        if abs(24-listAngka[a]) < abs(s) :
            s = 24-listAngka[a]
            hsl = listAngka[a]
    return hsl

# fungsi operasi a dioperasikan b
def op(char,a,b):
    if char == '+' :
        return (a+b)
    elif char == '-' :
        return  (a-b)
    elif char == '*' :
        return (a*b)
    elif char == '/':
        return (a/b)
    else :
        return 0

#Memulai input program
valid = False
while not (valid) :
    print("Input : ")
    try:        
        v,w,x,y = map(float, input().split())
        if ((v>0 and w>0 and x>0 and y>0) and (v <=13 and w<=13 and x <=13 and y<=13)):
            valid = True               
        else :     
            print("Input 4 integer [1..13] dipisah dengan spasi") 
    except:
        print("Input 4 integer [1..13] dipisah dengan spasi") 


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
    #print(tempHasil)
    if(sum == tempHasil[0]) :
        solusi = "%s + %s"%(solusi ,inputAngka[a])
    elif(sum == tempHasil[1]) :
        solusi = "%s - %s"%(solusi ,inputAngka[a])
    elif(sum == tempHasil[2]) :
        solusi = "%s * %s"%(solusi ,inputAngka[a])
    elif(sum == tempHasil[3]) :
        solusi = "%s / %s"%(solusi ,inputAngka[a])


print (solusi, '=', sum)
