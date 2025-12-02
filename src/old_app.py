
#ORIGINAL VERSION
print("FastAPI app.py loaded")
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from fastapi import FastAPI

def load_model():
    """Load the GPT-2 tokenizer and model."""
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    return tokenizer, model


def generate_text(prompt):
    """Generate text from a prompt using GPT-2."""
    tokenizer, model = load_model()

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            temperature=0.7,
            top_k=50,
            do_sample=True
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    prompt = input("Enter a prompt: ")
    result = generate_text(prompt)
    print("\nGenerated Output:\n")
    print(result)




api = FastAPI()

@api.get("/generate")
def generate(prompt: str):
    return {"output": generate_text(prompt)}



