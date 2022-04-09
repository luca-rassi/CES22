class SerVivo:
    def __init__(self):
        print('Sou um Ser vivo')

class Bipede(SerVivo):
    def __init__(self):
        super().__init__()
        print('Sou um Bipede')

class Inteligente(SerVivo):
    def __init__(self):
        super().__init__()
        print('Sou inteligente')    

class Humano(Bipede, Inteligente):
    def __init__(self):
        super().__init__()
        print('Sou um humano')  
        
print('\nHumano:')
h = Humano()
print('\nBipede:')
b = Bipede()
print('\nInteligente:')
b = Inteligente()
print('\nSer vivo')
b = SerVivo()




