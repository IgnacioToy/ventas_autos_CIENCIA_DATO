from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            # Leemos todas las líneas
            lines = file_obj.readlines()
            
            for line in lines:
                # .strip() quita espacios, saltos de línea y tabuladores
                req = line.strip()
                
                # REGLA DE ORO: Si la línea tiene un guion al principio (-e, -c, -r)
                # la ignoramos, porque NO es un paquete de Python.
                if not req or req.startswith('-'):
                    continue
                
                requirements.append(req)
                    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}")

    return requirements

setup(
    name = 'proyecto',
    version = '0.0.1',
    author = 'Ignacio',
    author_email = 'ignacionicolastoyos@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)