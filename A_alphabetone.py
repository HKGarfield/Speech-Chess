import speech_recognition as sr

words = {'a':"Alpha",'b':"Beta",'c':"Charlie",'d':"Delta",'e':"Echo",'f':"Foxtroth",'g':"golf",'h':"Hotel"}


r=sr.Recognizer()
alphabetoneX=sr.AudioFile('XalphabetoneX.flac')
with alphabetoneX as source:
    audio=r.record(source)

awords='alpha'
bwords = {'b':"Beta"}
cwords = {'c':"Charlie"}
dwords = {'d':"Delta"}
ewords = {'e':"Echo"}
fwords = {'f':"Foxtroth"}
gwords = {'g':"Golf"}
hwords = {'h':"Hotel"}

if awords == r.recognize_google(audio):
    print('a')
elif r.recognize_google(audio) in bwords:
    print('b')
elif r.recognize_google(audio) in cwords:
    print('c')
elif r.recognize_google(audio) in dwords:
    print('d')
elif r.recognize_google(audio) in ewords:
    print('e')
elif r.recognize_google(audio) in fwords:
    print('f')
elif r.recognize_google(audio) in gwords:
    print('g')
elif r.recognize_google(audio) in hwords:
    print('h')
else:
    print('What the duck? Seems you said ' + r.recognize_google(audio))
