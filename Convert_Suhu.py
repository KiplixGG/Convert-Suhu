# Author 	= Paijo
# NickName      = COVID-19
# Github        = https://github.com/KiplixGG
# IG	        = @ahm_riski
# Contact	= 0895321579467


import os

def SD():
	print("=======================================================")

def convert():
	os.system("clear")
	choice = input('''
#######################################################
                WELCOME TO MATH CENTER
#######################################################
               Pilih Salah Satu Nomernya
=======================================================

1. °C ---> °R		7. °F ---> °C
2. °C ---> °F		8. °F ---> °R
3. °C ---> °K		9. °F ---> °K
4. °R ---> °C		10. °K ---> °C
5. °R ---> °F		11. °K ---> °R
6. °R ---> °K		12. °K ---> °F

              99. Keluar

NB :
C = Celcius
R = Reamur
F = Fahrenheit
K = Kelvin

=======================================================
Pilih Nomer : ''')

	if choice == '1':
		n1 = float(4/5)
		n2 = int(input("\nMasukan Nilainya (°C) : "))
		print("\nIni Rumusnya : 4/5 x °C")
		SD()
		print(n1,"x",n2,"=",n1*n2,"°R")
		SD()

	elif choice == '2':
		n1 = float(9/5)
		n2 = int(input("\nMasukan Nilainya (°C) : "))
		n3 = int(32)
		print("\nIni Rumusnya : (9/5 x °C) + 32°")
		SD()
		print("(",1,"x",n2,")","+",n3,"=",(n1*n2)+n3,"°F")
		SD()

	elif choice == '3':
		n1 = int(input("\nMasukan Nilainya (°C) : "))
		n2 = int(273)
		print("\nIni Rumusnya : °C + 273")
		SD()
		print(n1,"+",n2,"=",n1+n2,"°K")
		SD()

	elif choice == '4':
		n1 = float(5/4)
		n2 = int(input("\nMasukan Nilainya (°R) : "))
		print("\nIni Rumusnya : 5/4 x °R")
		SD()
		print(n1,"x",n2,"=",n1*n2,"°C")
		SD()

	elif choice == '5':
		n1 = float(9/4)
		n2 = int(input("\nMasukan Nilainya (°R) : "))
		n3 = int(32)
		print("\nIni Rumusnya : 9/4 x (°R + 32)")
		SD()
		print(n1,"x","(",n2,"+",n3,")","=",n1*(n2+n3),"°F")
		SD()

	elif choice == '6':
		n1 = float(5/4)
		n2 = int(input("\nMasukan Nilainya (°R) : "))
		n3 = int(273)
		print("\nIni Rumusnya : 5/4 x (°R - 273)")
		SD()
		print(n1,"x","(",n2,"-",n3,")","=",n1*(n2-n3),"°K")
		SD()

	elif choice == '7':
		n1 = float(5/9)
		n2 = int(input("\nMasukan Nilainya (°F) : "))
		n3 = int(32)
		print("\nIni Rumusnya : 5/9 x (°F - 32)")
		SD()
		print(n1,"x","(",n2,"-",n3,")","=",n1*(n2-n3),"°C")
		SD()

	elif choice == '8':
		n1 = float(4/9)
		n2 = int(input("\nMasukan Nilainya (°F) : "))
		n3 = int(32)
		print("\nIni Rumusnya : 4/9 x (°F - 32)")
		SD()
		print(n1,"x","(",n2,"-",n3,")","=",n1*(n2-n3),"°R")
		SD()

	elif choice == '9':
		n1 = float(5/9)
		n2 = int(input("\nMasukan Nilainya (°F) : "))
		n3 = int(32)
		n4 = int(273)
		print("\nIni Rumusnya : 5/9 x (°F - 32) + 273")
		SD()
		print(n1,"x","(",n2,"-",n3,")","+",n4,"=",n1*(n2-n3)+n4,"°K")
		SD()

	elif choice == '10':
		n1 = int(input("\nMasukan Nilainya (°K) : "))
		n2 = int(273)
		print("\nIni Rumusnya : °K - 273")
		SD()
		print(n1,"-",n2,"=",n1-n2,"°C")
		SD()

	elif choice == '11':
		n1 = float(4/5)
		n2 = int(input("\nMasukan Nilainya (°K) : "))
		n3 = int(273)
		print("\nIni Rumusnya : 4/5 x (°K - 273)")
		SD()
		print(n1,"x","(",n2,"-",n3,")","=",n1*(n2-n3),"°R")
		SD()

	elif choice == '12':
		n1 = float(9/5)
		n2 = int(input("\nMasukan Nilainya (°K) : "))
		n3 = int(273)
		n4 = int(32)
		print("\nIni Rumusnya : 9/5 x (°K - 273) + 32")
		SD()
		print(n1,"x","(",n2,"-",n3,")","+",n4,"=",n1*(n2-n3)+32,"°F")
		SD()

	elif choice == '99':
		print("\nArigato Gozaimaasu")
		os.system("sleep 1")
		os.sys.exit()

	else:
		print("\nInput Salah")
		os.system("sleep 1")
		convert()

	again()

def again():
	os.system("sleep 2")
	calc_again = input('''
Apakah Mau Menggunakan Convert Lagi
Ketik Y Untuk Ya
Ketik N Untuk Tidak
=======================================================
Ketik Apa : ''')

	if calc_again.upper() == 'Y':
		convert()

	elif calc_again.upper() == 'N':
		print("\nArigato Gozaimassu")
		os.system("sleep 1")
		os.sys.exit()

	else:
		print("\nInput Salah")
		again()

convert()
