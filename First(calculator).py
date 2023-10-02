print('Welcome to calculator')
f = int(input('Enter First namber:'))
s = int(input('Enter second number:'))
o = input('Enter Operation:')
if o== '+' :
   print(f+s)
elif o=='-' :
   print(f-s)
elif o=='*' :
   print(f*s)
if o=='/' :
   print(f/s)
else:
    print('This operation is not valid')