#Welcome to second day at this day I will try to relarn the operations.
def main():
    sec=int(input(f"Lütfen hangi metot'un çalıştırılacağını seçiniz : \n(1,2)"))
    match sec:
        case 1:
            firstmethod()
        case 2:
            ilk_sayi = int(input("Hesaplama için ilk sayıyı giriniz: "))
            ikinci_sayi = int(input("Hesaplama için ikinci sayıyı giriniz: "))
            islem = int(input("Yapılacak operasyonu seçin: (Toplama 1, Çıkarma 2, Çarpma 3, Bölme 4)"))

            Calc(ilk_sayi, ikinci_sayi, islem)



def firstmethod():
    a = 5
    b = 3
    c = a + b
    d = a - b
    e = a * b
    f= a / b
    g = a // b # This is a division operation but the catch is example of you dividing 7 and 2 the answer is 3.5 if you use floor division it will correct to the 3.
    h = a % b # this is modulus operation for checking which returns the remainder of a division between two numbers.
    i = a ** b # this is for Exponentiation now we are making 5^3 but there is a catch it is also used for opening directories
    print(f"First Number: {a} Second Number: {b}\n Addition Proccess Result: {c}\n Subcration Result: {d}\n Multipliction Result: {e}\n Division Result: {f}\n Floor Division {h}\n Modulus: {f} Exponentiation : {i}")


def Calc(first, second, operation):
    print(first, second, operation)
    match operation:
        case 1:
            sonuc = first + second
            print(sonuc)
        case 2:
            sonuc = first - second
            print(sonuc)
        case 3:
            sonuc = first * second
            print(sonuc)
        case 4:
            sonuc = first // second
            print(sonuc)

