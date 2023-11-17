import json
import difflib
import tkinter as tk

# Cargar el conocimiento desde el archivo JSON
with open("knowledge_base.json", "r", encoding="utf-8") as knowledge_file:
    knowledge_base = json.load(knowledge_file)

preguntas = knowledge_base["preguntas"]
respuestas = knowledge_base["respuestas"]
palabras_prohibidas = knowledge_base["palabras_prohibidas"]

# Función para filtrar palabras no deseadas
def filtrar_palabras_no_deseadas(texto):
    for palabra in palabras_prohibidas:
        texto = texto.replace(palabra, "*CENSURADO*")
    return texto

# Función para obtener respuesta de la red neuronal
def obtener_respuesta_red_neuronal(pregunta):
    pregunta_cercana = difflib.get_close_matches(pregunta, preguntas)
    if pregunta_cercana:
        index_pregunta_cercana = preguntas.index(pregunta_cercana[0])
        return respuestas[index_pregunta_cercana]
    else:
        return "Lo siento, no tengo información sobre esa pregunta."

# Función para manejar la interacción en la interfaz gráfica
def manejar_interaccion():
    pregunta_usuario = entrada_usuario.get()
    pregunta_usuario = pregunta_usuario.strip()
    
    if pregunta_usuario:
        pregunta_usuario = pregunta_usuario.capitalize()
        respuesta_chatbot = chatbot(pregunta_usuario)
        print(f"Tu: {pregunta_usuario}")
        print(f"Bot: {respuesta_chatbot}\n")
        
        # Limpiar la entrada después de imprimir la pregunta y respuesta
        entrada_usuario.delete(0, 'end')
    else:
        print("Por favor, ingresa una pregunta.")

# Función para cerrar la aplicación
def cerrar_aplicacion():
    print("🌞Hasta luego que tenga un buen dia👌")
    root.destroy()

# Función principal del ChatBot
def chatbot(texto_usuario):
    texto_filtrado = filtrar_palabras_no_deseadas(texto_usuario)
    respuesta = obtener_respuesta_red_neuronal(texto_filtrado)
    return respuesta

# Mensaje de bienvenida
print("🤖Bienvenido al futuro😎")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("ChatBot GUI")

# Ajustar el tamaño predeterminado de la ventana
root.geometry("400x200")

# Crear elementos de la interfaz gráfica
etiqueta_pregunta = tk.Label(root, text="Tu:")
etiqueta_pregunta.pack()

entrada_usuario = tk.Entry(root)
entrada_usuario.pack()

boton_enviar = tk.Button(root, text="Enviar", command=manejar_interaccion)
boton_enviar.pack()

# Etiqueta de respuesta en la interfaz gráfica
etiqueta_respuesta = tk.Label(root, text="")
etiqueta_respuesta.pack()

# Agregar botón para cerrar la aplicación
boton_cerrar = tk.Button(root, text="Cerrar", command=cerrar_aplicacion)
boton_cerrar.pack()

root.mainloop()

