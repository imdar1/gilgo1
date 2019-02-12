import sys

class Graf:
    def __init__(self,simpul):
        self.simpul = simpul
        self.adjMatriks = [[0 for kol in range(simpul)] for brs in range(simpul)]
    
    def tambahSisi(self,simpul1,simpul2,bobot=1):
        self.adjMatriks[simpul1][simpul2] = bobot

    def ubahBobot(self,simpul1,simpul2,bobot):
        self.adjMatriks[simpul1][simpul2] = bobot   


def hitungBobot(listsolusi,k):
    # Urutkan berdasarkan solusi
    # Idenya cari yang terdekat ke 24
    listbobot = [0,0,0,0]
    n = 1
    idxmax = 0
    for i in range(1,4):
        if (abs(24-listsolusi[i])>abs(24-listsolusi[idxmax])):
            idxmax = i
    for i in range(0,4):
        idxmin = idxmax
        for j in range(0,4):
            if (abs(24-listsolusi[j])<=abs(24-listsolusi[idxmin])) and (not listbobot[j]):
                minval = abs(24-listsolusi[j])
                idxmin = j
        if (minval == 0):
            listbobot[idxmin] = 1
            n+=1
        else:
            listbobot[idxmin] = n+k*10
            n+=1
    return listbobot

def simpultoOP(simpul):
    return (int(simpul)-1)%4

def updateBobot(g,listAngka,path,simpul):
    #0 ana 1 2 3 4
    #1 2 3 4 ama 5 6 7 8
    #5 6 7 8 ama 9 10 11 12
    #9 10 11 12 ama 13
    operator = ['+','-','*','/']
    if (simpul <= 8):
        listjalur = path[simpul].split('-')
        i = 0
        tempsolusi = [0,0,0,0]
        for a in operator:
            if (simpul == 0):
                tempsolusi[i] = eval(str(listAngka[0])+a+str(listAngka[1]))
            elif (simpul <= 4):
                #tempsolusi[i] = eval('('+str(listAngka[0])+operator[simpultoOP(simpul)]+str(listAngka[1])+')'+a+str(listAngka[2]))
                tempsolusi[i] = eval(str(listAngka[0])+operator[simpultoOP(simpul)]+str(listAngka[1])+a+str(listAngka[2]))
            elif (simpul <= 8):
                #tempsolusi[i] = eval('(('+str(listAngka[0])+operator[simpultoOP(listjalur[1])]+str(listAngka[1])+')'+operator[simpultoOP(simpul)]+str(listAngka[2])+')'+a+str(listAngka[3]))
                tempsolusi[i] = eval(str(listAngka[0])+operator[simpultoOP(listjalur[1])]+str(listAngka[1])+operator[simpultoOP(simpul)]+str(listAngka[2])+a+str(listAngka[3]))
            i+=1
        if (simpul == 0):
            a = 1
            b = 5
            k = 0
        else:
            a = int(((simpul-1)/4))*4+5
            b = int(((simpul-1)/4))*4+9
            k = int(((simpul-1)/4))+1
        listbobot = hitungBobot(tempsolusi,k)
        j = 0
        for i in range(a,b):
            g.ubahBobot(simpul,i,listbobot[j])
            j+=1
    else:
        for i in range(9,13):
            g.ubahBobot(i,13,1)
    return g
    
def dijkstra(g,src,listAngka):
    dlist = [sys.maxsize]*g.simpul
    dlist[src] = 0
    path = ['']*g.simpul
    vstdSet = [False]*g.simpul
    for i in range(g.simpul):
        #Pertama cari simpul dengan total bobot paling minimum yang belum pernah dikunjungi
        minval = sys.maxsize
        for j in range(g.simpul):
            if (dlist[j]<minval) and (not vstdSet[j]):
                minval = dlist[j]
                idxmin = j
        #print(minval) 
        vstdSet[idxmin] = True
        #path[src] = str(src)
        g = updateBobot(g,listAngka,path,idxmin)
        for j in range(g.simpul):
            if (g.adjMatriks[idxmin][j] > 0) and (not vstdSet[j]) and (dlist[j] > dlist[idxmin] + g.adjMatriks[idxmin][j]): 
                dlist[j] = dlist[idxmin] + g.adjMatriks[idxmin][j]
                if path[idxmin] == '':
                    path[j] = str(idxmin)
                else:
                    path[j] = path[idxmin]+'-'+str(idxmin)
                #path[j] = path[j]+'-'+str(j)
    return path
 

def solution(v,w,x,y):
    #4 angka yang diinput disimpan dalam list sementara
    inputAngka=[v,w,x,y]

    # Traverse through all inputAngka elements
    for i in range(4):

        # Last i elements are already in place
        for j in range(0, 4-i-1):

            # traverse the inputAngka from 0 to 4-i-1
            # Swap if the element found is greater than the next element
            if inputAngka[j] < inputAngka[j+1] :
                inputAngka[j], inputAngka[j+1] = inputAngka[j+1], inputAngka[j]
    #inputAngka sudah terurut menurun

    g  = Graf(14) 
    path = dijkstra(g,0,inputAngka)
    operator = ['+','-','*','/']
    listjalur=path[13].split('-')
    #print(listjalur)
    hsl = str(inputAngka[0])+operator[simpultoOP(listjalur[1])]+str(inputAngka[1])+operator[simpultoOP(listjalur[2])]+str(inputAngka[2])+operator[simpultoOP(listjalur[3])]+str(inputAngka[3])
    return hsl