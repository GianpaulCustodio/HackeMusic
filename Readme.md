# HackeMusicMenu

## Descripción

**HackeMusicMenu** es un programa interactivo que permite realizar las siguientes operaciones:

1. **Encriptar**: Ocultar un archivo PDF dentro de un archivo MP3.
2. **Decifrar**: Extraer un archivo PDF oculto dentro de un archivo MP3.
3. **Salir**: Finalizar el programa.

El programa solicita los nombres de los archivos necesarios y muestra mensajes según el proceso realizado.

---

## Requisitos

- Python 3.x
- Archivos PDF y MP3 válidos para realizar las operaciones.

---

## Funcionalidades

### 1. `print_logo()`
Muestra un logo ASCII en colores rojo y azul, junto con una leyenda de derechos reservados.

### 2. `embed_pdf_in_mp3(pdf_path, mp3_path, output_path)`
Oculta un archivo PDF dentro de un archivo MP3.

- **Parámetros**:
  - `pdf_path`: Ruta del archivo PDF a ocultar.
  - `mp3_path`: Ruta del archivo MP3 donde se ocultará el PDF.
  - `output_path`: Ruta del archivo MP3 resultante con el PDF incrustado.

- **Proceso**:
  - Lee los datos del archivo MP3 y PDF.
  - Agrega un marcador (`!@#PDF-EMBEDDED!@#`) para identificar la posición del PDF.
  - Escribe los datos combinados en el archivo de salida.

- **Errores**:
  - Si no se pueden leer o escribir los archivos, se muestra un mensaje de error.

### 3. `extract_pdf_from_mp3(mp3_path, output_path="extracted.pdf")`
Extrae un archivo PDF oculto dentro de un archivo MP3.

- **Parámetros**:
  - `mp3_path`: Ruta del archivo MP3 encriptado.
  - `output_path`: Ruta del archivo PDF extraído (por defecto: `extracted.pdf`).

- **Proceso**:
  - Busca el marcador (`!@#PDF-EMBEDDED!@#`) en el archivo MP3.
  - Extrae los datos del PDF a partir del marcador.
  - Escribe el PDF extraído en el archivo de salida.

- **Errores**:
  - Si no se encuentra el marcador o no se pueden leer/escribir los archivos, se muestra un mensaje de error.

### 4. `menu()`
Muestra un menú interactivo para que el usuario seleccione una de las opciones disponibles:

1. **Encriptar**: Solicita los nombres de los archivos PDF, MP3 y de salida, y llama a `embed_pdf_in_mp3`.
2. **Decifrar**: Solicita el nombre del archivo MP3 encriptado y el nombre del archivo PDF de salida, y llama a `extract_pdf_from_mp3`.
3. **Salir**: Finaliza el programa.

---

## Uso

1. Ejecuta el programa desde la terminal:
   ```bash
   python3 HackeMusic.py
2. Selecciona una opción del menú:
    1: Encriptar un PDF dentro de un MP3.
    2: Decifrar un PDF oculto en un MP3.
    3: Salir del programa.
3. Sigue las instrucciones en pantalla para proporcionar los nombres de los archivos necesarios.

## Ejemplo de uso
Encriptar un PDF en un MP3
1. Selecciona la opción 1 en el menú.
2. Ingresa los nombres de los archivos:
    PDF: documento.pdf
    MP3: cancion.mp3
    Salida: cancion_encriptada.mp3
3. El programa generará un archivo MP3 con el PDF oculto.

Decifrar un PDF de un MP3

1. Selecciona la opción 2 en el menú.
2. Ingresa los nombres de los archivos:
    MP3 encriptado: cancion_encriptada.mp3
    PDF extraído: documento_extraido.pdf
3. El programa extraerá el PDF y lo guardará en el archivo especificado.


## Notas
- El marcador utilizado para identificar el PDF oculto es !@#PDF-EMBEDDED!@#.
- Asegúrate de que los archivos proporcionados sean válidos y accesibles.
- Este programa es solo para fines educativos y no debe ser utilizado para actividades malintencionadas.
