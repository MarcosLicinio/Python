import pyautogui
import time
import pandas as pd


with open("CNPJ.txt", "r") as listacnpj:
    cnpj = listacnpj.readlines()

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Bloco de Notas")
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("win")
time.sleep(1)
pyautogui.write("Crhome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("win", "UP")
pyautogui.write("https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp")
pyautogui.press("enter")

for linha in cnpj:
    print(linha)
    time.sleep(5)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.write(linha)
    time.sleep(1)
    pyautogui.click(x=1187, y=529)
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.click(x=444, y=634)
    pyautogui.doubleClick(x=444, y=634)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    print("Copiando a razão social")
    pyautogui.hotkey("alt", "tab")
    time.sleep(2)
    print("Mudando de aba")
    pyautogui.write("A nome da empresa do CNPJ: ")
    time.sleep(1)
    print("Escrevendo")
    pyautogui.write(linha)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    print("Escrevendo o que copiou")
    pyautogui.press("enter")
    print("Apertando enter")
    time.sleep(1)
    pyautogui.hotkey("alt", "tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    print("Volta e cola o proximo CNPJ da lista")







