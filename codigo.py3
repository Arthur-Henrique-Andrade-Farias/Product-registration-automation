import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write('chrome')

pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=739, y=537)

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
 
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=853, y=391)

pyautogui.write('pythonimpressonador@gmail.com')

pyautogui.click(x=888, y=485)

pyautogui.write('minha senha')

pyautogui.click(x=982, y=552)

time.sleep(2)

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    
    pyautogui.click(x=832, y=270)

    pyautogui.write(tabela.loc[linha, "codigo"])

    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, "marca"])

    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, "tipo"])

    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))

    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "obs"]))
    
    pyautogui.press('tab')
    
    pyautogui.press('enter')
    
    pyautogui.scroll(1000)

