Transformers -> Un **Transformer** es una arquitectura de red neuronal diseñada para procesar secuencias (como texto) que está en el corazón de los **LLMs (Large Language Models)** como GPT.
Un Transformer es un modelo que:
- Lee una secuencia (palabras, tokens…)
- Aprende **qué partes son importantes entre sí**
- Y genera un resultado (por ejemplo, la siguiente palabra)
👉 La clave: usa un mecanismo llamado **atención (attention)** para decidir en qué fijarse.
![[Pasted image 20260621194629.png]]


# ¿Qué es un Transformer (idea intuitiva)?

Un Transformer es un modelo que:

- Lee una secuencia (palabras, tokens…)
- Aprende **qué partes son importantes entre sí**
- Y genera un resultado (por ejemplo, la siguiente palabra)

👉 La clave: usa un mecanismo llamado **atención (attention)** para decidir en qué fijarse.

---

# 🏗️ Estructura del Transformer (según la imagen)

En la imagen aparece el diseño clásico:

## 1. **Embeddings + Positional Encoding**

Abajo del todo:

- **Input Embedding**: convierte palabras en vectores numéricos.
- **Positional Encoding**: añade información de orden (porque el modelo no “ve” el orden por sí mismo).

📌 Ejemplo:

> "gato come pescado" ≠ "pescado come gato"

---

## 2. **Encoder (lado izquierdo)**

Bloques repetidos **N veces** (Nx en la imagen):

Cada bloque tiene:

- **Multi-head attention**
- **Feed Forward**
- **Add & Norm** (normalización + conexiones residuales)

### 🔍 Qué hace el encoder:

Convierte la frase en una representación rica donde cada palabra:

- "entiende" las demás palabras
- capta contexto

👉 Ejemplo: En `"banco"` puede entender si es dinero o un asiento según el contexto.

---

## 3. **Decoder (lado derecho)**

También repetido **N veces**, pero con un extra:

- **Masked Multi-head Attention** (solo mira al pasado)
- **Multi-head Attention** con el encoder
- **Feed Forward**

### 🔍 Qué hace el decoder:

Genera la salida palabra por palabra.

👉 Ejemplo: Va produciendo:

```
El gato → El gato come → El gato come pescado
```

---

## 4. **Salida (Output)**

Arriba del todo:

- **Linear**
- **Softmax → Output Probabilities**

Esto da probabilidades de la siguiente palabra.

---

# ⚡ Lo más importante: la Atención (Attention)

El corazón del Transformer.

Permite al modelo:

- fijarse en palabras relevantes
- ignorar las irrelevantes

📌 Ejemplo:

> "El gato que estaba en el tejado saltó"

Para "saltó", el modelo presta atención a "gato", no a "tejado".

---

# 🧩 ¿Qué significa “Multi-Head”?

- Son múltiples “atenciones” en paralelo
- Cada una aprende relaciones distintas

👉 Ejemplo:

- una mira sintaxis
- otra semántica
- otra dependencias largas

---

# 🤖 ¿Por qué es tan importante?

Antes:

- RNN / LSTM → lentos, secuenciales

Ahora:

- Transformers → **paralelizables + más potentes**

👉 Resultado:

- GPT
- BERT
- Claude
- Copilot

TODOS usan Transformers.

---

# 🧪 Simplificación extrema

Un Transformer es:

> "Un modelo que mira todas las palabras a la vez y decide cuáles son importantes entre sí para entender y generar texto."

---

# 💡 En contexto de LLMs

- GPT → solo usa el **decoder**
- BERT → solo usa el **encoder**
- Otros modelos → encoder + decoder