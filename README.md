# PascalCompilador
Realización de un compilador del lenguaje Pascal utilizando la librería de Python SLY.

Para ejecutar es necesario seguir el siguiente formato

python3 pascal.py [opcion] archivo [archivo]* <---- Para la ejecución en terminal unix

python pascal.py [opcion] archivo [archivo]* <---- Para ejecución en algún entorno de Python 3.6

Opciones:
La presente entrega contiene el analizador léxico y el analizador sintáctico. Se ejecuta de cualquiera de las siguientes maneras:

python3 pascal.py -l archivo [archivo]*
python3 pascal.py --lex archivo [archivo]*
Las anteriores opciones son para ver el resultado del análisis léxico

python3 pascal.py -p archivo [archivo]*
Esta opción es para ejecutar el análisis sintáctico y ver su resultado

Con la ejecución de ese comando y teniendo los correspondientes archivos de código en Pascal, el programa pascal.py mostrará todos los tokens de los códigos ingresados como parámetro a la ejecución.
