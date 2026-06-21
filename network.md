# Comandos

$ipconfig /all  -> info interesante

Servidores DNS
Dirección IPv4



- Necesitamos DNS para resolver por nombre

nslookup -> sirve para comprobar si un DNS funciona

nslookup servidor_vpn   -> =¿Qué IP tiene este nombre?

route print -> Muestra las rutas de red del equipo

- Tráfico a internet → router normal
- Tráfico a la VPN → túnel VPN

----

¿El DNS responde?
→ nslookup


¿Puedes llegar al servidor DNS?
→ ping y tracert


¿Está bien la ruta de red?
→ route print

-----------
Combinación importante: route print + ipconfig /all -> Permite ver la configuración completa de red (IP, DNS, MAC) y cómo se enruta el tráfico (tabla de rutas)

- La Columna interfaz: identifica el adaptador usado para la ruta; coincide con la dirección IP listada en ipconfig /all.