class motocicleta:
    estado = "Nueva"
    motor = False
    
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        
    def arrancar(self):
        if self.motor == False:
            self.motor = True
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba en marcha")
            
    def detener(self):
        if self.motor == True:
            self.motor = False
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")
    
    def consultar_precio(self):
        saber_precio = input("Quiere saber el precio de la moto?(si/no): ")
        if saber_precio.lower() == "si":
            print(f"El precio de la motocicleta {self.marca}, {self.modelo} es de {self.precio}$.")

moto1 = motocicleta("azul", "AJH 134", 10, 2, "Yamaha", "FZ25A", "2/1/10", 140, 132)

moto2 = motocicleta("negro", "HER 764", 25, 2, "Honda", "F-25", "4/2/15", 110, 120)

print(f"""Moto 1:
color = {moto1.color}
matricula = {moto1.matricula}
combustible_litros = {moto1.combustible_litros}
numero_ruedas = {moto1.numero_ruedas}
marca = {moto1.marca}
modelo = {moto1.modelo}
fecha_fabricacion = {moto1.fecha_fabricacion}
velocidad_punta = {moto1.velocidad_punta}
peso = {moto1.peso}
-------------------------""")

print("Arrancar moto: ")
moto1.arrancar()
print("Arrancar moto: ")
moto1.arrancar()
print("Detener moto: ")
moto1.detener()
print("Detener moto: ")
moto1.detener()

print("")
moto1.precio = 1300000

moto1.consultar_precio()

mostrar_moto = input("""
Quieres ver la moto 2?(si/no): """)

if mostrar_moto.lower() == "si":
    print(f"""Moto 2:
color = {moto2.color}
matricula = {moto2.matricula}
combustible_litros = {moto2.combustible_litros}
numero_ruedas = {moto2.numero_ruedas}
marca = {moto2.marca}
modelo = {moto2.modelo}
fecha_fabricacion = {moto2.fecha_fabricacion}
velocidad_punta = {moto2.velocidad_punta}
peso = {moto2.peso}
-------------------------""")
    
    print("Arrancar moto: ")
    moto2.arrancar()
    print("Arrancar moto: ")
    moto2.arrancar()
    print("Detener moto: ")
    moto2.detener()
    print("Detener moto: ")
    moto2.detener()

    print("")
    moto2.precio = 950000

    moto2.consultar_precio()
else:
    print("Fin programa")

