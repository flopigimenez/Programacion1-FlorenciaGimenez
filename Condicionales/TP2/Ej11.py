"""11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes 
para cada tipo de pizza aparecen a continuación.
•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un 
ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por 
pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""
#Ejercicio 11
pizza_vegetarian = input("Pizzería Bella Napoli. \n¿Quiere una pizza vegetariana(si/no)?")

if pizza_vegetarian.lower() == "si":
    ingredient = input("• Ingredientes vegetarianos: Pimiento y tofu. \nElija un ingrediente: ")
elif pizza_vegetarian.lower() == "no":
    ingredient = input("• Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. \nElija un ingrediente: ")

print(f"La pizza elegida {pizza_vegetarian} es vegetariana \nIngredientes elejidos: mozzarella, tomate y {ingredient}")