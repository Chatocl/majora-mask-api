from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

client = OpenAI(api_key='TuClaveAPIdeOpenAI')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Extrae el mensaje y los parámetros opcionales del cuerpo de la solicitud
        data = request.json
        user_message = data.get('message')
        temperature = data.get('temperature', 0.5)  
        max_tokens = data.get('max_tokens', 2000)  

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Llama a la API de OpenAI para generar una respuesta
        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Al iniciar, apareceremos en un bosque con una única salida (una cueva en un árbol). Debemos entrar por ella y luego atravesar la siguiente zona saltando sobre unos troncos de árbol."},
                {"role": "system", "content": "Después de esto, caemos a un precipicio y hay una cinemática donde Skull Kid nos convierte en un Deku y conocemos a Tatl."},
                {"role": "system", "content": "Debemos acercarnos a la puerta, abrirla y seguir el camino."},
                {"role": "system", "content": "Utilizaremos las flores rosadas, Flor Deku, en el piso. Con Link Deku al estar encima y pulsar A podremos planear por un momento. Utiliza esto y llega a la siguiente puerta."},
                {"role": "system", "content": "En la siguiente habitación se realiza lo mismo hasta llegar a la siguiente zona en donde entraremos a Ciudad Reloj o Clock Town."},
                {"role": "system", "content": "Aparecemos en una habitación donde debemos seguir el camino de madera y llegaremos arriba donde hay una puerta de madera. Al intentar cruzar habrá una cinemática donde conocemos al vendedor de máscaras felices."},
                {"role": "system", "content": "Luego de la cinemática, él nos propone un trato donde debemos recuperar la máscara de Majora de Skull Kid. Sal por la puerta y estaremos en Ciudad Reloj."},
                {"role": "system", "content": "Nuestro objetivo es volver a convertirnos en Link, por lo que debemos hacer los siguientes pasos:"},
                {"role": "system", "content": "Estando en Ciudad Reloj estaremos en una plaza, esta es al sector sur. Avanzando por donde hay un guardia hay unas escaleras con un buzón, subiendo por allí llegamos al lavadero."},
                {"role": "system", "content": "En el lavadero hay un hada, con Link Deku podremos dar saltitos en el agua, hay que tomar el hada posicionándonos encima."},
                {"role": "system", "content": "Luego debemos ir al sector norte de Ciudad Reloj volviendo por donde venimos y detrás de la torre del reloj estará la puerta."},
                {"role": "system", "content": "En la sección norte vamos a ir a la cueva de la Gran Hada donde entregaremos al hada que recogimos y nos dará la magia."},
                {"role": "system", "content": "Una vez con la magia podremos tirar burbujas. Saliendo de la cueva de la Gran Hada disparamos al globo azul con la máscara. Disparamos con el botón Z y B."},
                {"role": "system", "content": "Una vez hecho esto hablaremos con el niño de gorra roja, el cual nos hará jugar un minijuego de capturar a 5 niños repartidos por la ciudad."},
                {"role": "system", "content": "Deberemos buscarlos a todos: En el sector norte hay dos. Uno detrás del árbol y otro detrás de unos juegos."},
                {"role": "system", "content": "En el sector sur no hay ninguno, por lo que debemos ir al sector este donde hay 2. Uno está sobre el tejado de la posada, por lo que hay dos formas de alcanzarlo: utilizando la flor Deku o entrando a la posada y subiendo al segundo nivel. Si es de noche, dependiendo de la hora, no podremos ingresar."},
                {"role": "system", "content": "El segundo estará sobre un edificio con una gallina; al acercarnos a él, saltará y tendremos que correr detrás de él."},
                {"role": "system", "content": "El último niño está en el sector oeste; el área es corta, por lo que no es tan complicado."},
                {"role": "system", "content": "Una vez capturados todos, saltará una cinemática de los niños dándonos un código; recordarlo."},
                {"role": "system", "content": "Con el código podremos ir al sector oeste y hablar con un niño de gorro amarillo, y al entregar el código pasaremos a una habitación con un canal de agua."},
                {"role": "system", "content": "Avanzando con cuidado de los enemigos y de no ahogarnos, llegaremos a una escalera con un globo. Hay que explotarlo disparándole una burbuja. Subiendo llegaremos a un observatorio."},
                {"role": "system", "content": "En el observatorio hay que subir y hablar con un anciano."},
                {"role": "system", "content": "Tras hablar con el anciano podremos utilizar el telescopio, donde deberemos apuntar a la cima de la torre del reloj, donde estará Skull Kid, y veremos una pequeña cinemática donde la luna deja caer una lágrima."},
                {"role": "system", "content": "Deberemos salir por la puerta que está frente al telescopio y recoger la lágrima de luna."},
                {"role": "system", "content": "Una vez con la lágrima de luna, podemos regresar al observatorio y seguir el camino de regreso por el canal de agua hasta volver a Ciudad Reloj."},
                {"role": "system", "content": "Una vez tenemos la lágrima de luna, debemos ir al sector sur y acercarnos a una flor amarilla que está cerca de la puerta donde entramos por primera vez."},
                {"role": "system", "content": "Allí hablaremos con un Deku y le daremos la lágrima de luna."},
                {"role": "system", "content": "Una vez le hayamos dado la lágrima de luna, él nos entregará la flor Deku y podremos usarla para llegar a la parte de arriba de la puerta de la torre de reloj."},
                {"role": "system", "content": "En este sector debemos estar hasta las 12 de la noche del tercer día, donde se abrirá la puerta debajo del reloj."},
                {"role": "system", "content": "Debemos entrar por allí y saltará una cinemática con Skull Kid."},
                {"role": "system", "content": "Una vez terminada la cinemática, Skull Kid se quedará quieto en el aire y debemos dispararle con una burbuja."},
                {"role": "system", "content": "Una vez disparamos con la burbuja, él soltará la ocarina y la recogeremos."},
                {"role": "system", "content": "Una vez la recogemos, nos saltará una cinemática donde la Princesa Zelda nos enseñará la canción del tiempo."},
                {"role": "system", "content": "Una vez fuera de la cinemática, deberemos tocar la canción del tiempo y con esto terminaremos la primera parte del juego."},
                {"role": "system", "content": "Una vez de regreso, estaremos con el vendedor de máscaras felices y nos enseñará la canción de la curación para volver a ser Link."},
                {"role": "system", "content": "Para abrir el menu se debe apretar el start y con Z y L nos moveremos por las pantallas. Para seleccionar un objeto debemos posicionarnos sobre el y con las los botones amarillos (C) seleccionar un espacio. Una vez hecho esto lo tendremos equipado. Al salir del menú podremos utilizarlo al presionar el boton correspondiente."},
                {"role": "system", "content": "Para llegar allí es posible hacerlo mediante un glitch. Debes posicionarte en la esquina derecha de las gradas debajo de la plataforma y presionando Z, presionar el botón de A y moverte hacia atrás para realizar un backflip e inmediatamente moverte para adelante. "},
                {"role": "system", "content": "El codigo es distinto para cada ranura del juego por lo que no podría darte esa información."},
                {"role": "user", "content": user_message}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        # Extrae la respuesta generada por la IA
        assistant_message = chat_completion.choices[0].message.content
        # Devuelve la respuesta generada por la IA
        return jsonify({'response': assistant_message}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
