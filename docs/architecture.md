# Arquitectura

En esta seccion se va a describir de manera general la arquitectura de la solucion propuesta. La documentacion arquitectonica sigue el estandar **C4** para describir el sistema en distintos niveles de abstraccion.

## Diagrama de contexto

En primera instancia el diagrama de contexto (nivel 1 del modelo C4) provee una vista general de la solucion y las interacciones existentes con sistemas externos.

![Diagrama de contexto - Hormiga Culona](https://i.imgur.com/x2LtAy5.png)

El diagrama muestra a **Hormiga Culona**, el sistema de visualizacion de presupuesto, como nucleo de la solucion. El **Usuario** interactua directamente con la aplicacion para consultar informacion publica en lenguaje natural (texto o voz) y recibir respuestas claras con visualizaciones.

Hacia afuera, Hormiga Culona depende de dos sistemas externos:

- **Azure** (nube publica): se usa principalmente para el alojamiento del agente y los servicios de IA que interpretan las consultas del usuario.
- **Datos Abiertos** (sistema de datos abiertos del gobierno): se usa principalmente para extraer los datos publicos que alimentan la visualizacion y las respuestas del sistema.

## Diagrama de contenedores

El diagrama de contenedores (nivel 2 del modelo C4) descompone Hormiga Culona en los bloques ejecutables que conforman la solucion y muestra como se comunican entre si y con los sistemas externos.

![Diagrama de contenedores - Hormiga Culona](https://i.imgur.com/zBQjvst.png)

Dentro del sistema se identifican los siguientes contenedores:

- **Aplicacion Web (Astro):** cliente web de visualizacion con el que interactua el usuario. Envia las consultas (texto o voz) hacia el backend y presenta respuestas, tablas y graficos.
- **FastAPI:** backend de comunicacion y orquestacion. Recibe las peticiones del frontend, consulta la base de datos, se conecta con Azure para el agente/IA y devuelve respuestas estructuradas listas para la interfaz.
- **Apache Airflow:** orquestador del pipeline de datos. Extrae informacion de Datos Abiertos, la procesa y la carga en la base de datos.
- **Base de datos (PostgreSQL en Supabase):** almacena la informacion resultante de la extraccion. Airflow escribe los datos cargados y FastAPI los consulta en modo lectura para responder al usuario.

Como sistemas externos al diagrama:

- **Azure:** nube publica donde se alojan el agente y los servicios de IA/voz que FastAPI consume.
- **Datos Abiertos:** fuente gubernamental de la que Airflow extrae los datos que alimentan el sistema.

## Diagrama de componentes

El diagrama de componentes (nivel 3 del modelo C4) detalla la estructura interna de los contenedores: como se descompone el backend, como el agente orquesta servicios especializados y como el pipeline de Airflow alimenta la base de datos.

![Diagrama de componentes - Hormiga Culona](https://i.imgur.com/PAZc5Fe.png)

### Flujo de consulta del usuario

El **Usuario** interactua con la **Aplicacion Web (Astro)**, el cliente de visualizacion. Esta envia peticiones HTTP al backend, donde el **Fast API Controller** actúa como punto de entrada: recibe los requests de la API y los deriva al nucleo de la logica de negocio.

El **AgentOrchestratorService** es el servicio principal de orquestacion. Centraliza la peticion del usuario, decide que capacidades del agente se requieren (voz, memoria, respuesta conversacional o salida para interfaz) y coordina el resto de componentes.

### Componentes del agente

Bajo el control del orquestador operan cuatro componentes especializados:

- **AudioService:** administra el audio de los agentes (transcripcion y sintesis de voz). Se apoya en Azure (p. ej. Azure Speech) para convertir voz a texto y respuestas a audio, habilitando la interaccion hablada.
- **Memory:** gestiona la memoria contextual de los agentes, de modo que la conversacion conserve historial y coherencia entre turnos. Tambien se apoya en Azure.
- **ResponseService:** administra la generacion de respuestas del agente a partir del lenguaje natural. Consulta Azure para el modelo de lenguaje y la **base de datos** cuando la respuesta requiere datos presupuestales o publicos ya cargados.
- **UIService:** transforma datos estructurados en formatos listos para graficar o renderizar en la interfaz (tablas, charts, listas). Consulta la **base de datos** para obtener la informacion a visualizar y se apoya en Azure cuando hace falta procesamiento adicional.

Asi, la consulta del usuario puede resolverse como conversacion (texto/voz) o como salida orientada a interface, sin cambiar el punto de entrada.

### Persistencia y sistemas externos

- **Azure (nube publica):** hospeda y provee los servicios de IA y voz que consumen AudioService, Memory, ResponseService y UIService.
- **Base de datos (PostgreSQL en Supabase):** almacena la informacion proveniente de la extraccion. La consultan **ResponseService** y **UIService** para armar respuestas y visualizaciones; tambien recibe la carga final del pipeline de Airflow.

### Pipeline de datos (Apache Airflow)

De forma asincrona al flujo de consulta, el contenedor **Apache Airflow** ejecuta un pipeline ETL compuesto por tres componentes encadenados:

1. **Extraccion de datos:** obtiene los datasets publicos desde **Datos Abiertos** (sistema de datos abiertos del gobierno).
2. **Limpieza / Procesamiento:** recibe los datos crudos, los limpia y los transforma a un esquema util para consulta.
3. **Almacenamiento:** persiste el resultado limpio en la **base de datos** de Supabase.

Con esto, el sistema separa claramente dos vias: el camino interactivo (usuario → web → controller → orquestador → servicios del agente → Azure/BD) y el camino de alimentacion de datos (Datos Abiertos → extraccion → limpieza → almacenamiento → BD).

### Estilo de comunicacion

La comunicacion entre componentes es principalmente **REST** para la mayoria de los servicios (consultas de texto, respuestas estructuradas, visualizacion y operaciones habituales del backend). Para la **comunicacion de voz** entre el front-end y el backend se utilizan **WebSockets**, lo que permite un canal bidireccional en tiempo real adecuado para streaming de audio (transcripcion y sintesis).

### Arquitectura del back-end

La arquitectura del back-end es principalmente en **capas**: el controller recibe la peticion, el orquestador coordina la logica de aplicacion y los servicios especializados (audio, memoria, respuesta, UI) encapsulan responsabilidades concretas hacia Azure y la base de datos. Esta separacion mantiene el flujo ordenado y facilita evolucionar cada capa de forma independiente.
