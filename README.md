# hormiga-culona

Repositorio principal del proyecto del hackathon.

## Descripción del proyecto

**Hormiga Culona** es una solución web pensada para facilitar el acceso ciudadano a datos públicos. La idea es que cualquier persona pueda consultar información del Estado en lenguaje natural, por texto o por voz, y recibir respuestas claras, útiles y fáciles de interpretar.

El proyecto busca reducir la barrera técnica que normalmente existe alrededor de los datos abiertos. En lugar de obligar al usuario a navegar tablas, bases de datos o documentos complejos, la plataforma transforma esos datos en una experiencia más accesible, con respuestas estructuradas y potencialmente acompañadas de visualizaciones.

## Estructura

- `backend/`: submódulo git que apunta a [`hormiga-culona-back-end`](https://github.com/CapituloJaverianoACM/hormiga-culona-back-end).
- `frontend/`: espacio reservado para la aplicación frontend.
- `docs/`: documentación del proyecto, problemática, propuesta de valor y enfoque tecnológico.

## Notas de trabajo

- Mantener el código de cada aplicación dentro de su propia carpeta (`backend/`, y luego `frontend/`).
- Preferir commits pequeños y con mensajes claros.
- Documentar decisiones y pasos de configuración en `docs/`.
- El backend es un submódulo, así que después de clonar el repositorio hay que inicializarlo.

## Comandos útiles

```bash
# clonar con submódulos
git clone --recurse-submodules git@github.com:CapituloJaverianoACM/hormiga-culona.git

# si ya clonaste el repositorio
git submodule update --init --recursive

# actualizar el backend desde su rama principal remota
git submodule update --remote backend
```

## Más contexto

Si quieres más detalle sobre la motivación y la solución, revisa:

- `docs/Problematica.md`
- `docs/Propuesta_de_valor.md`
- `docs/Aproach_tecnologico.md`
- `docs/CRISP-DM.md`
