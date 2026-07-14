# Approach tecnológico

## ¿Cuál es nuestro approach?

Nuestro approach tecnológico parte de una idea simple: tomar datos públicos que ya existen y convertirlos en una experiencia de consulta mucho más natural para las personas. Para lograrlo, planteamos una solución web en la que el usuario puede interactuar por texto o por voz, hacer preguntas en lenguaje natural y recibir respuestas claras, visualizaciones y resultados útiles para interpretar la información.

La solución está pensada como una arquitectura conectada entre frontend, backend, datos y servicios de inteligencia artificial. Desde la experiencia de usuario, el frontend puede comunicarse con el sistema por medio de endpoints HTTP cuando la interacción es solo texto y por medio de WebSocket cuando se requiere una experiencia con voz. Esto permite que la comunicación sea más flexible y más cercana a una conversación real.

En el backend utilizamos FastAPI como capa principal de orquestación. Allí se reciben las solicitudes del usuario, se identifica si la intención es conversacional o si requiere una salida orientada a interfaz, se consulta la base de datos y se devuelve una respuesta estructurada. Este flujo permite no solo responder preguntas, sino también preparar información lista para tablas, gráficos, listas y otros componentes visuales.

La parte más importante de nuestro approach está en Azure, porque es el núcleo que hace posible una solución inteligente, accesible y preparada para crecer. Usamos Azure AI Foundry para el despliegue del modelo de lenguaje que interpreta las preguntas del usuario y transforma una necesidad expresada en lenguaje natural en una respuesta entendible o en una consulta útil sobre los datos. Esto nos permite construir una interacción mucho más intuitiva, sin exigir conocimientos técnicos al ciudadano.

Además, usamos Azure Speech para dos capacidades fundamentales. La primera es la transcripción de audio a texto, que permite que una persona hable con el sistema y que su consulta sea comprendida. La segunda es la síntesis de voz, que permite responder de vuelta con habla natural. Este punto es clave para la accesibilidad, porque la comunicación con el sistema deja de depender únicamente de la lectura y la escritura y se vuelve más incluyente para distintos perfiles de usuario.

Azure nos aporta beneficios concretos dentro de esta solución. Nos permite integrar modelos de lenguaje y servicios de voz dentro de una misma lógica de nube, facilita el despliegue de capacidades avanzadas sin construir esa infraestructura desde cero y nos deja una base tecnológica con posibilidades reales de crecimiento a futuro. También nos permite mantener una arquitectura más ordenada, donde la inteligencia del sistema y la capa de voz se apoyan en servicios robustos y listos para escalar.

A nivel de datos, la solución se conecta con una base preparada para consultas de solo lectura, lo que ayuda a proteger la integridad de la información. Adicionalmente, incorporamos un pipeline automatizado para extraer, procesar y cargar datos públicos a la base, garantizando que la solución no dependa solo de actualizaciones manuales y que tenga mejores condiciones para mantenerse vigente en el tiempo.

## ¿Cuál es su potencial a futuro?

El potencial a futuro de esta solución es alto porque no está pensada únicamente para resolver un caso puntual, sino para convertirse en una forma más amplia de acceso ciudadano a la información pública. Hoy trabajamos sobre conjuntos de datos específicos, pero el mismo enfoque puede extenderse a más bases de datos, más entidades y más tipos de información del Estado.

Gracias al uso de Azure, el proyecto tiene una base tecnológica con capacidad de evolución. A futuro se pueden desplegar mejores modelos, mejorar la calidad de la conversación, fortalecer la interacción por voz y ampliar la cobertura a más usuarios sin cambiar la idea principal del sistema. Esto significa que la solución puede crecer no solo en cantidad de datos, sino también en calidad de la experiencia.

También existe potencial para fortalecer el frontend como una capa más completa de visualización y comunicación. La arquitectura actual ya está pensada para entregar respuestas conversacionales, datos estructurados para interfaz y audio sintetizado, por lo que más adelante se podrían construir paneles, vistas comparativas, experiencias móviles o asistentes especializados sobre la misma base tecnológica.

## ¿Es escalable?

Sí, es escalable porque su diseño tecnológico separa responsabilidades y se apoya en servicios de nube que pueden crecer con la demanda. El backend orquesta las solicitudes, los servicios de Azure resuelven la capa de inteligencia artificial y voz, la base de datos soporta las consultas y el pipeline automatizado mantiene actualizada la información. Esta separación hace que el sistema pueda evolucionar por componentes sin tener que rehacerlo completamente.

El uso de servicios en nube es una de nuestras mayores ventajas en escalabilidad. Azure nos permite pensar en una solución que puede atender más usuarios, integrar nuevas capacidades y sostener una operación más amplia con mejores posibilidades de mantenimiento. Esto nos diferencia porque no estamos construyendo una demo aislada, sino una base tecnológica que puede crecer hacia un producto público real.

Además, la solución ya contempla distintos canales de comunicación con el usuario. Puede funcionar en texto, en voz y en respuestas orientadas a interfaz. Esa flexibilidad ayuda a escalar no solo en infraestructura, sino también en usos posibles, ya que la misma lógica puede alimentar chat, asistentes hablados, paneles visuales y futuras integraciones.

## ¿Por qué es novedoso?

Es novedoso porque no se limita a mostrar datos abiertos ni a responder preguntas de forma aislada. Nuestra propuesta conecta lenguaje natural, consulta de datos, visualización y comunicación por voz dentro de una misma experiencia. Esto hace que el acceso a la información pública sea más natural, más comprensible y más cercano para las personas.

También es novedoso porque prioriza la accesibilidad como parte central de la solución y no como un añadido posterior. La posibilidad de hablar con el sistema y recibir respuestas por voz amplía el alcance del proyecto y mejora la relación entre ciudadanía e información pública. En lugar de pedirle al usuario que aprenda a navegar bases de datos complejas, llevamos la información a un formato de conversación.

Otro punto novedoso es que nuestro stack tecnológico no solo resuelve el presente, sino que está pensado para crecer. La combinación de Azure AI Foundry, Azure Speech, backend modular, base de datos en nube y automatización de actualización de datos crea una solución con valor inmediato y con proyección futura. Esa capacidad de crecimiento es parte de lo que nos diferencia.

## Accesibilidad para muchos no significa para todos

Para nosotros, accesibilidad para muchos no significa necesariamente accesibilidad para todos. Una solución realmente útil no puede asumir que todas las personas se relacionan igual con la tecnología, con la lectura, con la escritura o con la interpretación de tablas complejas. Por eso, nuestro approach tecnológico da tanta importancia a la voz y a la comunicación clara.

La integración de transcripción y síntesis de voz con Azure permite abrir una puerta distinta de acceso a la información pública. Una persona puede hablar, preguntar de forma natural y recibir una respuesta hablada y entendible. Esto hace que la solución sea más incluyente y que la experiencia no dependa únicamente de interfaces tradicionales.

En ese sentido, la tecnología no está solo al servicio de procesar datos, sino también de comunicar mejor. Ese es uno de los puntos más fuertes de nuestra solución: no solo acercamos información pública a las personas, sino que la acercamos en un formato más humano, más usable y con mejores condiciones de accesibilidad.
