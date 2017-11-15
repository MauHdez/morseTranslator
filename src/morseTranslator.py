ALPHA = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n',
    'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y' ,'z', ' ']

MORSE = ['.-' ,'-...' ,'-.-.' ,'-..' ,'.' ,'..-.' ,'--.' ,'....' ,'..' ,'.---' ,
    '-.-' , '.-..' ,'--' ,'-.' ,'---' ,'.--.' ,'--.-' ,'.-.' ,'...' ,'-' ,
    '..-' ,'...-', '.--' ,'-..-' ,'-.--' ,'--..', '/']

# MORSE = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
#         'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
#         'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.',
#         's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
#         'y':'-.--', 'z':'--..', ' ':'/'}

def to_Morse(char):
    return dict(zip(ALPHA,MORSE)).get(char.lower(),'')

# def to_Char(char):
#     return dict(zip(MORSE,ALPHA)).get(char.lower(),'')

def translate_to_Morse(sentence):
    r = ''
    for c in sentence:
        r += to_Morse(c) + ' '
    return r

def translate_to_Alpha(morse):
    # Not implemented
    return
