import speech_recognition as sr

1words = {'1'}
2words = {'2'}
3words = {'3'}
4words = {'4'}
5words = {'5'}
6words = {'6'}
7words = {'7'}
8words = {'8'}

r=sr.Recognizer()
oneX=sr.AudioFile('XoneX.flac')
with oneX as source:
    audio=r.record(source)
    if oneX in aoneX in awords.keys():
        print('1')
    elif oneX in bwords.keys():
        print('2')
    elif oneX in cwords.keys():
        print('3')
    elif oneX in dwords.keys():
        print('4')
    elif oneX in ewords.keys():
        print('5')
    elif oneX in ewords.keys():
        print('6')
    elif oneX in ewords.keys():
        print('7')
    elif oneX in ewords.keys():
        print('8')
