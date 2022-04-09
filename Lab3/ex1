import abc

class BaseItem():
    __metaclass__ = abc.ABCMeta

    #método estático para calcular tamanho ocupado pela caixa
    #não depende do objeto, vantagem implementar como estática

    @staticmethod
    def Volume_box(a, b, c):
        return a*b*c

    #método abstrato que devolverá as informações do Item vendido
    #todo item deverá possuir mas cada item tera informações
    #específicas

    @abc.abstractmethod 
    def get_infos(self):
        pass


class Notebook(BaseItem):

    def __init__(self, category, id, CPU, memory, storage, price, qtd, height, length, width, GPU = False):
        self.category = category
        self.id = id
        self.CPU = CPU
        self.memory = memory
        self.storage = storage
        self.price = price
        self.qtd = qtd
        self.height = height
        self.length = length
        self.width = width
        self.GPU = GPU

    def get_infos(self):
        print(f'\nCategory: {self.category}')
        print(f'id : {self.id}')
        print(f'CPU : {self.CPU}')
        print(f'memory : {self.memory}GB')
        print(f'storage : {self.storage}GB')
        
        if self.GPU:
            print(f'GPU: {self.GPU}')
        else:
            print(f'GPU: Integrated w/ CPU')

        print(f'price: R${self.price}')

        if self.qtd == 0:
            print(f'out of stock!')
        else:
            print(f'There are {self.qtd} in stock\n')

    def size_ocupped(self):
        print(f'the box dimensions: {self.height} x {self.length} x {self.width} = {self.Volume_box(self.height, self.length, self.width):.2f} m³')

    def sell(self):
        if self.qtd == 0:
            print(f'There are no Notebooks {self.id} avaliable in stock')
        else:
            print(f'Notebook {self.id} sold!')
            self.qtd = self.qtd - 1


class TV(BaseItem):
    def __init__(self, category, id, resolution, size, price, qtd, height, length, width):
        self.category = category
        self.id = id
        self.resolution = resolution
        self.size = size
        self.price = price
        self.qtd = qtd
        self.height = height
        self.length = length
        self.width = width

    def get_infos(self):
        print(f'\nCategory: {self.category}')
        print(f'id : {self.id}')
        print(f'resolution : {self.resolution}')
        print(f'size : {self.size} inches')
        print(f'price: R${self.price}')

        if self.qtd == 0:
            print(f'out of stock!')
        else:
            print(f'There are {self.qtd} in stock\n')

    def space_ocupped(self):
        print(f'the box dimensions: {self.height} x {self.length} x {self.width} = {self.Volume_box(self.height, self.length, self.width):.2f} m³')

    def sell(self):
        if self.qtd == 0:
            print(f'There are no Tv {self.id} avaliable in stock')
        else:
            print(f'Tv {self.id} sold!')
            self.qtd = self.qtd - 1
    
class Bed(BaseItem):
    def __init__(self, category, id, size, price, qtd, height, length, width):
        self.category = category
        self.id = id
        self.size = size
        self.price = price
        self.qtd = qtd
        self.height = height
        self.length = length
        self.width = width
    
    def get_infos(self):
        print(f'\nCategory: {self.category}')
        print(f'id : {self.id}')
        print(f'type : {self.size}')
        print(f'price: R${self.price}')

        if self.qtd == 0:
            print(f'out of stock!')
        else:
            print(f'There are {self.qtd} in stock\n')
    
    def space_ocupped(self):
        print(f'the box dimensions: {self.height} x {self.length} x {self.width} = {self.Volume_box(self.height, self.length, self.width):.2f} m³')

    def sell(self):
        if self.qtd == 0:
            print(f'There are no Bed {self.id} avaliable in stock')
        else:
            print(f'Bed {self.id} sold!')
            self.qtd = self.qtd - 1
    
    #método de classe, permite contruir novos objetos com parâmetros
    #da classe

    @classmethod
    def add_bed(cls, id, size, value, height = 0.8, length = 1.8, width = 0.8):
        return cls('Bedroom', id, size, value, 1, height, length, width)


n1 = Notebook('Eletronics', 'Acer aspire 5', 'Ryzen 5 5500U', 8, 512, 3500, 9, 0.3, 0.6, 0.5, GPU = False)
n2 = Notebook('Eletronics', 'Dell Inspirion 3000', 'Intel i5 10350U', 8, 256, 4000, 15, 0.3, 0.65, 0.5, GPU = False)
n3 = Notebook('Eletronics', 'Macbook air', 'M2', 32, 1024, 12000, 4, 0.1, 0.3, 0.2, GPU = True)
t1 = TV('Eletronics', 'Samsung 7 series', '4K UHD', 50, 2000, 9, 1, 1.5, 0.2)
b1 = Bed('Bedroom', 'Ortobom', 'single', 1200, 6, 0.80, 1.8, 0.8)
b2 = Bed.add_bed('EuroColchoes', 'single', 1600)
n1.get_infos()
n2.get_infos()
n3.get_infos()
t1.get_infos()
b1.get_infos()
b2.get_infos()

b1.sell()
n1.sell()
b1.sell()
b2.sell()
