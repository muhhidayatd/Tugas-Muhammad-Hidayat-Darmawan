class Lingkaran(object):
    def __init__(self, r):
        self.r = r
        self.phi = 3.14

    def hitungLuas(self):
        return self.phi * self.r * self.r
    def hitungKeliling(self):
        return 2 * self.phi * self.r

def main():

    lingkaran = Lingkaran(7)

    print("Luas Lingkaran")
    print("phi\t: ",lingkaran.phi)
    print("r\t: ", lingkaran.r)
    print("Luas\t= ", lingkaran.hitungLuas())

    lingkaran2 = Lingkaran(6)

    print("\nLuas Lingkaran")
    print("phi\t: ", lingkaran.phi)
    print("r\t: ", lingkaran.r)
    print("Luas\t= ", lingkaran.hitungKeliling())

if __name__=="__main__":
    main()

class Persegi(object):
    def __init__(self, s):
        self.s = s
    def hitungLuas(self):
        return self.s * self.s
    def hitungKeliling(self):
        return 4 * self.s 
    
def main():
    
    persegi = Persegi(4)

    print("\nLuas Persegi")
    print("Sisi\t: ", persegi.s)
    print("Luas\t= ", persegi.hitungLuas())

    persegi2 = Persegi(6)

    print("\nKeliling Persegi")
    print("Sisi\t: ", persegi.s)
    print("Luas\t= ", persegi.hitungKeliling())

if __name__=="__main__":
    main()
