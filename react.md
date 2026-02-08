
## Versiones

| SOftware | Versión | Ver version    | Instalación          | Actualización | Desinstalación |
| -------- | ------- | -------------- | -------------------  | ----------    |  ------------- |
| nvm      | 1.2.2   | nvm version    | nvm-setup.exe        | ----------    |  ------------- |
| Node     | 22.12.2 | node --version | nvm install 22.12.0  | ----------    |  ------------- |
| React    | ------- | ----------- | xxx  | ----------    |  ------------- |

nvm: https://github.com/coreybutler/nvm-windows/releases/download/1.2.2/nvm-setup.exe

# Inicializar proyecto


## 1. Creando nosotros el punto de entrada

Crear un proyecto vanilla y pasarlo a React

``` 
npm create vite@latest  #Elegimos Vanilla y JS.  Más adelante, con todo montado: React y "Javascript + SWC"
```
Al finalizar

```
npm install
```

Entramos a la carpeta del proyecto, y abrimos VSCOde
``` 
code .
npm install @vitejs/plugin-react -E  #Plugin React
npm install react react-dom -E
```
Nuevo Fichero configuración de vite vite.config.js

index.html  -> main.js (punto de entrada)

En main.js creamos el root...

Renombarar (por vite) js por jsx, en el index.html y en el main.jsx

## 2. Instalar el linter

```
npm install standard -D
```

Modificar el package.json, bajo dependencias


````
},
"eslintConfig": {
    ~~"extends": "./node_modules/standard/eslintrc.json"~~
    "extends": "standard"
}
````
## 3. Comenzamos la app

Limpiar css en App.css y index.css. Ir a water.css (framework CSS classLess) y copiarlo en el index.css
Creamos fichero App.jsx con simplemente un h1
```
function App(){
    return(
        <div>
            <h1>Hello World!</h1>
        </div>
    )
}
export default App;
```
Lo configuramos desde el main.jsx
```

import {createRoot} from 'react-dom/client'
import { StrictMode } from 'react'

createRoot(document.getElementById('root')).render(
    <strictMode>
        <App />
    </strictMode>
)
```

Input y botón... y siempre que haya un input y un botón, englobarlos en un Formulario!



Lo importamos en el main.jsx

Usar conceptos: usseEffect, useState, customHooks

    useEffect : Ejecuta lógica tras renderizar el componente, sincronizando efectos secundarios con cambios en dependencias específicas

    customHook: Utilizar lógica de nuestro componente, en otro componente. Extrayendo...
        - Es una caja negra
        - Desligarlo de la implementación. Por ejemplo en el nombre, no usar cosas del estilo useFactFetch sino UseCatFact, porque hay que evitar ligarlo a la implementación (fetch...)
        - Pregunta importante: ¿Este useEffect lo puedo separar a un customHook?
    
    useRef: hook que permite crear una referencia mutable  que persiste durante todo el ciclo de vida del componte (=su valor no se reinicia). Útil para guardar cualquier valor que pueda mutar (identificador, contador, elemento del dom) y, que cada vez que cambia, no vuelve a renderizar el componente. Esto es lo que lo hace totalmente diferente al useState, porque el useState cada vez que cambia, se vuelve a renderizar el componente

PREGUNTAS
  - Si veo useEffect ¿puede ir a  un customHook?
  - Si veo código renderizándose ¿puede ir a un componente?
COSTUMBRES
  - Dejar los componentes limpios ¿Cómo? Sacando al lógica a customHooks

Ejemplo típico, pasos:

- Versión inicial. Lectura de un mock y renderizado de items sin lógica de búsqueda (folder mocks)
- Nuevo componente Movies.jsx (folder components)
- Cusom Hook que se encargue del fetch, estado (folder hooks)
    - Establecer mapeos para evitar que los componentes dependan de los contratos de API
- No lo usamos. Opcional. Capturar la referencia del valor del input con un useRef
- Usar  onSubmit={handleSubmit} del formulario en vez del onClick={handleClick} del botón
- OPCIÓN 1 (Recomendada). Forma NO  CONTROLADA. Leer info del formulario según el evento de formulario
- OPCIÓN 2. Forma CONTROLADA. Usando Estado. 
    - customHook useSearch, para validaciones, mostrar mensaje de error, control del estado de la search, etc.
    - useRef para evitar mensajes de error en el primer render (uno de sus buenos usos... es mucho más que una referencia a un elemento del dom!!!)


- Banderitas para detectar primera vez. Usar useRef en vez de useState, porque useState renderizaría el compomnente. Solo necesitamos que controle el componente. Las referencias, cuando se actualizan, NO se vuelven a renderizar!!!

- Implementar fetch de datos con el valor de la caja de búsqueda

- Servicio de búsqueda

- Loading antes del fetching de datos. Poner a false en el finally

- UseRef para guardar la búsqueda anterior y evitar llamadas innecesarias

# Test

1. Instalación

```
PS C:Documents\Repos\react-testing> npm init playwright@latest

> npx
> create-playwright

Getting started with writing end-to-end tests with Playwright:
Initializing project in '.'
? Do you want to use TypeScript or JavaScript? ...
> TypeScript
√ Do you want to use TypeScript or JavaScript? · JavaScript
√ Where to put your end-to-end tests? · tests
√ Add a GitHub Actions workflow? (Y/n) · false
√ Install Playwright browsers (can be done manually via 'npx playwright install')? (Y/n) · true
Installing Playwright Test (npm install --save-dev @playwright/test)…

added 3 packages, and audited 267 packages in 5s

118 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
Installing Types (npm install --save-dev @types/node)…

added 2 packages, and audited 269 packages in 3s

118 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
Writing playwright.config.js.
Writing tests\example.spec.js.
Writing package.json.
Downloading browsers (npx playwright install)…
Downloading Chromium 143.0.7499.4 (playwright build v1200) from https://cdn.playwright.dev/dbazure/download/playwright/builds/chromium/1200/chromium-win64.zip
169.8 MiB [====                ] 20% 19.7s

```

2. Ejecución

```
PS C:\Users\Repos\react-testing\projects\react-test> npx playwright test
```

2. Ejecución viendo informe

```
PS C:\Users\Repos\react-testing\projects\react-test> npx playwright show-report
```
# Ideas

ELEMENTO = Lo que se renderiza!!

COMPONENTE = 1 función que crea un elemento
 Componente 

    -> Factoría de elementos

    -> Crea elementos

    -> Función que devuelve elementos...


main.jsx --> punto de entrada de la aplicación

```
<div id="root"></div>
<script type="module" src="/src/main.jsx"></script>  

```` 


## Estados
La actualización de los estados es asíncrona, o sea, no se pueden utilizar inmediatamente después de actualizarlos

Dos estados, y uno depende de otro


## Varios


### Desestructuración de objetos

Ejemplo de objeto

```
const data = { fact: "X", length: 10, type: "curioso" };

// Desestructuración
const { fact, length, type } = data;

setFact(fact);
console.log(length, type);
```


### EJEMPLO SPREAD -> Array/objetos  -> Expande

```
const frutasBase = ['manzana', 'pera'];
const frutasExtra = ['plátano', 'kiwi'];

const todasLasFrutas = [...frutasBase, ...frutasExtra, 'mango'];
console.log(todasLasFrutas);
// Resultado: ['manzana', 'pera', 'plátano', 'kiwi', 'mango']

```` 

#EJEMPLO REST  -> Parámetros -> Agrupa

````
function mostrarFrutas(favorita, ...otrasFrutas) {
    console.log(`Mi fruta favorita es: ${favorita}`);
    console.log(`Otras frutas: ${otrasFrutas.join(', ')}`);
}

mostrarFrutas('fresa', 'uva', 'sandía', 'melón');
// Resultado:
// Mi fruta favorita es: fresa
// Otras frutas: uva, sandía, melón

