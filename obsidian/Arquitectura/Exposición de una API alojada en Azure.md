Camino de despliegue y exposición de una API alojada en Azure hasta que queda accesible desde Internet.

# Visión ejecutiva

La API se desarrolla en .NET, se despliega en Azure mediante infraestructura como código (Terraform) y se publica inicialmente en entornos internos (PRE y PRO). Posteriormente se conecta a la red corporativa del cliente mediante peering y, finalmente, si debe ser accesible desde Internet, pasa por los controles de red y seguridad perimetral antes de ser publicada.

El proceso implica normalmente cuatro equipos:

1. **Equipo de Arquitectura / Desarrollo**
2. **Equipo Cloud**
3. **Equipo de Redes**
4. **Equipo de Perímetro / Publicación Internet**

---

# 1. Construcción de la solución en Azure

## Responsabilidad

Equipo de Arquitectura Local.

## Qué crea

Mediante Terraform se aprovisionan recursos Azure como:

- App Service
- App Service Plan
- Private Endpoint / Private Link
- Key Vault
- Resource Groups
- Storage Accounts
- Monitoring (Application Insights)
- Networking
- Otros recursos auxiliares

En el esquema aparece "12-13 recursos más", que es algo habitual porque una API empresarial suele requerir bastante infraestructura de soporte.

## Resultado

Se dispone de una infraestructura repetible y automatizada.

Terraform  

↓  

Azure Resources  

↓  

API .NET desplegada  

---

# 2. Separación de entornos PRE y PRO

## Responsabilidad

Equipo Cloud. "2 suscripciones para Preproducción y Producción"

---
# 3. Integración con la red corporativa

Una vez desplegada la API, todavía puede estar aislada dentro de Azure. Ahora entra el equipo de redes.

## Responsabilidad

Equipo de Redes.

En el esquema aparece:

> "Punto central de interconexión de la red corporativa"

Este equipo gestiona:

- conectividad
- routing
- segmentación
- seguridad perimetral
- acceso Internet

Su pregunta principal es:

> ¿Cómo llega el tráfico desde la red corporativa a la red Azure donde está la API?

---

# 4. Peering de redes

Se conecta la red Azure (VNet) donde vive la API con otra red corporativa o de cliente.

Normalmente mediante:

- VNet Peering
- Hub & Spoke
- ExpressRoute
- VPN Site-to-Site

(según arquitectura del cliente)

## Objetivo

Que los sistemas corporativos puedan alcanzar la API. Si el peering no está correctamente configurado:

- no hay rutas
- no hay resolución DNS
- la aplicación no es accesible

---

# 5. Servicios levantados

Cuando el peering está validado: Significa que:

- infraestructura creada
- aplicación desplegada
- conectividad validada

La API ya puede estar funcionando.
Pero todavía no necesariamente está publicada a Internet.
**Servicio operativo ≠ servicio publicado externamente**

---

# 6. Apertura de firewall (opcional)

### 443 
Es HTTPS -> API
### 22
SSH
En arquitecturas modernas de Azure PaaS (App Service) muchas veces no es necesario exponerlo.
Podría corresponder a:
- bastiones
- máquinas virtuales
- operaciones de administración

---
# 7. Bastión de acceso

El esquema comenta:

> "Se puede poner un bastión y acceder sin que se hayan publicado"

Esto es importante.

## Bastion

Azure Bastion permite acceder a recursos internos sin exponerlos directamente a Internet.

Ventajas:

- acceso administrativo seguro
- evita IPs públicas innecesarias
- permite validar despliegues antes de publicar

Arquitectónicamente suele ser una buena práctica.

---

# 8. Publicación en Internet

Probablemente se refiere al equipo de: (depende de la organización)

- Redes
- Seguridad Perimetral
- Infraestructura Corporativa

---

## Qué hacen realmente

### DNS

Crean registros DNS.

api.empresa.com  

Mostrar más líneas

apuntando al servicio correcto.

---

### Certificados

Instalan o validan:

Plain Text

TLS / SSL  

Mostrar más líneas

para HTTPS.

---

### Balanceadores o Proxies

Muchas veces hay:

- Reverse Proxy
- Load Balancer
- Application Gateway
- F5
- WAF

entre Internet y la API.

---

### Publicación controlada

Definen:

- qué URL se publica
- desde dónde se puede acceder
- qué puertos están permitidos
- qué tráfico se bloquea

---

# Flujo completo simplificado


![[Pasted image 20260707123236.png]]

# Resumen

> "La solución se aprovisiona mediante Terraform sobre Azure App Service en suscripciones separadas de PRE y PRO. Posteriormente se integra con la red corporativa mediante peering, se validan rutas y conectividad, y finalmente el equipo de networking/perímetro publica el servicio externamente mediante DNS, certificados, reglas de firewall y, si aplica, elementos de seguridad como WAF o Application Gateway."

