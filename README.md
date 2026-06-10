# Trabajo Práctico Integrador - Procesamiento de compras de supermercado

**Alumna:** Paz Sevilla

Sistema en Python para el procesamiento de compras de un supermercado, con un flujo de trabajo basado en Integración Continua (CI) usando GitHub Actions.

## Descripción

El proyecto procesa un archivo CSV de compras, ordena los registros por sucursal mediante el método burbuja y genera un resumen por sucursal (unidades vendidas, producto de mayor y menor importe).

## Estructura del proyecto

```
├── main.py                     # Código fuente del sistema
├── test_main.py                # Pruebas unitarias con pytest
├── requirements.txt            # Dependencias del proyecto
├── .gitignore                  # Archivos y carpetas ignorados por Git
└── .github/
    └── workflows/
        └── ci.yml              # Pipeline de Integración Continua
```

## Requisitos

- Python 3.12 o superior

## Instalación

Crear y activar un entorno virtual:

```bash
python3 -m venv myfirstproject
source myfirstproject/Scripts/activate   # Windows (Git Bash)
# source myfirstproject/bin/activate     # Linux / Mac
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar el programa

```bash
python main.py
```

## Pruebas unitarias

El proyecto cuenta con pruebas unitarias desarrolladas con pytest:

| Test | Función evaluada | Qué verifica |
|------|------------------|--------------|
| `test_ordenar_burbuja_ordena_por_sucursal` | `ordenar_burbuja` | Ordenamiento correcto de filas por sucursal |
| `test_procesar_sucursal_calcula_resumen` | `procesar_sucursal` | Cálculo de unidades, producto mayor y menor |
| `test_ordenar_burbuja_un_elemento` | `ordenar_burbuja` | Comportamiento con una lista de un solo elemento |
| `test_procesar_sucursal_un_solo_producto` | `procesar_sucursal` | Resumen correcto con un único producto |
| `test_procesar_sucursal_acumula_mismo_producto` | `procesar_sucursal` | Acumulación de unidades de un producto repetido |


## Ejecutar los tests

```bash
pytest
```

## Integración Continua (CI)

El proyecto utiliza GitHub Actions. Cada push o Pull Request hacia `main` dispara una pipeline que:

1. Clona el repositorio
2. Instala Python y las dependencias
3. Ejecuta los tests automáticamente

La rama `main` está protegida: requiere Pull Request y que la pipeline pase para poder mergear.


## Pruebas del flujo de CI (Pull Requests)

Para validar el funcionamiento de la pipeline y la protección de rama, se realizaron dos pruebas que quedan documentadas como Pull Requests abiertos:

### PR con tests exitosos

Se agregó un test válido en una rama secundaria y se abrió un Pull Request. La pipeline se ejecutó automáticamente y todos los tests pasaron, por lo que el check apareció en verde y el merge quedó habilitado.

### PR con fallo intencional

Se introdujo un test incorrecto a propósito (un `assert` que afirma un orden equivocado) en otra rama. Al abrir el Pull Request, la pipeline se ejecutó y detectó el fallo:

- El test `test_error_intencional` falló con un `AssertionError`.
- pytest finalizó con el resumen `1 failed, 5 passed` y código de salida 1.
- GitHub Actions interpretó ese código de salida como una falla y marcó el check en rojo.
- Gracias a la protección de la rama `main`, el botón de merge quedó bloqueado, impidiendo integrar código que no pasa las pruebas.

Esto demuestra que la pipeline y las reglas de protección funcionan correctamente: solo se puede mergear a `main` cuando los tests pasan.