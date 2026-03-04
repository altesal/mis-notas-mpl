## Entorno de desarrollo

## Crear proyecto  - Verificar versiones antes de crear

```
PS C:\repos> node -v
v18.19.1
PS C:\repos\carpeta_proyecto> npm install -g yo@4.3.1
PS C:\repos\carpeta_proyecto> npm install -g gulp-cli@2.3.0
PS C:\repos\carpeta_proyecto> npm install -g @microsoft/generator-sharepoint@1.19.0
PS C:\repos\carpeta_proyecto> npm install  -g spfx-fast-serve@^4.0.2

PS C:\repos\carpeta_proyecto> yo --version
4.3.1
PS C:\repos\carpeta_proyecto> npm ls -g --depth=0 @microsoft/generator-sharepoint
C:\Program Files\nodejs -> .\
└── @microsoft/generator-sharepoint@1.19.0

PS C:\repos\carpeta_proyecto> node -v
v18.19.1
PS C:\repos\carpeta_proyecto> gulp -v
CLI version: 2.3.0
Local version: 4.0.2



PS C:\repos\carpeta_proyecto> yo @microsoft/sharepoint
```
Rellenar el asistente con estas opciones (modelo típico):

- SharePoint Online only (latest)
- WebPart
- Nombre del proyecto
- Descripción
- Framework: React o No JavaScript Framework
- Nombre del WebPart
- Descripción del WebPart


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
