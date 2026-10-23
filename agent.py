from agents import Agent, Runner

agent = Agent(
    name="Data Engineer AI",
    instructions="""
    Eres un ingeniero de datos especializado en
    Python, SQL, AWS y arquitecturas de datos.

    Tu función es ayudar a analizar problemas
    de ingeniería de datos.

    Explica tus decisiones técnicas.
    No inventes resultados de ejecuciones.
    Responde en español.
    """
)

def main():
    print("Data Engineer AI Agent")
    print("Escribe 'salir' para terminar.\n")

    while True:
        pregunta = input("Tú: ").strip()

        if pregunta.lower() == "salir":
            break

        if not pregunta:
            continue

        resultado = Runner.run_sync(agent, pregunta)
        print(f"\nAgente: {resultado.final_output}\n")


if __name__ == "__main__":
    main()

