# Candidate Recruitment Automation

Este proyecto automatiza el proceso de reclutamiento de candidatos utilizando **Selenium WebDriver** para interactuar con el navegador y **Behave** para pruebas automatizadas siguiendo el estilo de desarrollo basado en comportamiento (**BDD**).

## Tecnologías utilizadas

- **Selenium WebDriver**: Para la automatización del navegador.
- **Behave**: Para ejecutar pruebas en el formato de Cucumber.

## Estructura del Proyecto

```bash
├── abilities
│   └── use_browser.py            # Habilidad para usar el navegador
├── actor.py                      # Actor que realiza las acciones en el sistema
├── questions
│   └── check_status.py           # Pregunta para verificar el estado del candidato
├── tasks
│   ├── add_candidate.py          # Tarea para agregar un candidato
│   ├── login.py                  # Tarea para iniciar sesión como Admin
│   ├── navegate_to.py            # Tarea para cambiar el estado del candidato
│   ├── navigate_to_recruitment.py # Tarea para navegar al módulo de reclutamiento
│   ├── save_form.py              # Tarea para guardar cambios en el formulario
│   └── interview.py              # Tarea para programar una entrevista
├── features
│   ├── cadidate.feature  # Archivo de características para el flujo de reclutamiento
│   └── steps
│       └── candidate_steps.py              # Definiciones de pasos para Behave
├── main.py                       # Script para ejecutar el proceso completo sin Behave
├── README.md                     # Documentación del proyecto
```

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/ronaldo2983/recruitment-automation-test.git
   ```

2. **Navega a la carpeta del proyecto**:
   ```bash
   cd recruitment-automation-test
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución del Proyecto

### 1. **Ejecución con Python (`main.py`)**

Puedes ejecutar el proceso de automatización directamente utilizando el script `main.py`. Este script cubre el flujo completo de reclutamiento: iniciar sesión, agregar candidato, programar entrevistas y cambiar los estados del candidato.

```bash
python main.py
```

### 2. **Ejecución con Behave (BDD)**

Para ejecutar las pruebas en formato **BDD** usando **Behave**, primero asegúrate de que Behave está instalado:

```bash
pip install behave
```

Luego, ejecuta **Behave** con:

```bash
python -m behave
```

Esto ejecutará el archivo de características que describe el proceso de reclutamiento (`manage_candidate.feature`).

## Notas

- Asegúrate de tener la última versión de **Selenium WebDriver** y **Geckodriver** (para Firefox) configurados correctamente en tu sistema.
- Si encuentras problemas al ejecutar los tests, revisa si los ejecutables de **WebDriver** están bien configurados en tu sistema.

---

Este **README.md** proporciona instrucciones sencillas para instalar y ejecutar el proyecto, ya sea con **Python** directamente o utilizando **Behave** para pruebas basadas en comportamiento.