## Entorno de desarrollo

## Proyecto
1. Fichero tsconfig.json

#### 📊 Tabla de valores recomendados vs prohibidos   *(React vs SPFx)*

| Opción TS | React – Recomendado ✅ | React – Prohibido ❌ | SPFx – Recomendado ✅ | SPFx – Prohibido ❌ |
|---------|----------------------|--------------------|---------------------|-------------------|
| **`target`** | `esnext` | `es5` (salvo legacy) | `es6` | `esnext` |
| **`module`** | `esnext` | `commonjs` | `esnext` | `commonjs`, `nodenext` |
| **`moduleResolution`** | `bundler` *(Vite / Next)*<br>`node` *(Webpack)* | `nodenext` (apps) | `node` | `nodenext`, `bundler` |
| **`jsx`** | `react-jsx` | `react` | `react` | `react-jsx`, `preserve` |



2. Fichero serve.json

  ```
  "initialPage": "https://<tenant>.sharepoint.com/sites/<nombre_site>/_layouts/workbench.aspx"
  ````

### Ejecutar

```
fast-serve
npm install -g spfx-fast-serve
npm install spfx-fast-serve --save-dev
spfx-fast-serve

npm run serve
````

### Compilar y empaquetar
```
gulp clean
gulp bundle --ship
gulp package-solution --ship
```
Subir solución (sharepoint/solution/*.sppkg) al catálogo de apps

## Sharepoint Online

1. Catálogo
  https://&lt;tenant&gt;.sharepoint.com/sites/appcatalog/AppCatalog/Forms/AllItems.aspx

2. SPFX – Application Insights. Instalar el paquete Application Insights
   
```
npm para instalar @microsoft/applicationinsights-web
```
