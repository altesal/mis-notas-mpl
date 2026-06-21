import os
import numpy as np
import faiss
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

DATA_DIR = "obsidian"

docs = []
texts = []

# 1. Leer archivos
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".md"):
        path = os.path.join(DATA_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            docs.append(filename)
            texts.append(content)

# 2. Crear embeddings
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

embeddings = [get_embedding(t) for t in texts]
embeddings_np = np.array(embeddings).astype("float32")

# 3. Indexar con FAISS
index = faiss.IndexFlatL2(len(embeddings_np[0]))
index.add(embeddings_np)

# 4. Función de búsqueda
def search(query, k=3):
    q_emb = np.array([get_embedding(query)]).astype("float32")
    distances, indices = index.search(q_emb, k)
    return [texts[i] for i in indices[0]]

# 5. Chat
def ask(query):
    context = "\n\n---\n\n".join(search(query))

    prompt = f"""
Usa SOLO la información de abajo para responder:

{context}

Pregunta:
{query}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output[0].content[0].text


# Loop interactivo
while True:
    q = input("\nPregunta (o 'exit'): ")
    if q == "exit":
        break

    answer = ask(q)
    print("\n💬 Respuesta:\n", answer)