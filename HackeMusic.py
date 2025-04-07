#!/usr/bin/env python3
"""
HackeMusicMenu.py

Menú interactivo para:
1. Encriptar (ocultar un archivo PDF dentro de un MP3)
2. Decifrar (extraer un PDF oculto en un MP3)
3. Salir

El programa solicita los nombres de los archivos y muestra mensajes según el proceso realizado.
"""

def print_logo():
    # Códigos ANSI para colores
    red_color = "\033[91m"   # rojo
    blue_color = "\033[94m"  # azul
    reset_color = "\033[0m"  # reiniciar color

    # Definir las líneas del logo en rojo
    red_lines = [
        "▗▖ ▗▖▗▞▀▜▌▗▞▀▘█  ▄ ▗▞▀▚▖",
        "▐▌ ▐▌▝▚▄▟▌▝▚▄▖█▄▀  ▐▛▀▀▘",
        "▐▛▀▜▌         █ ▀▄ ▝▚▄▄▖",
        "▐▌ ▐▌         █  █      "
    ]

    # Definir las líneas del logo en azul
    blue_lines = [
        "▗▖  ▗▖█  ▐▌ ▄▄▄ ▄ ▗▞▀▘",
        "▐▛▚▞▜▌▀▄▄▞▘▀▄▄  ▄ ▝▚▄▖",
        "▐▌  ▐▌     ▄▄▄▀ █     ",
        "▐▌  ▐▌          █     "
    ]

    # Combinar línea a línea, mostrando la parte roja y la azul juntos.
    for r_line, b_line in zip(red_lines, blue_lines):
        print(red_color + r_line + reset_color + " " + blue_color + b_line + reset_color)
    
    # Mostrar la leyenda en letras rojas debajo del logo.
    print(red_color + "\nBy HackeMate 2025 © Todos los derechos reservados" + reset_color)

def embed_pdf_in_mp3(pdf_path, mp3_path, output_path):
    try:
        with open(mp3_path, "rb") as f:
            mp3_data = f.read()
    except Exception as e:
        print(f"Error al leer el archivo MP3 ({mp3_path}): {e}")
        return
    
    try:
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()
    except Exception as e:
        print(f"Error al leer el archivo PDF ({pdf_path}): {e}")
        return
    
    marker = b'!@#PDF-EMBEDDED!@#'
    
    try:
        with open(output_path, "wb") as f:
            f.write(mp3_data)
            f.write(marker)
            f.write(pdf_data)
        print(f"\nEl archivo encriptado ha sido creado exitosamente: {output_path}")
    except Exception as e:
        print(f"Error al escribir el archivo encriptado ({output_path}): {e}")

def extract_pdf_from_mp3(mp3_path, output_path="extracted.pdf"):
    try:
        with open(mp3_path, "rb") as f:
            data = f.read()
    except Exception as e:
        print(f"Error al leer el archivo MP3 ({mp3_path}): {e}")
        return
    
    marker = b'!@#PDF-EMBEDDED!@#'
    marker_index = data.find(marker)
    if marker_index == -1:
        print("No se encontró un marcador válido en el archivo. Asegúrate de que el MP3 contenga un PDF oculto.")
        return
    
    pdf_data = data[marker_index + len(marker):]
    
    try:
        with open(output_path, "wb") as f:
            f.write(pdf_data)
        print(f"\nEl archivo PDF ha sido extraído exitosamente: {output_path}")
    except Exception as e:
        print(f"Error al escribir el archivo PDF extraído ({output_path}): {e}")

def menu():
    print_logo()
    while True:
        print("\nMenú:")
        print("1. Encriptar (ocultar PDF en MP3)")
        print("2. Decifrar (extraer PDF de MP3)")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            pdf_path = input("Ingrese el nombre del archivo PDF a ocultar (ej.: paper.pdf): ")
            mp3_path = input("Ingrese el nombre del archivo MP3 (ej.: music.mp3): ")
            output_path = input("Ingrese el nombre del archivo de salida (ej.: musicencrypt.mp3): ")
            embed_pdf_in_mp3(pdf_path, mp3_path, output_path)
        elif opcion == "2":
            mp3_path = input("Ingrese el nombre del archivo MP3 encriptado (ej.: musicencrypt.mp3): ")
            output_path = input("Ingrese el nombre del archivo PDF extraído (ej.: extracted.pdf) [Presione Enter para usar 'extracted.pdf']: ")
            if output_path.strip() == "":
                output_path = "extracted.pdf"
            extract_pdf_from_mp3(mp3_path, output_path)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()