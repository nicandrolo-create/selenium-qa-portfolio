# Selenium QA Portfolio

Suite de pruebas automatizadas end-to-end con **Selenium + Pytest**, corriendo contra
[saucedemo.com](https://www.saucedemo.com/), el sitio oficial de práctica de Sauce Labs.

## Qué cubre

- **Login** (`tests/test_login.py`): credenciales válidas, usuario bloqueado, credenciales inválidas.
- **Checkout** (`tests/test_checkout.py`): flujo completo de compra de principio a fin, y validación de carrito vacío.

## Cómo correrlo

```bash
python -m venv venv
venv\Scripts\activate        # en Windows
pip install -r requirements.txt
pytest -v
```

No necesitas instalar ChromeDriver a mano — `webdriver-manager` lo descarga y gestiona automáticamente.

## Integración continua

Cada push a `main` corre toda la suite automáticamente en GitHub Actions (`.github/workflows/tests.yml`),
en Chrome headless sobre Ubuntu.

## Por qué este proyecto

Demuestra un flujo de QA automation real: page interactions, aserciones sobre estado de la
aplicación (no solo "el botón existe"), fixtures reutilizables con Pytest, y CI configurado —
no solo scripts sueltos.
