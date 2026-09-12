1. Modos
	1. Ask
	2. Plan
	3. Agent -> implementa el plan
2. Models
	1. GitHub Copilot -> provee la interfaz y las herramientas con los que trabajará el  LLM 
	2. Modelos -> Antropic provee los modelos Claude, Google los modelos Gemini, OpenAI los modelos GPT...
	3. Esfuerzo - Effort. 
3. Settings de Copilot
	1. @feature:chat auto approve


- **`.github/`** es una carpeta especial que GitHub/GitHub Copilot reconoce como lugar para guardar configuración relacionada con el repositorio. No es código de la aplicación.
- **`.github/agents/`** es el directorio donde se pueden definir **agentes personalizados de Copilot** mediante ficheros `.agent.md`.
- **`instructions-generator.agent.md`** es, por tanto, la definición de un agente llamado aproximadamente **Instructions Generator**. El nombre del fichero es el que permite identificarlo dentro de esa colección de agentes.
- Un fichero **`.agent.md`** es básicamente un documento Markdown con **instrucciones/metadatos que Copilot utiliza para configurar el comportamiento de ese agente**. No es un fichero que tu aplicación ejecute.
- Cuando en Copilot seleccionas **Instructions Generator**, le estás diciendo: _«para esta conversación, utiliza la configuración/instrucciones definidas por este agente»_.
- El `/create-copilot-instructions ...` es un **comando especial de Copilot**. No es algo que vaya a ejecutar Next.js, TypeScript ni tu aplicación. Es una instrucción dirigida al propio Copilot para que genere unas **instrucciones persistentes para el repositorio**.
- La idea general del ejercicio es, por tanto, un flujo de dos niveles:
    1. **`.github/agents/instructions-generator.agent.md`** → configura _cómo trabaja Copilot como generador de instrucciones_.
    2. **`/create-copilot-instructions ...`** → le pides a ese agente que convierta tus requisitos en instrucciones que Copilot pueda aplicar posteriormente al trabajar en el código.
- Esas instrucciones generadas normalmente terminan en un fichero de configuración/instrucciones de Copilot dentro de **`.github/`**. Ese fichero queda **versionado junto con el proyecto**, de modo que otros desarrolladores/Copilot puedan utilizar las mismas reglas.
- La ventaja de ponerlo en `.github` es que **las reglas forman parte del repositorio**, no de tu configuración personal de VS Code/Copilot. Puedes hacer commit, revisarlas en PR, modificarlas, etc.
- En resumen, **no estás creando una estructura que Next.js vaya a leer**. Estás creando una estructura que **GitHub Copilot lee para saber cómo debe comportarse al ayudarte con ese repositorio**.
- Una forma sencilla de visualizarlo es:

```
.github/
└── agents/
    └── instructions-generator.agent.md
          ↓
    configura el agente
          ↓
    seleccionas "Instructions Generator"
          ↓
    ejecutas /create-copilot-instructions ...
          ↓
    Copilot genera instrucciones para el repositorio
          ↓
    esas instrucciones sirven posteriormente
    para que Copilot siga las reglas al programar
```

Hay un detalle importante: **`.github/agents/` y los ficheros de instrucciones generados no son exactamente lo mismo**. Si quieres, en la siguiente pregunta podemos centrarnos únicamente en **qué ficheros concretos puede haber dentro de `.github/`, para qué sirve cada uno y cuándo Copilot lee cada uno**.