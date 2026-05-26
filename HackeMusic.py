#!/usr/bin/env python3
"""
HackeMusic.py - Advanced Steganography & Crypto Tool
By HackeMate © 2026

Permite inyectar y extraer archivos PDF dentro de archivos MP3, 
añadiendo una capa de cifrado AES (Fernet) para máxima seguridad.
"""

import os
import sys
import time
import argparse
import base64
from pathlib import Path

# Dependencias externas
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt, IntPrompt
from rich.text import Text

console = Console()

# Marcador único y robusto
MARKER = b'!@#HACKEMATE-SECURE-V1!@#'

def print_logo():
    logo = """[bold bright_red]▗▖ ▗▖▗▞▀▜▌▗▞▀▘█  ▄ ▗▞▀▚▖  [bold bright_cyan]▗▖  ▗▖█  ▐▌ ▄▄▄ ▄ ▗▞▀▘
[bold bright_red]▐▌ ▐▌▝▚▄▟▌▝▚▄▖█▄▀  ▐▛▀▀▘  [bold bright_cyan]▐▛▚▞▜▌▀▄▄▞▘▀▄▄  ▄ ▝▚▄▖
[bold bright_red]▐▛▀▜▌         █ ▀▄ ▝▚▄▄▖  [bold bright_cyan]▐▌  ▐▌     ▄▄▄▀ █     
[bold bright_red]▐▌ ▐▌         █  █        [bold bright_cyan]▐▌  ▐▌         █      [/]"""
    
    panel = Panel(
        logo, 
        title="[bold bright_yellow]HackeMusic - Advanced Payload Binder[/]", 
        subtitle="[bold bright_red]By HackeMate © Todos los derechos reservados[/]",
        border_style="bright_blue",
        expand=False
    )
    console.print(panel)

def generate_key(password: str, salt: bytes) -> bytes:
    """Deriva una llave segura de 32 bytes a partir de la contraseña."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000, # Alto número de iteraciones para evitar fuerza bruta
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def validate_files(files_to_check, check_size=False):
    """Valida que los archivos existan y opcionalmente revisa su peso."""
    for file_path in files_to_check:
        path = Path(file_path)
        if not path.is_file():
            console.print(f"[bold red]❌ Error:[/] El archivo [bright_yellow]{file_path}[/] no existe.")
            return False
    return True

def embed_pdf(pdf_path, mp3_path, output_path, password, is_cli=False):
    if not validate_files([pdf_path, mp3_path]):
        return

    # Advertencia si el PDF es sospechosamente grande
    if os.path.getsize(pdf_path) > os.path.getsize(mp3_path):
        console.print("[bold bright_yellow]⚠️ Advertencia:[/] El PDF es más pesado que el MP3. Esto podría ser detectado fácilmente en un análisis forense.")

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=40, style="bright_cyan", complete_style="bright_red"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
            disable=is_cli # Oculta la barra si se corre desde CLI para scripts limpios
        ) as progress:
            
            task = progress.add_task("[bright_cyan]Leyendo archivos base...", total=100)
            
            with open(mp3_path, "rb") as f:
                mp3_data = f.read()
            with open(pdf_path, "rb") as f:
                pdf_data = f.read()
            progress.update(task, advance=30, description="[bright_cyan]Generando llaves criptográficas...")
            time.sleep(0.3) # Retraso visual para efecto en demostraciones
            
            # Cifrado
            salt = os.urandom(16)
            key = generate_key(password, salt)
            f = Fernet(key)
            encrypted_pdf = f.encrypt(pdf_data)
            progress.update(task, advance=40, description="[bright_red]Inyectando payload cifrado en MP3...")
            time.sleep(0.3)

            # Estructura final: Audio Original + Marcador + Salt + PDF Cifrado
            with open(output_path, "wb") as out_file:
                out_file.write(mp3_data)
                out_file.write(MARKER)
                out_file.write(salt)
                out_file.write(encrypted_pdf)
            
            progress.update(task, advance=30, description="[bold green]¡Inyección completada!")

        console.print(f"\n[bold green]✔️ Éxito:[/] Archivo blindado creado en [bold bright_yellow]{output_path}[/]")
    
    except Exception as e:
        console.print(f"[bold red]❌ Error crítico:[/] {e}")

def extract_pdf(mp3_path, output_path, password, is_cli=False):
    if not validate_files([mp3_path]):
        return

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=40, style="bright_cyan", complete_style="bright_red"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
            disable=is_cli
        ) as progress:
            
            task = progress.add_task("[bright_cyan]Analizando estructura del archivo...", total=100)
            
            with open(mp3_path, "rb") as f:
                data = f.read()
            progress.update(task, advance=20, description="[bright_cyan]Buscando marcadores esteganográficos...")
            time.sleep(0.3)
            
            marker_index = data.find(MARKER)
            if marker_index == -1:
                progress.stop()
                console.print("\n[bold red]❌ Error:[/] No se encontró un payload de HackeMate válido en este archivo.")
                return

            progress.update(task, advance=30, description="[bright_yellow]Extrayendo payload y descifrando...")
            time.sleep(0.3)
            
            # Extraer componentes
            payload_start = marker_index + len(MARKER)
            salt = data[payload_start : payload_start + 16]
            encrypted_pdf = data[payload_start + 16 :]
            
            # Descifrado
            key = generate_key(password, salt)
            f = Fernet(key)
            
            try:
                decrypted_pdf = f.decrypt(encrypted_pdf)
            except InvalidToken:
                progress.stop()
                console.print("\n[bold red]❌ Acceso Denegado:[/] Contraseña incorrecta o archivo corrompido.")
                return

            progress.update(task, advance=40, description="[bright_red]Escribiendo archivo recuperado...")
            
            with open(output_path, "wb") as out_file:
                out_file.write(decrypted_pdf)
                
            progress.update(task, advance=10, description="[bold green]¡Extracción completada!")

        console.print(f"\n[bold green]✔️ Éxito:[/] Archivo extraído correctamente como [bold bright_yellow]{output_path}[/]")

    except Exception as e:
        console.print(f"[bold red]❌ Error crítico:[/] {e}")

def interactive_menu():
    print_logo()
    while True:
        console.print("\n[bold bright_white]Menú de Operaciones:[/]")
        console.print("[bold bright_cyan]1.[/] Ocultar y Cifrar (Inyectar PDF en MP3)")
        console.print("[bold bright_cyan]2.[/] Extraer y Descifrar (Recuperar PDF)")
        console.print("[bold bright_cyan]3.[/] Salir")
        
        opcion = Prompt.ask("\n[bold bright_yellow]Seleccione una opción[/]", choices=["1", "2", "3"])
        
        if opcion == "1":
            pdf_path = Prompt.ask("[bright_white]Ruta del PDF a ocultar[/]")
            mp3_path = Prompt.ask("[bright_white]Ruta del MP3 base[/]")
            output_path = Prompt.ask("[bright_white]Nombre de salida[/]", default="output.mp3")
            password = Prompt.ask("[bright_red]Contraseña de cifrado AES[/]", password=True)
            embed_pdf(pdf_path, mp3_path, output_path, password)
            
        elif opcion == "2":
            mp3_path = Prompt.ask("[bright_white]Ruta del MP3 que contiene el secreto[/]")
            password = Prompt.ask("[bright_red]Contraseña de descifrado[/]", password=True)
            extract_pdf(mp3_path, "extracted_secret.pdf", password)
            
        elif opcion == "3":
            console.print("[bold bright_red]Sesión finalizada. Happy Hacking![/]")
            break

def main():
    # Configuración de Argparse para uso en Terminal (CLI)
    parser = argparse.ArgumentParser(
        description="HackeMusic - Herramienta Profesional de Esteganografía y Cifrado",
        epilog="Ejemplo: python HackeMusic.py --hide -p secreto.pdf -m audio.mp3 -o final.mp3"
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--hide", action="store_true", help="Modo ocultar: inyecta un PDF en un MP3")
    group.add_argument("--extract", action="store_true", help="Modo extraer: recupera el PDF de un MP3")
    
    parser.add_argument("-p", "--pdf", help="Ruta del archivo PDF (requerido para --hide)")
    parser.add_argument("-m", "--mp3", help="Ruta del archivo MP3")
    parser.add_argument("-o", "--out", help="Archivo de salida (por defecto: extracted_secret.pdf)", default="extracted_secret.pdf")
    parser.add_argument("-k", "--key", help="Contraseña para el cifrado AES")

    # Si el usuario no pasa argumentos, abrimos el menú interactivo con estética visual
    if len(sys.argv) == 1:
        interactive_menu()
        return

    # Si pasa argumentos, ejecutamos en modo silencioso de terminal
    args = parser.parse_args()

    if args.hide:
        if not all([args.pdf, args.mp3, args.key, args.out]):
            parser.error("Para ocultar se requiere: --pdf, --mp3, --out y --key")
        embed_pdf(args.pdf, args.mp3, args.out, args.key, is_cli=True)
        
    elif args.extract:
        if not all([args.mp3, args.key]):
            parser.error("Para extraer se requiere: --mp3 y --key")
        extract_pdf(args.mp3, args.out, args.key, is_cli=True)

if __name__ == "__main__":
    main()
