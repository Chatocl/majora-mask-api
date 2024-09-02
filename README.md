# Majora Mask Chat API

Esta es una API simple construida con Flask y OpenAI que permite a los usuarios enviar preguntas y recibir respuestas generadas por modelos de lenguaje como GPT-3.5 o GPT-4. La API permite controlar la aleatoriedad de las respuestas (`temperature`) y la longitud máxima de la respuesta en tokens (`max_tokens`).

## Requisitos

- Python 3.7 o superior
- Una clave API de OpenAI

## Instalación

1. **Clonar el repositorio:**
   
   ```bash
   git clone https://github.com/tu-usuario/majora-mask-api.git
   cd majora-mask-api
   
3. **Instalar dependencias:**
   
   ```bash
   pip install -r requirements.txt
   
## Uso

1. **Iniciar el servidor:**
   Ejecuta el siguiente comando para iniciar el servidor Flask:
   
    ```bash
     pip install -r requirements.txt

3. **Realizar solicitudes:**
    Puedes enviar solicitudes POST a la API en la ruta /api/chat con el siguiente formato JSON:
   
    ```bash
      {
          "message": "Tu mensaje aquí",
          "temperature": 0.7,
          "max_tokens": 150
      }
* message: El mensaje o la pregunta que deseas enviar al modelo.
* temperature (opcional): Controla la aleatoriedad de la respuesta. Valores entre 0.0 y 1.0.
* max_tokens (opcional): Limita la longitud de la respuesta
