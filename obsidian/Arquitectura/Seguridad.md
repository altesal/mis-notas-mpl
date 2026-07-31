
OIDC -> **OpenID Connect**. Es un protocolo de autenticación moderno que se construye sobre **OAuth 2.0** y permite verificar la identidad de un usuario de forma segura.

**Microsoft Entra ID** (antes Azure Active Directory) **implementa OpenID Connect (OIDC)** como protocolo de autenticación moderno.

De hecho:

- **OIDC** → se utiliza para **autenticar** usuarios (saber quién es el usuario).
- **OAuth 2.0** → se utiliza para **autorizar** acceso a APIs y recursos.
- **Microsoft Entra ID** actúa como **Identity Provider (IdP)**, emitiendo tokens OIDC y OAuth 2.0 para aplicaciones.