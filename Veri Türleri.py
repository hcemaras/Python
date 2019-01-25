#Değişken Tanımlama
a = "Hello, World!"
b = 36
c = 1.80
d = 2j-1
e = 1 == 2
#Tek satırda birden fazla değişkene değer atanabilir.
f, g = False, True

#print() ile değişken değerini yazdırma
print("a= ", a)
a=  Hello, World!
print("1, 2'ye eşit midir?", e)
1, 2'ye eşit midir? False
print(d+3)
(2+2j)
print(f == 0, g == 1)
True True
#False ifadesi sayısal olarak 0'a, True ifadesi ise 1'e eşittir.
print(f + g)
1

#type() ile değişkenin türüne bakılabilir.
print(type(a), type(b), type(c), type(d))
<class 'str'> <class 'int'> <class 'float'> <class 'complex'>
print(type(e), type(f), type(g))
<class 'bool'> <class 'bool'> <class 'bool'>
