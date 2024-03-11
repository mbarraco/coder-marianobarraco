# Ejercicios sobre línea de comandos (Windows y Mac)
Recuerda que siempre es importante tener precaución al manipular archivos y directorios, ya que los cambios realizados son permanentes y no se pueden deshacer fácilmente. Practica estos ejercicios con cuidado y asegúrate de comprender completamente las acciones que estás realizando.
## Windows

1. Navegación de directorios:
   - Navega al directorio raíz del sistema usando el comando `cd \` (barra invertida).
   - Navega a tu directorio de usuario usando `cd %userprofile%`.
   - Navega a un directorio específico utilizando la ruta completa, por ejemplo, `cd C:\Ruta\Hacia\Directorio`.

2. Creación de archivos:
   - Crea un archivo de texto vacío usando el comando `echo. > MiArchivo.txt`.
   - Verifica la creación del archivo utilizando `dir` para mostrar la lista de archivos en el directorio actual.

3. Copia de archivos:
   - Crea una copia de un archivo existente usando el comando `copy Ruta\Del\Archivo\Original.txt Ruta\De\Destino\Copia.txt`.
   - Verifica que la copia se haya realizado correctamente usando `dir` para listar los archivos en el directorio de destino.

4. Movimiento y renombrado de archivos:
   - Mueve un archivo a otro directorio utilizando `move Ruta\Del\Archivo.txt Ruta\De\Destino\Archivo.txt`.
   - Cambia el nombre de un archivo usando `ren Ruta\Del\Archivo.txt NuevoNombre.txt`.

5. Creación de directorios:
   - Crea un nuevo directorio usando el comando `mkdir NuevoDirectorio`.
   - Verifica la creación del directorio utilizando `dir` para mostrar la lista de archivos y directorios en el directorio actual.

6. Borrado de archivos:
   - Borra un archivo usando el comando `del Ruta\Del\Archivo.txt`.
   - Confirma la eliminación del archivo utilizando `dir` para verificar que el archivo ya no esté presente.

7. Borrado de directorios:
   - Borra un directorio vacío utilizando `rmdir DirectorioVacio`.
   - Borra un directorio y todos sus archivos y subdirectorios utilizando `rmdir /s DirectorioCompleto` (ten cuidado al utilizar esta opción, ya que eliminará todo el contenido del directorio).

## Mac

1. Navegación de directorios:
   - Navega al directorio raíz del sistema usando el comando `cd /`.
   - Navega a tu directorio de usuario usando `cd ~`.
   - Navega a un directorio específico utilizando `cd /ruta/hacia/directorio`.

2. Creación de archivos:
   - Crea un archivo de texto vacío usando el comando `touch MiArchivo.txt`.
   - Verifica la creación del archivo utilizando `ls` para mostrar la lista de archivos en el directorio actual.

3. Copia de archivos:
   - Crea una copia de un archivo existente usando el comando `cp Ruta/Del/Archivo/Original.txt Ruta/De/Destino/Copia.txt`.
   - Verifica que la copia se haya realizado correctamente utilizando `ls` para listar los archivos en el directorio de destino.

4. Movimiento y renombrado de archivos:
   - Mueve un archivo a otro directorio utilizando `mv Ruta/Del/Archivo.txt Ruta/De/Destino/Archivo.txt`.
   - Cambia el nombre de un archivo usando `mv Ruta/Del/Archivo.txt NuevoNombre.txt`.

5. Creación de directorios:
   - Crea un nuevo directorio usando el comando `mkdir NuevoDirectorio`.
   - Verifica la creación del directorio utilizando `ls` para mostrar la lista de archivos y directorios en el directorio actual.

6. Borrado de archivos:
   - Borra un archivo usando el comando `rm Ruta/Del/Archivo.txt`.
   - Confirma la eliminación del archivo utilizando `ls` para verificar que el archivo ya no esté presente.

7. Borrado de directorios:
   - Borra un directorio vacío utilizando `rmdir DirectorioVacio`.
   - Borra un directorio y todos sus archivos y subdirectorios utilizando `rm -rf DirectorioCompleto` (ten cuidado al utilizar esta opción, ya que eliminará todo el contenido del directorio).
