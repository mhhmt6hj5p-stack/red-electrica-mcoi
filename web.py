"""Entrada de Streamlit Cloud: abre la copia de consulta incluida, sin solver."""
from pathlib import Path
import hashlib
import os
import runpy
import sys
import tempfile
import zipfile

paquete = Path(__file__).resolve().with_name('consulta.zip')
firma = hashlib.sha256(paquete.read_bytes()).hexdigest()
carpeta = Path(tempfile.gettempdir()) / ('mcoi_consulta_' + firma)
if not (carpeta / 'interfaz.py').exists():
    with zipfile.ZipFile(paquete) as archivo:
        archivo.extractall(carpeta)
if str(carpeta) not in sys.path:
    sys.path.insert(0, str(carpeta))
os.chdir(carpeta)
runpy.run_path(str(carpeta / 'interfaz.py'), run_name='__main__')
