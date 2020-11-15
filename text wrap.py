import textwrap
def val(s,w):
    print(textwrap.fill(s,w))
a=input('Enter the prahraph:')
b=int(input("Enter the width:"))
val(a,b)
