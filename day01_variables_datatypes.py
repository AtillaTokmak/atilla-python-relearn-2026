#Welcome to first day at this day I will try to relarn the variables and datatypes.

#First example
ogrenci =str(input("İsim soy isim gir: "))
ogrenci_no = int(input("Okul numaranı gir: "))
ogrenci_brans = str(input("Branşını gir: "))
#There is a two type of multi variable and printing text at the same time first it called F-string printing second one is called string concatenation

print(f"Ogrenci ismi:  {ogrenci} \nOgrenci numarası: {ogrenci_no} \nOgrenci bransı: {ogrenci_brans}")

#But the reccomended one is f-string bcs it is cleaner and its easy to read

# string concatenation = print("Ogrenci ismi: "+ ogrenci+"\n"+ "Ogrencinin branşı: "+ogrenci_brans+ "\n" + "Ogrenci No: "+ ogrenci_no+"\n")


#Second Example

a = 5
b = "Hi"


print(type(a))
print(type(b))


x = 10
y = 5.5

print(type(x) is type(y))

#Third Expamle
text = "merhabalar ben ahmet"
x = text.capitalize()
print(x)

text = "merhabalar ben ahmeti"
x = text.title()
print(x)

text = "merhabalar ben ahmet"
x = text.swapcase()
print(x)
text = "merhabalar BEN ahmet"

#Final example of the DAY01
degisecek01=int("5")
degisecek02=float("5.232323")
degisecek03=str(42)
degisecek04=int(3.9)
print(type(degisecek01))
print(type(degisecek02))
print(type(degisecek03))
print(type(degisecek04))
