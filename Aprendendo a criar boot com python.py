#!/usr/bin/env python
# coding: utf-8

# # Criar boot com Python

# Por meio do treinamento disponibilizado pela hastag programação, eu estou aprendendo a como criar boot utilizando a linguagem python.
# 
# Referência: https://www.youtube.com/watch?v=pZ6EqsHskM8
# Data: 07/01/24

# ## Boot no Computador- Pyautogui

# In[20]:


# importar pyautogui
import pyautogui

# pausa de 3 segundos para abrir o arquivo/programa/sistema
pyautogui.PAUSE=3


# In[34]:


# Abrir a ferramenta, sistema ou programa
pyautogui.press("win")
pyautogui.write ("login.xlsx") #escreve o que deve ser buscado na pesquisa
pyautogui.press ("backspace") #apaga uma letra da busca para que a pesquisa traga a planilha
pyautogui.press("Enter")

# Preencher login
pyautogui.click (x=494, y=313) #coloca a posição exibida na saída do comando pyautogui.position ()
pyautogui.write ("Juliana") #Escreve o nome que deve ser exibido no login

# Preenche a senha
pyautogui.click (x=501, y=365) #coloca a posição exibida na saída do comando pyautogui.position ()
pyautogui.write ("0912") #Escreve a senha


# Clicar em fazer login
pyautogui.click (x=443, y=386)


# In[35]:


#importando o time para que dê tempo abrir a tela de login e selecionar a posições
import time
time.sleep(3)
pyautogui.position () #mostra a posição do mouse, a saída deste comando deve ser inserida entre os () deste comando pyautogui.click


# ## Boot para internet
# ###Ferramenta utilizada- Selenium
# ###para instalar via prompt- pip install selenium
# 

# In[ ]:




