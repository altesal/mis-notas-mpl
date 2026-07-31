Probar una API publicada en Azure
En la web app, API, permitir CORS

En el Entra ID tenemos una App registrada
En el menú Authentication > Redirect URI configuration, dar de alta un registro de tipo Mobile and desktop applications, marcando el check `msalclienteID-app-registrada://auth` (MSAL only)



Postman
Authorization
	Auth TYpe= OAuth 2.0
	Token Name= NOmber del token
	Header prefix=Bearer
	Callback url = https://login.microsoftonline.com/{tenantID}/oauth2/v2.0/authorize
	Access token url = https://login.microsoftonline.com/{tenantID}/oauth2/v2.0/token
	ClientID = clientid-de la app registrada
	ClientSecret = vacío
	Code Challenge Method =SHA-256
	scope=api://clientId-app-registrada/access_as_user   (ver esto en el entraid para la app registrada)
GET NEW ACCESS TOKEN