### Frontend + Lógica

- **Next.js** (App Router)
    - Gratis
    - Login, páginas, formularios y calendario en una sola app
    - Preparado para futura API (Fase 2)

### Base de datos

- **MongoDB Atlas Free Tier**
    - Gratis para empezar
    - Encaja perfectamente con Next.js

### Autenticación

- **Auth.js (antes NextAuth.js)**
    - Gratis
    - Login por email con **código OTP** (one-time password)
    - JWT integrado
    - Duración de sesión configurable

### Envío de emails

- **Resend**
    - Plan gratuito suficiente para arrancar
    - Envío del código de acceso por email (Gmail, Hotmail, Outlook, etc.)

### Calendario

- **FullCalendar**
    - Muy popular
    - Fácil colorear eventos:
        - 🔴 Rojo: necesidad sin cubrir ≤ 15 días
        - 🟡 Amarillo: necesidad sin cubrir > 15 días
        - 🟢 Verde: necesidad cubierta

### UI

- **Tailwind CSS**
    - Gratis
    - Rápido para construir pantallas limpias

### Roles

Tres roles en MongoDB:

- **Admin**
    - CRUD completo
    - Gestión de pacientes, voluntarios y necesidades
- **Voluntario**
    - Ver y cubrir necesidades
- **Paciente** (opcional como usuario)
    - Sólo consulta de sus necesidades


### Modelo de datos mínimo
Users  
- id  
- nombre  
- email  
- role (admin, volunteer)  

Patients  
- id  
- nombre  
- direccion  
- necesidad  
- fechaNecesidad  
  
Assignments  
- id  
- patientId  
- volunteerId  
- cubierta  
- fechaCobertura
### Despliegue
- **Vercel (free)**
    - Integración directa con Next.js
    - Despliegue en minutos
### Arquitectura recomendada (Fase 1)
Next.js  

├─ Páginas  

├─ Auth.js (JWT + OTP email)  

├─ Server Actions  

└─ MongoDB Atlas  

  

Resend  

└─ Envío de códigos login