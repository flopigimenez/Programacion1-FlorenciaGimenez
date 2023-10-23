"""1. Create a while loop with the following characteristics:
• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was
skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the 
loop was broken when x was ' + x.
• The console output should look like this: (IMAGEN)"""
#Ejercicio 1
x = 0
while x < 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print(f"Se saltó el valor {x} de x")
    elif x == 15:
        break
    else:
        print(x)
        
print(f"Se rompió la ejecución del bucle cuando x valía: {x}")