# Encrypt PDF - Python Script

## Descripción
Este proyecto es un script en Python que utiliza la biblioteca [PyPDF2](https://pypi.org/project/PyPDF2/) para cifrar archivos PDF. El script permite proteger documentos PDF con una contraseña, asegurando que solo las personas con la clave correcta puedan acceder a su contenido.

## Características
- Lee un archivo PDF existente.
- Cifra el archivo con una contraseña.
- Guarda el archivo PDF cifrado en una ubicación especificada.

## Requisitos
Antes de ejecutar el script, asegúrese de que tiene instalado lo siguiente:

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/)
- Biblioteca PyPDF2

## Instalación
1. Instalar pip (si no está instalado):
   ```bash
   python get-pip.py
   ```
2. Instalar la biblioteca PyPDF2:
   ```bash
   pip install PyPDF2
   ```

## Uso
1. Cambie la ruta `input_pdf_path` en el archivo `encrypt_pdf.py` a la ubicación de su archivo PDF original:
   ```python
   input_pdf_path = 'ruta/a/su/archivo.pdf'
   ```

2. Cambie la variable `password` para establecer la contraseña deseada:
   ```python
   password = 'su_contraseña'
   ```

3. Ejecute el script desde la línea de comandos:
   ```bash
   python encrypt_pdf.py
   ```

El archivo PDF cifrado se guardará en la ruta especificada en `output_pdf_path`.

## Cómo Funciona
1. El script utiliza `PdfReader` para leer el archivo PDF original.
2. Usa `PdfWriter` para crear un nuevo archivo PDF cifrado.
3. Copia todas las páginas del PDF original al nuevo archivo.
4. Establece una contraseña de usuario para proteger el archivo.
5. Guarda el archivo PDF cifrado.

## Ejemplo de Ejecución
Supongamos que tiene un archivo `documento.pdf` en su carpeta de descargas. Modifique el script para que quede así:
```python
input_pdf_path = 'C:\\Users\\Usuario\\Downloads\\documento.pdf'
output_pdf_path = 'C:\\Users\\Usuario\\Downloads\\documento_encriptado.pdf'
password = 'mi_contraseña_segura'
```
Luego, ejecute el script y obtendrá el archivo `documento_encriptado.pdf` cifrado.

## Contribuciones
Este repositorio está configurado para ser de solo lectura. Si desea contribuir, puede bifurcar el proyecto y realizar cambios en su propia copia.

## Licencia
Este proyecto está disponible bajo la licencia MIT. Consulte el archivo `LICENSE` para más detalles.

## Contacto
Si tiene preguntas o sugerencias, puede abrir un [issue](https://github.com/) o contactarme directamente.

