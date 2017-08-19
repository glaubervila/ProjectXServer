# Importa por default os settings de development caso nao haja arquivo de local.py
try:
    from server.settings.local import *
except:
    from server.settings.development import *
