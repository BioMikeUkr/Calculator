a = float(input('1 number: '))
u = input('What to do? (+, -. *, /, ^, : )')
if u =='^':
    u1 = float(input('Який ступінь?:'))
    c = a ** u1
else:
    b = float(input('2 number: '))
if u=='+':
    c=a+b
if u == '-':
    c = a-b
if u == '*':
    c = a*b
if u == '/':
    c = a/b
print('Result:' + str(c))