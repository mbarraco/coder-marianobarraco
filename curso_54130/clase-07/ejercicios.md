# Ejercicios Básicos en `for` y `wile` Loops de Python

## `for`
1. Escribir un programa que calcule la suma de los primeros 10 enteros positivos.
   ```bash
   # Ejemplo
   - Entrada esperada: Ninguna
   - Salida esperada: 55
    ```
2. Escribir un programa que imprima los primeros 10 números impares.
   ```bash
   # Ejemplo
   - Entrada esperada: Ninguna
   - Salida esperada: 1 3 5 7 9 11 13 15 17 19
    ```
3. Escribir un programa que calcule el factorial de un número entero dado. Un factorial es el producto de todos los enteros positivos desde 1 hasta un número dado. Se representa con el signo de exclamación (!). Por ejemplo, el factorial de 5 se escribe como 5! y se calcula como 5 x 4 x 3 x 2 x 1 = 120.
   ```bash
   # Ejemplo
   - Entrada esperada: 5
   - Salida esperada: 120
    ```
4. Escribir un programa que tome como input del usuario un número y calcule la suma de todos los números pares menores al valor ingresado:
    ```bash
   # Ejemplo
    >> Ingresar número: 9
    >> La suma de los números pares menores a 9 es: 20
    ```

5. Escribir un programa que encuentre el elemento más grande en una lista de enteros dada.
   ```bash
   # Ejemplo
   - Entrada esperada: [5, 10, 2, 8, 3]
   - Salida esperada: 10
    ```

6. Escribir un programa que imprima un rectángulo de asteriscos de un ancho y alto dados.
   - Entrada esperada: ancho=4, alto=3
   - Salida esperada:
      ```
      ****
      ****
      ****
      ```

7. Escribir un programa que imprima un triángulo rectángulo de asteriscos de una altura dada.
   - Entrada esperada: alto=5
   - Salida esperada:
      ```
      *
      **
      ***
      ****
      *****
      ```

8. Escribir un programa que imprima la tabla de multiplicar para los números del 1 al 5.
   - Entrada esperada: Ninguna
   - Salida esperada:
      ```
       1  2  3  4  5
      --------------
      1|1  2  3  4  5
      2|2  4  6  8  10
      3|3  6  9  12 15
      4|4  8  12 16 20
      5|5  10 15 20 25
      ```


9. Escribir un programa que calcule e imprima la suma de todos los números entre 1 y 10, y la suma de sus cuadrados.
   - Entrada esperada: Ninguna
   - Salida esperada:
      ```
      La suma de los números es: 55
      La suma de los cuadrados es: 385
      ```

10. Escribir un programa que tome una lista de nombres y edades, y devuelva un diccionario que contenga solo los nombres de las personas que tienen 18 años o más.

    ```
    # Ejemplo
    - Entrada esperada: [("Alice", 25), ("Bob", 16), ("Charlie", 19)]
    - Salida esperada: {"Alice": 25, "Charlie": 19}
    ```
11. Escribir un programa que tome una cadena de texto y devuelva un diccionario que contenga la frecuencia de cada palabra en la cadena.

    ```
    # Ejemplo
    - Entrada esperada: "the quick brown fox jumps over the lazy dog"
    - Salida esperada: {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}
    ```
12. Escribir un programa que tome una lista de números y devuelva un diccionario que contenga la cantidad de números pares e impares en la lista.

    ```
    # Ejemplo
    - Entrada esperada: [1, 2, 3, 4, 5, 6]
    - Salida esperada: {"par": 3, "impar": 3}
    ```
13. Escribir un programa que tome una lista de enteros y devuelva un diccionario que contenga el máximo, mínimo y promedio de los números en la lista.

    ```
    # Ejemplo
    - Entrada esperada: [5, 10, 2, 8, 3]
    - Salida esperada: {"max": 10, "min": 2, "prom": 5.6}
    ```

## `while`
14. Imprime todos los números pares del 0 al 20 usando un bucle "while".

   ```
   Ejemplo
   - Ejemplo de salida: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
   ```
15. Imprime todos los números del 10 al 1 en orden descendente usando un bucle "while".

   ```
   Ejemplo
   - Ejemplo de salida: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
   ```

16. Pide al usuario que ingrese un número entero positivo y luego imprime todos los números impares del 0 hasta ese número en orden ascendente usando un bucle "while".

   ```
   Ejemplo
   - Ejemplo de salida (el usuario ingresa 4): 1, 3
   ```

17. Elije una contraseña. Pide al usuario que ingrese una contraseña y sigue pidiéndoles que ingresen una contraseña hasta que ingresen la contraseña que has elegido usando un bucle "while".


   ```
   Ejemplo: la contraseña es admin1234
   >> Ingrese la contraseña: password1234
   >> Contraseña incorrecta. Ingrese la contraseña: admin!
   >> Contraseña incorrecta. Ingrese la contraseña: admin1234
   >> Bienvenido usuario!

   ```

18. Modifica el ejercicio anterior para que el usuario tenga sólo 3 intentos fallidos.


   ```
   Ejemplo: la contraseña es admin1234
   >> Ingrese la contraseña: password1234
   >> Contraseña incorrecta. Ingrese la contraseña: admin!
   >> Contraseña incorrecta. Ingrese la contraseña: ADMIN1234
   >> Usuario bloqueado!

   ```

19. Modifica el ejercicio anterior para que se indiquen cuántos intentos restantes tiene el usuario.


   ```
   Ejemplo: la contraseña es admin1234
   >> Ingrese la contraseña (3 intentos restantes): password1234
   >> Contraseña incorrecta. Ingrese la contraseña (2 intentos restantes): admin!
   >> Contraseña incorrecta. Ingrese la contraseña (1 intentos restantes): ADMIN1234
   >> Usuario bloqueado!

   ```