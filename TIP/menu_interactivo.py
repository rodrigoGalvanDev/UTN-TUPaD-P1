class Nodos:
    def __init__(self, name, action=None):
        self.name = name                  # Nombre del menú u opción
        self.action = action              # Función a ejecutar (si es hoja)
        self.children = []                # Subopciones
        self.parent = None                # Para retroceder

    def add_child(self, child_node):
        ##child_node.parent = self
        self.children.append(child_node)

    def is_leaf(self):
        return len(self.children) == 0


menu_principal = Nodos("Menu Principal")
submenu_consulta = Nodos("1_ Consulta de saldo")
submenu_retiro = Nodos("2_ Retiro de efectivo")
submenu_depositos = Nodos("3_ Depositos")
submenu_transferencias = Nodos("4_ Transferencias")
submenu_cambiar_clave = Nodos("5_ Cambiar de clave")

opcion_consulta_cc = Nodos("1_ Consultar saldo cuenta corriente", 'Su saldo es de 133928 pesos')
opcion_consulta_ca = Nodos("2_ Consultar saldo cuenta ahorro", 'Su saldo es de 900 pesos')
opcion_retiro_20 = Nodos("1_ Retirar 20 mil pesos", "Se ha retirado con exito 20 mil pesos")
opcion_retiro_monto = Nodos("2_ Retirar un monto en especifico", "Ingrese el monto a retirar: ")
opcion_deposito_efectivo = Nodos("1_ Depositar en efectivo", "Ingrese los billetes por el cajero por favor.")
opcion_deposito_sobre = Nodos("2_ Depositar en sobre", "Ingrese el sobre por el cajero por favor.")
opcion_transferencia_alias = Nodos("1_ Transferir a un alias", "Ingrese el alias: ")
opcion_transferencia_CBU = Nodos("2_ Transferir a un CBU/CVU", "Ingrese el CBU/CVU: ")
opcion_cambiar_clave_cajero = Nodos("1_Cambiar clave del cajero automatico", "Ingrese la nueva clave:")
opcion_cambiar_clave_hb = Nodos("2_Cambiar clave del home banking", "Ingrese la nueva clave del home banking: ")

menu_principal.add_child(submenu_consulta)
menu_principal.add_child(submenu_retiro)
menu_principal.add_child(submenu_depositos)
menu_principal.add_child(submenu_transferencias)
menu_principal.add_child(submenu_cambiar_clave)

submenu_consulta.add_child(opcion_consulta_cc)
submenu_consulta.add_child(opcion_consulta_ca)

submenu_retiro.add_child(opcion_retiro_20)
submenu_retiro.add_child(opcion_retiro_monto)

submenu_depositos.add_child(opcion_deposito_efectivo)
submenu_depositos.add_child(opcion_deposito_sobre)



print(f'Bienvenido al banco:\n {menu_principal.children[0].name} \n {menu_principal.children[1].name} \n {menu_principal.children[2].name} \n {menu_principal.children[3].name} \n {menu_principal.children[4].name}')

eleccion = input("Por favor, elige una opcion:")

if(eleccion == "1"):
    eleccion = input(f'{submenu_consulta.children[0].name}\n{submenu_consulta.children[1].name}\nPor favor, elige una opcion: ')
    if(eleccion == "1"):
        print(opcion_consulta_cc.action)



