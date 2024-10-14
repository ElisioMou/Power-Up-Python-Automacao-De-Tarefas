# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# pyautogui.PAUSE = 0.3

import pyautogui
import time

# Passo 1: Entrar no sistema da TIM: https://meutim.tim.com.br/
# abrir o menu do Windows

pyautogui.press("win")
time.sleep(3)
# digitar o navegador (chrome)
pyautogui.write("chrome")
#clicando para abrir nova janela
time.sleep(3)
pyautogui.click(x=841, y=610)
time.sleep(3)

pyautogui.hotkey('win','up')

time.sleep(7)
# acessar no link da TIM 
pyautogui.write("https://meutim.tim.com.br/")
time.sleep(2)
pyautogui.press("enter")
time.sleep(4)

# Passo 2: Fazer login
pyautogui.click(x=78, y=404) # click no campo numero do celular
time.sleep(2)
pyautogui.write("34992648587") # preenhttps://meutim.tim.com.br/


pyautogui.press("tab") # passa para o próximo campo
pyautogui.write("4545")
time.sleep(2)

# click no botão 'Entrar agora'
pyautogui.click(x=224, y=597)

# Passo 3: Carregar fatura da TIM
pyautogui.click(x=904, y=153) # click no menu Minhas Contas
time.sleep(2)
pyautogui.click(x=135, y=216) # click na opcao Conta Online
time.sleep(5)
# pyautogui.moveTo(474, 823)
# scroll para baixo em 10 "clicks"
pyautogui.press("down", 11)
time.sleep(3)

pyautogui.click(x=479, y=863) # click na opcao baixar PDF
time.sleep(5)
pyautogui.click(x=1183, y=66) # click em Downloads
time.sleep(1)
pyautogui.click(x=1183, y=66) # click em Downloads
time.sleep(1)
pyautogui.click(x=1016, y=158) # click em fatura.pdf
time.sleep(4)
pyautogui.click(x=908, y=1003)
time.sleep(1)
pyautogui.press("enter")