# Passo a passo do projeto 
# Passo 1: Entrar no sitema da empresa 
  # link a ser colocado que vai ser usado no processo
  #pip install pyautogui
import pyautogui
import time 
import pandas


pyautogui.PAUSE=0.5
pyautogui.click #clicar em algo
pyautogui.write #escrever um texto
pyautogui.press #pressionar 1 tecla do teclado

#pyautogui.press -> clica em algum lugar da tela
#pyautogui.write -> escreve um texto
#pyautogui.click - > pressionar 1 tecla do teclado

#pyautogui.hoykey ("ctrl", "v")

#abrir o navegador padrão do seu pc
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

link = ""
pyautogui.write(link)
pyautogui.press("enter")
 
#dar um pausa um pouco maior (3 segundos)
time.sleep(3)


#Passo 1: fazer login
pyautogui.click(x=714, y=465 ) 

#clicar no botão de logar
pyautogui.click(x=952, y=689)
time.sleep(3)

#passo 2: Importar a base de dados 
#pip install pandas
import pandas
tabela = pandas.read_csv("produtos(2).csv")
print(tabela)


#passo 3: Cadastrar 1 produto
#para cada linha do produto
for linha in tabela.index:
  # clicar no 1° campo
  pyautogui.click(x=709, y=319)
  #codigo do produto
  codigo =tabela.loc [linha, "codigo"]
  pyautogui.write("Codigo do Produto")
  pyautogui.press("tab")

  #marca
  pyautogui.write(tabela.loc[linha, "marca"])
  pyautogui.press("tab")

  #tipo
  pyautogui.write(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")

  #categoria
  pyautogui.write(tabela.loc[linha,"categoria"])
  pyautogui.press("tab")

  #preço
  pyautogui.write(tabela.loc[linha,"preco_unitario"])
  pyautogui.press("tab")

  #custo
  pyautogui.write(tabela.loc[linha,"preco_unitario"])
  pyautogui.press("tab")

  #obs
  obs = tabela.loc[linha,"obs"]
  if not pandas.isna(obs):
   pyautogui.write(tabela.loc[linha, "obs"])
  pyautogui.press("tab")

  #eviar
pyautogui.press("enter")
pyautogui.scroll(5000)

#passo 4: Repetir o processo de cadastro até acabar a base de dados