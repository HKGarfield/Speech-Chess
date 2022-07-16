import speech_recognition as sr

awords = {'alpha'}
bwords = {'beta'}
cwords = {'charlie'}
dwords = {'delta'}
ewords = {'echo'}
fwords = {'foxtroth'}
gwords = {'golf'}
hwords = {'hotel'}

r=sr.Recognizer()
oneX=sr.AudioFile('XoneX.flac')
with oneX as source:
    audio=r.record(source)
    if oneX in aoneX in awords.keys():
        print('a')
    elif oneX in bwords.keys():
        print('b')
    elif oneX in cwords.keys():
        print('c')
    elif oneX in dwords.keys():
        print('d')
    elif oneX in ewords.keys():
        print('e')
    elif oneX in fwords.keys():
        print('f')
    elif oneX in gwords.keys():
        print('g')
    elif oneX in hwords.keys():
        print('h')
