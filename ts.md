# Requisitos

node -v
npm -v

# Instrucciones

1. Repositorio git. Carpeta proyecto

2. Inicializar npm

    ```
    npm init -y

    ```

3. Instalar TypeScript

    ```
    npm install --save-dev typescript

    ```

4. Generar el archivo de configuración tsconfig.json

    ```
    npx tsc --init
    ```

5. Compilar y ejecutar

    ```
    npx tsc
    node dist/index.js        
    ```

### Ejemplo fichero tsconfig.json
```
{
  "compilerOptions": {
    "target": "es6",
    "module": "esnext",
    "moduleResolution": "node",
    "jsx": "react",
    "noImplicitAny": false,
    "sourceMap": true,
    "outDir": "./dist"    
  },
  "include": [
    "src/**/*"
  ],
  "exclude": [
    "node_modules"
  ]
}
``` 

### Ejemplo package.json

```
{
  "name": "only-ts",
  "version": "1.0.0",
  "description": "Template for TypeScript projects",
  "main": "dist/app.js",
  "scripts": {
    "start": "node dist/app.js",
    "compile": "tsc -b",
    "compile:watch": "tsc -b --watch",
    "test": "echo \"Error: no test specified\" && exit 1",
    "check-updates": "ncu -u"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "npm-check-updates": "^16.7.10",
    "typescript": "^5.9.3"
  }
}
```

