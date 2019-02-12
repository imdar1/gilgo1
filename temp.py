import sys
import beta
#import prototype1

#Validasi argumen yang tepat
if (len(sys.argv) == 3):
	
	#Mempersiapkan file input dan file output
	file_input = open("{}.txt".format(sys.argv[1]),"r")
	file_output = open("{}.txt".format(sys.argv[2]),"w")
	
	#Memproses kedua file sekaligus penyelesaian dari 24 Game
	EmpatAngka = list(file_input.read().split())
	for i in range(4):
		EmpatAngka[i] = int(EmpatAngka[i])
	file_output.write(beta.solution(EmpatAngka[0],EmpatAngka[1],EmpatAngka[2],EmpatAngka[3]))
	#KALO PAKE FILE SATUNYA
	#file_output.write(prototype1.solution(EmpatAngka[0],EmpatAngka[1],EmpatAngka[2],EmpatAngka[3]))
	
	#Menutup file
	file_input.close()
	file_output.close()

#Kasus typo alias salah ketik
else:
	print("Argumen salah!")
	print("<Nama file python>.py <Nama file input tanpa format> <Nama file output tanpa format>")
