# Crear Page

1. Ir a Settings > Pages
2. seleccionar rama y carpeta, por ejemplo /(root)

# Crear Gist

1. Ir a  https://gist.github.com
2. Crear un gist con nombre de archivo config.json y contenido: 

```
{
  "FLOW_URL": "https://prod-XX.westeurope.logic.azure.com:443/workflows/..."
}
```
3. Marcar el Gist como Secret (privado)
<script src="https://gist.github.com/altesal/aabd3ad46b5d6ad434c5c18a95fee598.js"></script>

# Generar un token personal para acceder al Gist

1. Ir  a GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic).

2. Crear un token con permisos gist.

