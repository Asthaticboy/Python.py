a = input(
    "You Should 'Code' or 'Decode':-\nIf code write 1 if decode write 2 If nothing write 3 "
)
if a == '1':
  while True:
   yo = input('Write Your Text :-')
   import random
   def shaurya(word):
    choice=['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    from3=random.choice(choice)
    from4 = random.choice(choice)
    from5 = random.choice(choice)
    from6 = random.choice(choice)
    newfront=word[0]+from3+from4+word[1:-1]+from5+from6+word[-1]
    return newfront
   print(shaurya(yo))
   break
elif a == '3':
  print("Bye Bye Tata Bye Bye Good Bye")
elif a == '2':
   while True:
     b = input('Write code here:- ')
   # for write code first,write the first letter of word first and then write 2 random letter and then write any symbol then write the remaining word but the last third letter is a another symbol then write random to letter and then the last third letter of the word.
     c = b[3:-3]
     d = c.replace(c[0],b[0])
     e = d.replace(d[-3],b[-1])
     print('Decode of code is:- ',e)
     break
else:
  print('This Number is Not Valid,Please Try Again')
   
