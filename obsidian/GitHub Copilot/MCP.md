Cursor, GitHub Copilot, etc -> AI generation tools for code (herramientas de generación de IA para código)


Model Context Protocol
- Expone al chat de GitHub Copilot un conjunto de herramientas y un servicio de terceros
- Por ejemplo, un tercero puede ser nuestra bbdd Neon
- GitHub Copilot puede interactuar, usando esas herramientas, con ese servicio de terceros
- Instalamos nuestro servidor MCP para Neon, y se expondrán una lista de herramientas: 
		- listar todos nuestros proyectos Neon:
		- ejecutar instrucciones SQL
		- 
- En las extensiones de VS Code, instalar la de Neon
	@mcp neon