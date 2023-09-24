from flask import Flask, request, render_template
import openai

app = Flask(__name__, static_folder='static')

API_KEY = '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'
openai.api_key = API_KEY

chat_log = []


# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot/chat.html')
def chatbot_index():
    return render_template('chatbot/chat.html')




@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']

    
    
    chat_log.append({"role": "user", "content":"imagina que eres un chatbot financiero para una aplicacion de un banco, estas programado unicamente para responder preguntas relacionadas, no tienes permitido hablar sobre ninguna otra cosa "})
    chat_log.append({"role": "user", "content":"se te proporcionaran opciones de inversion y de acuerdo al tiempo que el cliente quiere invertir y dependiendo de la cantidad de dinero que quiere invertir debes de elegir la mejor opcion de inversion. "})
    chat_log.append({"role": "user", "content": ''' 

Analiza la siguiente información de los fondos(planes) de inversion y comprendenla totalmente para cuando tengas que indicar que opción es la mejor:
                     
NTEDIG
Finalidad 
Solo Inversion de más de 50 pesos
Solo se puede invertir de un mes en adelante
Comisión por apertura: 1.00%
Rendimiento mensual: 10.06%

NTECT
Solo Inversion de más de 50 pesos
Solo se puede invertir de un mes en adelante
Comisión por apertura: 2.05%
Rendimiento mensual: 8.74%

NTED
Solo Inversion de más de 50 pesos
Solo se puede invertir desde un año hasta tres años
Comisión por apertura: 1.8%
Rendimiento mensual: 7.87%

NTE1
Solo Inversion de más de 50 pesos
Solo se puede invertir por tres años en adelante
Comisión por apertura: 2.10%
Rendimiento mensual: 0.44%

NTE2
Solo Inversion de más de 50 pesos
Solo se puede invertir por tres años en adelante
Comisión por apertura: 2.20%
Rendimiento mensual: 0.44%

NTE3
Solo Inversion de más de 50 pesos
Solo se puede invertir por tres años en adelante
Comisión por apertura: 2.30%
Rendimiento mensual: 0.47%

NTEDLS
Solo Inversion de más de 50 pesos
Solo se puede invertir por un año en adelante
Comisión por apertura: 1.75%
Rendimiento mensual: 0.02%

NTEDLS+
Solo Inversion de más de 50 pesos
Solo se puede invertir por dos años en adelante
Comisión por apertura: 1.35%
Rendimiento mensual: 0.21%

NTEIPC+
Solo Inversion de más de 50 pesos
Solo se puede invertir desde tres años hasta cinco años
Comisión por apertura: 2.50%
Rendimiento mensual: 1.21%

NTEPZO
Solo Inversion de más de 50,000 pesos
Solo se puede invertir por tres meses en adelante
Comisión por apertura: N/A
Rendimiento mensual: 2.70%
                                          
'''})
    chat_log.append({"role": "user", "content":"despues analiza los datos que proporciono el usuario, para poder proporcionar un fondo de inversion adecuado"})

    
    if user_message.lower() == "adios":
        return "Adiós"
    
    

    chat_log.append({"role": "user", "content": user_message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )

    assistant_response = response['choices'][0]['message']['content']
    chat_log.append({"role": "assistant", "content": assistant_response})

 
    
    return assistant_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)