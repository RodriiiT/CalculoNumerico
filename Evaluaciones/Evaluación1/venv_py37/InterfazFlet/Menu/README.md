# Evaluacion 1

La evaluación 1 consiste en realizar una interfaz en Python utilizando la librería de Flet en la cual
tiene un menú en donde podrá ir a una página llamada "Conversor" la cual convierte un valor de un
sistema númerico a otro, también, hay una página llamada "Seidel" en la cual podrá realizar un Gauss-Seidel
dandole valores una Matriz A y a un Vector B para obtener el valor del Vector X.

Para correr la interfaz tendrá que tener instalada la librería de flet, la puede instalar de la siguiente forma:

```
pip install flet
```

Adcionalmente, también es necesario que tenga numpy instalado, para instalarlo:

```
pip install numpy
```

Por último cabe recalcar que la interfaz se realizó en un entorno virtual, para crear e iniciar un entorno virtual
deberá realizar los siguientes pasos en la terminal:

Paso 1: Instalar el entorno virtual

```
pip install virtualenv
```

Paso 2: Crear el entorno virtual

```
python -m venv venv_py37
```

Paso 3: Deberá accder a la carpeta \Scripts para activar el entorno

```
cd venv_py37\Scripts
```

Paso 4: Tendrá que dar permisos en la terminal antes de activar el entorno

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Paso 5: Active el entorno desde la carpeta \Scripts

```
activate
```

Para desactivar el entorno:

```
deactivate
```

Una vez descargada las librerías podrá correr la interfaz de la siguiente manera:

```
flet run main.py
```

En caso de error asegurese que está la carpeta correcta, para accedar a una carpeta escriba el siguiente comando:

```
cd [NombreCarpeta]
```

Para salir de una carpeta escriba el siguiente comando:

```
cd..
```

Si desea ejecutar la interfaz en formato Web escriba el siguiente comando en terminal:

```
flet run --web main.py
```