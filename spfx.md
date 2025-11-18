## Entorno de desarrollo

## Proyecto
1. Fichero serve.json

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
  https://<tenant>.sharepoint.com/sites/appcatalog/AppCatalog/Forms/AllItems.aspx

2. SPFX – Application Insights. Instalar el paquete Application Insights
   
```
npm para instalar @microsoft/applicationinsights-web
```
