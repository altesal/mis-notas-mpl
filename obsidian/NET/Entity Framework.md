
dotnet tool install --global dotnet-ef

cd MCM.API
dotnet user-secrets set "ConnectionStrings:Password" "tu_contraseña"
dotnet ef migrations add InitialCreate
dotnet ef database update

dotnet ef migrations add InitialCreate -p ../MCM.Infrastructure
Le dices explícitamente a EF Core: "El DbContext está en el proyecto MCM.Infrastructure, úsalo como referencia".

•	Capa MCM.Infrastructure 
•	Carpeta Data
•	Archivo MCMDbContext.cs
Ahí se define:
•	DbSets (Paises, Tematicas, SubTematicas, Stamps)
•	Configuración de tablas y relaciones

En una arquitectura Clean Architecture típica:
MCM.API ← Startup/Web API
MCM.Application
MCM.Domain
MCM.Infrastructure ← DbContext, configuraciones EF

## Crear la migración

Suponiendo:

- `DbContext` en `MCM.Infrastructure`
- API de arranque en `MCM.API`

Desde la carpeta de la solución o desde `MCM.API` (ojo que hay un . al final)
dotnet ef migrations add InitialCreate --project ..\MCM.Infrastructure --startup-project .

## Aplicar la migración  
(ojo que hay un . al final)
dotnet ef database update --project ..\MCM.Infrastructure --startup-project .

## Eliminar una migración fallida
dotnet ef migrations remove --project ..\MCM.Infrastructure --startup-project .

## Crear una migración nueva
dotnet ef migrations add InitialCreate --project ..\MCM.Infrastructure --startup-project .

## Aplicar la migración  
(ojo que hay un . al final)
dotnet ef database update --project ..\MCM.Infrastructure --startup-project .
