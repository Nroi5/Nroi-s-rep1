import os
import pygame
from pygame import mixer #воспроизвести
from gtts import gTTS #озвучить текст
f=open('voice.txt', 'r',encoding='UTF-8')

voice_txt=f.read()

f.close()

mixer.init()
mp3='text_sound.mp3'
tts=gTTS(text=voice_txt, lang='ru')
tts.save(mp3)

mixer.music.load(mp3)
mixer.music.play()
while mixer.music.get_busy(): #для запуска файла
    pygame.time.Clock().tick(10)
mixer.quit()


os.remove(mp3)


# with open (r'file.txt', 'r') as f:  самозакрывающийся файл
#     f.read()

# import pyaudio 
# import speech_recognition as sr
# from random import *
# r=sr.Recognizer()
# while True:
#     with sr.Microphone(device_index=1) as source:
#         print('Скажи что-нибудь')
#         audio=r.listen(source)

#     speech=r.recognize_google(audio,language='ru_RU').lower()

#     print('вы сказали: ', speech)

#     if speech == 'тумба':
#         list_frase=['юмба', 'табуретка', 'сам такой']
#         print(choice(list_frase))
#         break
#     elif speech == 'йоу':
#         print('чумба')
#         break
#     else:
#         print('Ты чего городишь?')
    


# import datetime 
# today=datetime.datetime.today()