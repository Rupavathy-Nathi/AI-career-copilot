from backend.services.ai_gateway import ask_ai

def improve_resume(text):
    prompt = f"Improve this resume:\n{text}"
    return ask_ai(prompt)
