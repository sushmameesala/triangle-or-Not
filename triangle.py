#check whether the given numbers forms triangke or not #
a=int(input( ))
b=int(input( ))
c=int(input( ))
if(((a+b)>c)or((a+c)>b)or((b+c)>a)):
    print("these forms triangle")
else:
    print(" not forms triangle")