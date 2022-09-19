#IMPORTS
import subprocess
import sys

# install function, so its not necessary to install from cmds
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
to_install = ['pandas','pywhatkit','pyautogui','openpyxl']
for i in to_install:
    try:
        install(i)
    except:
        pass
    
# IMPORTS
import pandas as pd
import pywhatkit
from time import sleep
import pyautogui
from tkinter import *

# DATAFRAME
df = pd.read_excel('receptores.xlsx', header=None)

# ORDENAR POR TIEMPO DE SLEEP
tiempos = df[4]

#func
def get_sec(time_str):
    d, h, m, s = time_str.split(':')
    return int(d) * 86400 + int(h) * 3600 + int(m) * 60 + int(s)

tiempos_en_segundos = [get_sec(t) for t in tiempos]
df[4] = tiempos_en_segundos
df.sort_values(4, inplace=True, ignore_index=True)

tiempos_limpio = []
tiempos_limpio.append(df[4][0])
for i in df[4][1:]:
    tiempos_limpio.append(i - sum(tiempos_limpio))

df[5] = tiempos_limpio

# DATA
primer_sleep = 10
names = df[0]
phones = df[1]
texts = df[2]
images = df[3]
tiempos = df[5]

wait_time = 32

# WARNING
print(f'\n\n\nWARNING: THIS WILL TAKE {round(((len(names)*wait_time+len(names)+len([i for i in images if i == i])*wait_time+primer_sleep+sum(tiempos))/60),2)} MINUTES, PLEASE DONT USE PC UNTIL THEN\n\n\n')
sleep(primer_sleep)

# FUNCTION
def send_message(name, phone_number, text, image, pos):
    text = text.replace('RECEPTOR_WP',name)
    pywhatkit.sendwhatmsg_instantly(phone_number, text, wait_time)
    # pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2)
    # pyautogui.click()
    pyautogui.click(1050, 950)
    pyautogui.press('enter')
    if image == image:
        image = 'imagenes/'+image
        pywhatkit.sendwhats_image(phone_number, image)
        sleep(1)
        pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[0]/2)
        pyautogui.click()
        pyautogui.press('enter')

# ITERATION
for i in range(len(df)):
    sleep(tiempos[i])
    send_message(names[i], phones[i], texts[i], images[i], i)