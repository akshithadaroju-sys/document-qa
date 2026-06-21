from llama_cpp import Llama

llm = Llama(
    model_path="models/tinyllama-1.1b-chat-v1.0-q4_k_m.gguf",
    n_ctx=2048,
    verbose=False
)

def ask_llm(prompt):
    response = llm(
        prompt,
        max_tokens=200,
        temperature=0.2
    )

    return response["choices"][0]["text"]