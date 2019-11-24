'''
मैंने सिर्फ अभ्यास करने और अनुभव हासिल करने का फैसला किया। आँखों में दर्द के लिए क्षमा करें।
'''


def recpol(s):
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return recpol(s[1:-1])


def stringpol(t):
    return list(t) == list(reversed(t))

def stringpol2(t):
    return t == t[::-1]


def cyclpol(t):  # by index
    for i in range(len(t)):
        s = 0
        if t[i - 1] != t[-i]:
            s -= 1
    if s >= 0:
        return True
    return False


def cyclpol2():  # by object
    for i in t:
        n = len(t)
        s = 0
        if i != t[n - 1]:
            s -= 1
            if s >= 0:
                return True
            return False


def choise():
    input_user = input('1|2|3|4|5|anything else to exit')
    if input_user == '1':
        t = recpol(input('enter a word and find out if it is a polindrome'))
    elif input_user == '2':
        t = stringpol(input('enter a word and find out if it is a polindrome'))
    elif input_user == '3':
        t = stringpol2(input('enter a word and find out if it is a polindrome'))
    elif input_user == '4':
        t = cyclpol(input('enter a word and find out if it is a polindrome'))
    elif input_user == '5':
        t = cyclpol2(input('enter a word and find out if it is a polindrome'))
    else:
        exit(0)
    print(t)
    choise()


choise()

