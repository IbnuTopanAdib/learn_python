def eat (bf, lunch, dinner):
    print(f"today I eat {bf} and {lunch} and {dinner}")

# sebelum tanda bintang kita bisa memasang argumen baik positional ataupun keyword only namun setelah tand * harus 
# keyword only
def fn1(a, b, *, kwonly):
    print(f"a: {a} and b: {b} and kwonly {kwonly}")

def fn2(a, b, *args, kwonly = None):
    print(f"{a=}, {b=}, {args=}, {kwonly}")

#prnggunaan tanda * diawal parameter juga sangat menguntungkan kita bisa memasang argumen sebagai keyword only arguments
def fn3(*, item, price, quantity ):
    print(f"{quantity} units of {item} at {price} price")

#positional only arguments 
# sebelum tanda / semua parameter akan dianggap sebagai positional arguments

def fn4(poss_only, /,poss_or_kw, *, kw_only):
    pass

# tanda / diakhir akan membuat semua parameter akan dianggap sebagai positional arguments
def fn5(a, b,/):
    pass
# tanda / biasanya juga diikuti dengan tanda bintang untuk membuat parameter sebelum / dianggap sebagai positional arguments
#dan parameter setelah * dianggap sebagai keyword only arguments
def fn5(poss_only,/,*, kwonly):
    pass

# kita juga bisa menambahkan **kargs untuk menangkap semua keyword argument
def fn6(poss_only, /, *args,kwonly, **kwargs):
    pass

def printinfo(*args, **kwargs):
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argumen kata kunci {}:{}'.format(key, value))
 
 
# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i':7, 'j':8})

def call_fn():
    # positional arguments
    eat("nasgor", "geprek", "sop")
    #keyword arguments
    eat(bf = "nasi", lunch = "kambing", dinner = "apel")
    try:
        fn1(12, 13, 12) # akan menampilkan error
    except Exception as e:
        print(e)
    fn1("babi", "kucing", kwonly= 12)
    fn2(1, 2, 3, 4, kwonly="20")
    fn3(item = "laptop", price = 200, quantity=10)
call_fn()





