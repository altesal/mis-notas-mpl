# Envío de documentos codificados en Base64 mediante API

1. Abrir consola de PowerShell

```
PS C:\Users\miuser> $path ="C:\Users\miuser\docs_fake\Lorem ipsum dolor sit amet.docx"
PS C:\Users\miuser> $fileBytes = [System.IO.File]::ReadAllBytes($path)
PS C:\Users\miuser> $base64 = [Convert]::ToBase64String($fileBytes)
PS C:\Users\miuser> $base64
UEsDBBQABgAIAAAAIQDfpNJsWgEAACAFAAATAAgCW0NvbnRlbnRfVHlwZXNdLnhtbCCiBAIooAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAt...
```

2. Ejemplo del body de la petición POST, por ejemplo en Postman. Body, tipo raw
```
{
  "NOMBRE": "Nombre usuario",
  "APELLIDO": "Apellido usuario",
  "PAIS": "España",
  "FILENAME": "Información general HUB.pdf",
  "FILEBASE64": "data:application/pdf;base64,JVBERi0xLjcNCiW1tbW1DQoxIDAgb2JqDQo8PC9UeXBlL0NhdGFsb2cvUGFnZ1Ob....
}
````
