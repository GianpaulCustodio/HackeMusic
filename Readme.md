# 🎧 HackeMusic - Encriptador de archivos personales en música

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Crypto-AES_256-red?logo=lock&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

**HackeMusic** es una herramienta avanzada de esteganografía y criptografía diseñada para inyectar y ocultar archivos PDF dentro de pistas de audio MP3. 

Desarrollada para laboratorios de ciberseguridad, demostraciones de respuesta a incidentes (DFIR) y ejercicios de exfiltración de datos, esta herramienta combina el ocultamiento de datos ("File Binding") con una robusta capa de cifrado **AES (Fernet)**.

---

## Características Principales

* **Doble Interfaz:**
  * **Modo Interactivo UI:** Una interfaz de terminal de alto impacto visual con colores, paneles y barras de progreso fluidas.
  * **Modo CLI (Terminal):** Soporte completo para argumentos de línea de comandos (Flags), ideal para automatizar en scripts.
* **Cifrado de Grado Militar:** El payload (PDF) no solo se oculta, sino que se cifra usando AES de 256 bits con derivación de llaves PBKDF2HMAC.
* **Integridad del Archivo:** El archivo MP3 resultante es completamente funcional y se reproducirá con normalidad en cualquier reproductor multimedia estándar.
* **Portabilidad:** Posibilidad de compilarse en un ejecutable independiente (`.exe`) para ejecutar en entornos Windows sin dependencias.

---

## Instalación y Requisitos

### Opción 1: Para Desarrolladores / Analistas (Python)
Asegúrate de tener Python 3.8 o superior instalado.

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/HackeMusic.git](https://github.com/tu-usuario/HackeMusic.git)
   cd HackeMusic

```

2. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt

```



### Opción 2: Ejecutable para Windows (Usuarios Finales / Alumnos)

Si no deseas instalar Python, puedes descargar el binario precompilado.

1. Ve a la sección de **[Releases](https://www.google.com/search?q=%23)** *(Añadir link de release aquí)*.
2. Descarga `HackeMusic.exe`.
3. ¡Haz doble clic y úsalo directamente!

---

## Guía de Uso

Puedes ejecutar HackeMusic de dos formas, dependiendo de tu necesidad en el laboratorio.

### 1. Modo Interactivo (Recomendado para Demostraciones)

Simplemente ejecuta el script sin argumentos para desplegar el menú interactivo con estética visual avanzada.

```bash
python HackeMusic.py

```

*(Aquí te sugerimos añadir un GIF de unos 10 segundos mostrando la herramienta corriendo en la terminal)*

### 2. Modo Línea de Comandos (CLI)

Para usuarios avanzados o integración con otras herramientas.

**Ocultar y cifrar un PDF:**

```bash
python HackeMusic.py --hide -p reporte_secreto.pdf -m cancion.mp3 -k "SuperPassword123" -o cancion_modificada.mp3

```

**Extraer y descifrar el PDF:**

```bash
python HackeMusic.py --extract -m cancion_modificada.mp3 -k "SuperPassword123" -o reporte_recuperado.pdf

```

---

## Aviso Legal y Descargo de Responsabilidad

Esta herramienta ha sido creada estrictamente con **fines educativos y académicos**. Su uso está diseñado para estudiantes universitarios, investigadores de seguridad y profesionales en entornos de laboratorio controlados.

El autor no se hace responsable del uso indebido, ilegal o malicioso de este software. La exfiltración de datos no autorizada es un delito. Úsalo bajo tu propia responsabilidad.

---

**Desarrollado con 💻 por Gianpaul (HackeMate)** *Educación en Ciberseguridad & Hacking Ético*

```

```
