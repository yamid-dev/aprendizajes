print("________________________________________________________________________________")
x="Hola"
print(type(x)) #la funcion type() devuelve el tipo de dato de una variable
x=123
print(type(x))
x=1000.02
print(type(x))
x=100,200
print(type(x))
x=True
print(type(x))
x=[]
print((type(x)))
x={}
print(type(x))
prueba="Hola Yamid"
print(prueba)
print(prueba,type(prueba))
print("________________________________________________________________________________")
def suma(a,b): #El comando def crea una funcion con sus parametros
    s=a+b
    print("resultado de la suma: ",s)
def resta(a,b): #El comando def crea una funcion con sus parametros
    r=a-b
    print("resultado de la resta: ",r)
def mult(a,b): #El comando def crea una funcion con sus parametros
    m=a*b
    print("resultado de la multiplicación: ",m)
def div(a,b): #El comando def crea una funcion con sus parametros
    d=a/b
    print("resultado de la división: ",d)
a=10
b=30
suma(a,b)
resta(a,b)
mult(a,b)
div(a,b)