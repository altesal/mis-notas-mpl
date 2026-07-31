Paso 1: Obtener el UserSecretsId
cd MCM.API
dotnet user-secrets init

Paso 2: Guardar la contraseña en User Secrets
dotnet user-secrets set "ConnectionStrings:Password" "TU_CONTRASEÑA_AQUI"

Paso 3: Verificar que se guardó
dotnet user-secrets list
La contraseña se guardará en:
C:\Users\{TuUsuario}\AppData\Roaming\Microsoft\UserSecrets\{UserSecretsId}\secrets.json


"Server=tcp:mplserver.database.windows.net,1433;Initial Catalog=mcmbbdd;Persist Security Info=False;User ID=mplmcm;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"

dotnet user-secrets set "ConnectionStrings:DefaultConnectionMCM" "Server=tcp:mplserver.database.windows.net,1433;Initial Catalog=mcmbbdd;Persist Security Info=False;User ID=mplmcm;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"



