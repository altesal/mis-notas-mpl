Next JS (fullstack fwk)
Shadcn ui + tailwind css
Postgress DB on Neon
Drizzle ORM  (para interactuar con la bbdd)
Clerk for auth

Zod -> backend

## Requisitos

Next JS




## 24. Setup up Next JS project

#### Crear el proyecto
1. En una terminal de VS Code:    
$ npx create-next-app@latest calendarproject

2. Dependencias
	- Shadzen UI
	$ npx shadcn@latest init
	- 
#### Configurar autenticación con Clerk 
2. Ir a clerk.com (autenticación)
- Create Application. Name CalendarProject
- Opción Sign In solo mail (desmarcar Google)
- Seleccionamos Next.js, y copiamos prompt. Lo pegamos en el chat de GitHub Copilot
	- Install Clerk CLI   ($ npm install -g clerk)
	- Finalmente creará un fichero proxy.ts (antiguamente middleware.ts)

#### Crear bbdd Postgress y configurar el ORM

1. Lo creamos desde la web de postgress, neon.com
	1. Nombre del proeycto
	2. AWS Europe West (London)
2. Ir a  orm.drizzle.team   para isntalar sus dependencias
	1. Link Get Started, y seleccionar NEON https://orm.drizzle.team/docs/get-started/neon-new
	2. Ir a las isntrucciones de instalación
			npm i drizzle-orm@rc @neondatabase/serverless dotenv
			npm i -D drizzle-kit@rc tsx
		3. Create a `.env` file in the root of your project and add your database connection variable (renombraremos .env.local que ya existe a .env):
			```
			DATABASE_URL=
			```
		4.   Step 3 - Connect Drizzle ORM to the database
			Create a `index.ts` file in the `src` directory and initialize the connection:
			import { drizzle } from 'drizzle-orm/neon-http';
			const db = drizzle(process.env.DATABASE_URL);

			5. Crear un esquema src/db/schema.ts (nosotros antes pasamos de carpeta src)
			6. drizzle.config.ts
			7. Creamos el fichero schema.ts dentro de la folder db
			8. Volvemos a la documentación de clerk
				1. Ya habíamos lanzado el prompt
				2. Set your clerk apik en .env
			9. Ejecutar npm run dev -> https://localhost:3000

#### Custom agents
Fichero AGENTS.ms
Metemos en el chat el sigiente prompt (añadiendo el AGENTS.md al contexto)
Build out the content for this agent instructions file for this project. This is an instructions filespecifically for LLM's to adhere to the config standars for this project. Agent instructions will be separated out into separate .md markdown files located in the /docs directory.  

Seleccionar en la ventana de chat la opción Agent Customizations 
Agents > New Agent > "Select a directory for the new customization file in ..."
Seleccionamos .github\agents y le damos el nombre al fichero instructions-generator, y él lo llamará instructions-generator.agent.md
El ficchero se crea dentro de .github\agents 
Configuramos las tools -> Edit, Read, Search y Fetch web


#### Prompt file (custom)
Creamos un prompt que llamamos create-instructions.prompt.md
Lo invocamos en el chat con /create-instructions