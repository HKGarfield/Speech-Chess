#!/bin/bash

import speech_recognition as sr
import subprocess
import sys
import os

r=sr.Recognizer()
oneX=sr.AudioFile('XalphabetoneX.flac')
with oneX as source:
    audio=r.record(source)

A1='akita'
A2='akhita'
A3='Akita'
A4='akitah'
B1='bees'
B2='pees'
B3='piece'
B4='Bees'
C1='kit'
C2='kat'
C3='Cat'
C4='cat'
D1='Dog'
D2='dog'
D3='doc'
D4='dogue'
E1='Elephant'
E2='Elephants'
E3='elephant'
E4='elephants'
F1='Fucks'
F2='Fox'
F3='fox'
F4='foxs'
G1='Grizzly'
G2='grizzly'
G3='gold'
G4='grizzley'
H1='Horse'
H2='horse'
H3='hydrogen'
H4='hoarse'

if  A1 == r.recognize_google(audio):
    print('a')
elif A2 == r.recognize_google(audio):           
    print('a')
elif A3 == r.recognize_google(audio):
    print('a')
elif A4 == r.recognize_google(audio):
    print('a')
elif B1 == r.recognize_google(audio):
    print('b')
elif B2 == r.recognize_google(audio):
    print('b')
elif B3 == r.recognize_google(audio):
    print('b')
elif B4 == r.recognize_google(audio):
    print('b')
elif C1 == r.recognize_google(audio):
    print('c')
elif C2 == r.recognize_google(audio):
    print('c')
elif C3 == r.recognize_google(audio):
    print('c')
elif C4 == r.recognize_google(audio):
    print('c')
elif D1 == r.recognize_google(audio):
    print('d')
elif D2 == r.recognize_google(audio):
    print('d')
elif D3 == r.recognize_google(audio):
    print('d')
elif D4 == r.recognize_google(audio):
    print('d')
elif E1 == r.recognize_google(audio):
    print('e')
elif E2 == r.recognize_google(audio):
    print('e')
elif E3 == r.recognize_google(audio):
    print('e')
elif E4 == r.recognize_google(audio):
    print('e')
elif F1 == r.recognize_google(audio):
    print('f')
elif F2 == r.recognize_google(audio):
    print('f')
elif F3 == r.recognize_google(audio):
    print('f')
elif F4 == r.recognize_google(audio):
    print('f')
elif G1 == r.recognize_google(audio):
    print('g')
elif G2 == r.recognize_google(audio):
    print('g')
elif G3 == r.recognize_google(audio):
    print('g')
elif G4 == r.recognize_google(audio):
    print('g')
elif H1 == r.recognize_google(audio):
    print('h')
elif H2 == r.recognize_google(audio):
    print('h')
elif H3 == r.recognize_google(audio):
    print('h')
elif H4 == r.recognize_google(audio):
    print('h')
else:
    print('What the Duck? It seems you said ' + r.recognize_google(audio)+'!')
