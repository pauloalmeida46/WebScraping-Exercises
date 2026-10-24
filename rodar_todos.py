import os
import socket
import subprocess
import sys
import time
from pathlib import Path

HOST = "127.0.0.1"
PORTA = 8000
RAIZ = Path(__file__).resolve().parent


def esperar_servidor(timeout=10):
    limite = time.time() + timeout
    while time.time() < limite:
        try:
            with socket.create_connection((HOST, PORTA), timeout=0.5):
                return True
        except OSError:
            time.sleep(0.2)
    return False


def main():
    env = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
    pastas = sorted(p for p in RAIZ.glob("exercicio_*") if p.is_dir())

    for pasta in pastas:
        print(f"\n{'#' * 60}\n# {pasta.name.upper()}\n{'#' * 60}", flush=True)

        servidor = subprocess.Popen(
            [sys.executable, "-m", "http.server", "--bind", HOST, str(PORTA)],
            cwd=pasta,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            if not esperar_servidor():
                print(f"Servidor não subiu na porta {PORTA} (já está em uso?).")
                continue
            subprocess.run([sys.executable, "raspagem.py"], cwd=pasta, env=env)
        finally:
            servidor.terminate()
            servidor.wait()
            print(f"\n[servidor de {pasta.name} encerrado]", flush=True)

    print("\nTodos os exercícios foram executados.")


if __name__ == "__main__":
    main()
