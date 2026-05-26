# API Search

| Source | Source Id | API Search |
| ------ | --------- | ---------- |
| Personas (user profile) | b09a7990-05ea-4af9-81ef-edfab16c4e31 |https://{tenant}.sharepoint.com/_api/search/query?querytext=%27*%27&sourceid=%27b09a7990-05ea-4af9-81ef-edfab16c4e31%27&rowlimit=80  |
| Documentos Sharepoint | 8413cd39-2156-4e00-b54d-11efd9abdb89 | /_api/search/query?querytext='report'&sourceid='8413cd39-2156-4e00-b54d-11efd9abdb89'| 
| Vídeos (Office 365 Video/Stream legacy) | 9479bf85-e257-4318-b5a2-81a180f5faa1 | /_api/search/query?querytext='training'&sourceid='9479bf85-e257-4318-b5a2-81a180f5faa1'
``|
| Contenido todo SharePoint (global) | e7ec8cee-ded8-43c9-beb5-436b54b31e84| /_api/search/query?querytext='*'&sourceid='e7ec8cee-ded8-43c9-beb5-436b54b31e84'|
| Conversaciones / social | 5dc9f503-801e-4ced-8a2c-5d1237132419 |_api/search/query?querytext='discussion'&sourceid='5dc9f503-801e-4ced-8a2c-5d1237132419' |



# Administración usuarios

Login en SharePoint Online: el usuario que inicia sesión es un usuario de Microsoft 365, es decir, una cuenta gestionada por la organización mediante Microsoft Entra ID (antes Azure AD).

Grupos O365 https://myaccount.microsoft.com/groups/groups-i-own/

## Editar los permisos de un grupo

1. Ir a los settings del site > Site permissions
2. Marcar el check del grupo
3. En la ribbon Edit User Permissions


# Llamadas API REST de SharePoint Online

```
https://<tenant>.sharepoint.com/sites/<site_url>/_api/site?$select=IsHubSite,HubSiteId  --> HUBSITE-ID

https://<tenant>.sharepoint.com/sites/<site_url>/_api/site?$select=Id  --> SITE-ID

https://<tenant>.sharepoint.com/sites/DEV-Infostat/_api/web/lists?$select=Title,Id  --> Info de listas de un site

https://<tenant>.sharepoint.com/sites/DEV-Infostat/_api/web/lists/getbytitle('NOMBRE_LISTA')/Id  -> Info de lista por Title

https://{tenant}.sharepoint.com/sites/{site}/_api/site?$select=Id  -> ID del tenant  d:Id    


``` 

# Webpart tipo Text

## Tamaño fuentes por defecto

| Size          | Nombre clase fuente                  | Elemento            |
| ------------- | ------------------------------------ | ------------------- |
| 68            | fontSizeMega rte-fontscale-font-max  |                     |
| 42            | fontSizeSuper rte-fontscale-font-max |                     |
| 36            | fontSizeXxLargePlus                  |                     |
| 32            | fontSizeXxxLarge                     |                     |
| 28            | fontSizeXxLarge                      | H2                  |
| 24            | fontSizeXLargePlus                   | H3                  |
| 20            | fontSizeXLarge                       | H4  y pull quote    |
| 18            | fontSizeLarge                        | Normal y No spacing |
| 16            | fontSizeMediumPlus                   |                     |
| 14            | fontSizeMedium                       | Monospace           |
| 12            | fontSizeSmall                        |                     |
| 10            | fontSizeXSmall                       |                     |

# PnP Modern Search - Configuración.

**PnP Search Box**
- Reset query on clear: Activat

**PnP - Search Results**
-  Available datasources: Sharepoint Search
- Query template

```
{inputQueryText}  (contentclass:STS_ListItem_DocumentLibrary  OR FileExtension:aspx) DepartmentId:<tenantId> IsDocument:true 
```
- Result Source Id / Scope|Name: LocalSharepointResults
- Page 3. Available Connections: use input query text
- Dynamic Value
- Connect al origin: PnP - Search Box
- Propietats de l'origen PnP - Search Box: Search query
- Default value: *
Connnect to a filters Web Part: Activat
- Use filters from this component: Search Filters Web Part - guid



### Documentación

- Sobre ordenar resultados de búsqueda https://blog.franckcornu.com/post/modern-search-overview-sort-control/



# Flujos de aprobación

1. Ir a la biblioteca, por ejemplo, Site Pages

2. Menú horizontal: Integrar > Power Automate > Configurar el flujo de aprobación de página > Crear flujo

- Aprobaciones estándar
- Sharepoint (permisos)
- Sharepoint (permisos)
- Notificaciones

Continuar

Nombre del flujo: Test Enviar la página de SharePoint para aprobación

Aprobadores: usuarios_aprobadores, o grupo con rol Aprobador (no Diseño, sino solo lectores)
Permisos de este grupo para la Site Page.
Site Pages -> Control de versiones, caulqueir usuraio que pueda leer elementos

3. Crear una página en blanco. Marcar check Crear como un borrador privado > Crear página

    Compartir página con el grupo de Aprobadores (rol Lectura), no como Editar. Estos deben solicitar permiso. 
    Enviar para aprobación
    Aceptar o Rechazar (con mensaje y devolución)

4. Crear una página en blanco. NO Marcar check Crear como un borrador privado

- El flujo avanza correctamente.
