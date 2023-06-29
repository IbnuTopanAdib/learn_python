import menyapa
import luas_bangunan
import keyword_class

lb = luas_bangunan.LuasBangunan(12, 13)

lb.segitiga()
#ekuivalen dengan === 
segitiga = luas_bangunan.LuasBangunan.segitiga(lb)
print(segitiga)

sapa = menyapa.Menyapa()
sapa.hallo()


kw = keyword_class.Apaya(name = "ibnu", income= 500000000)
print(kw)
