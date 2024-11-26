print("=" * 46)
print("\t\tKonversi Jarak")
print("=" * 46)


def konversi():
    meter = float(input("Masukan Dalam Satuan Meter\t\t= "))
    kilometer = (meter/1000)
    hektameter = (meter/100)
    dekameter = (meter/10)
    desimeter = (meter*10)
    centimeter = (meter*100)
    milimeter = (meter*1000)

    print("Jarak Dalam Satuan Kilometer  (KM)\t=",kilometer)
    print("Jarak Dalam Satuan Hektameter (HM)\t=",hektameter)
    print("Jarak Dalam Satuan Dekameter  (DAM)\t=",dekameter)
    print("Jarak Dalam Satuan Desimeter  (DM)\t=",desimeter)
    print("Jarak Dalam Satuan Centimeter (CM)\t=",centimeter)
    print("Jarak Dalam Satuan Milimeter  (MM)\t=",milimeter)

konversi()