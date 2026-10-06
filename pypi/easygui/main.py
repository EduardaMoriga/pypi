import sys

# Remove a pasta atual da busca do Python para carregar o pacote do pip
sys.path.pop(0) if sys.path[0] in ('', '.', sys.path[0]) else None

import easygui

# Seu código normal do EasyGUI abaixo:
easygui.msgbox("Agora sim funcionou!", "Sucesso")