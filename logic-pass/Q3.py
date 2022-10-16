string = 'Artificial Intelligence'
def st(ch):
    string_repeated = 0
    i = 0
    while i < len(string):
        if string[i] == ch:
            string_repeated +=1
        i+=1
    print('the total amount of repeating the character {} is: '.format(ch), string_repeated)
    print('thanks for using this Function')
st(input('Enter a character: '))
