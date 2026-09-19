https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/use-hooks?utm_source=chatgpt.com


carpeta hooks en .github, con fichero vacío format.json

npm i -D prettier

creamos el fichero .prettierrc
y le añadimos el contenido 
{
    "semi": true,
    "singleQuote":true
}


Lanzamos en la terminal copilot, para que se abra el CLI y usamos el siguiente prompt:

update the @app/page.tsx to remove any references to tracking or analytics
as these features do not exist in our app

El contenido del prompt en este caso no es importante, lo imporatne es que se lanzará el hook que revisará el códig ajustándolo a pretty mode, poniendo ; al final de líneas, etc. 

