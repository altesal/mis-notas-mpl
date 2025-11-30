
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
npm create vite@latest  #Elegimos vanilla y js
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
    "extends": "./node_modules/standard/eslintrc.json"
}
````
## 3. Comenzamos la app

Creamos fichero App.jsx

Lo importamos en el main.jsx



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

