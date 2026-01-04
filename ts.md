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