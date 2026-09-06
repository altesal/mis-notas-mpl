Un MCP es la "Embajada" de un servicio
Un servidor MCP no sustituye la API, el dominio o los casos de uso de una apliación. 
Un servidor MCP presenta las capacidades de una API, un servicio, etc. mediante un contrato común

https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro 


Terminal 1
==============
PS C:\Users\mjped> python -m http.server 9000
Serving HTTP on :: port 9000 (http://[::]:9000/) ...

Keyboard interrupt received, exiting.

Terminal 2
=================
C:\Users\mjped>netstat -ano | findstr :6173
  TCP    0.0.0.0:6173           0.0.0.0:0              LISTENING       23468
  TCP    0.0.0.0:6173           0.0.0.0:0              LISTENING       2104
  TCP    [::]:6173              [::]:0                 LISTENING       2104
  TCP    [::]:6173              [::]:0                 LISTENING       23468

C:\Users\mjped>tasklist /FI "ID eq 23468"
Error: No se reconoce el filtro de búsqueda.

C:\Users\mjped>tasklist /FI "PID eq 23468"

Nombre de imagen               PID Nombre de sesión Núm. de ses Uso de memor
========================= ======== ================ =========== ============
python.exe                   23468 Console                   12    23.432 KB

minuto 21:35