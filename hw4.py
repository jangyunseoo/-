def rep_char():
    print('-'*nstr)
def draw_line_string():
    rep_char()
name=input('Input his/her name: ')
msg1='Hello '+name+','
msg2='Welcome to Seoul.'
nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
draw_line_string()
print(msg1)
print(msg2)
draw_line_string()
