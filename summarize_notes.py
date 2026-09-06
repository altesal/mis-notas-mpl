import os
from dotenv import load_dotenv
import certifi
import httpx
from openai import OpenAI

# cargar variables de entorno
load_dotenv()

# Asegurar certificados SSL
os.environ["SSL_CERT_FILE"] = certifi.where()

# Crear cliente HTTP con certificados
http_client = httpx.Client(
    verify=False,           # ya sabemos que tu red rompe SSL
    follow_redirects=True   # 🔥 clave para el 302
)


#Cliente de OpenAI con el cliente HTTP personalizado

client = OpenAI(
    http_client=httpx.Client(
        verify=False,
        follow_redirects=True
    )
)


INPUT_DIR = "obsidian"
OUTPUT_DIR = "summaries"

os.makedirs(OUTPUT_DIR, exist_ok=True)
def summarize(text):
    response = client.responses.create(

    model="gpt-4.1-mini",
    input=f"""
        Resume estas notas en formato Markdown bien estructurado.

        Incluye:
        - Título
        - Secciones con encabezados (##)
        - Listas con bullets
        - Ejemplos si aplica

        Notas:
        {text}
        """
    )

    return response.output_text

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".md"):
        path = os.path.join(INPUT_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        print(f"Procesando {filename}...")

        summary = summarize(content)

        output_path = os.path.join(OUTPUT_DIR, f"summary_{filename}")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)

print("✅ Resúmenes generados en /summaries")
