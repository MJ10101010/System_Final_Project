from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pathlib
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI(title="GPT-2 Text Generator")

# Get root folder (parent of src/)
root_dir = pathlib.Path(__file__).parent.parent.resolve()

# Mount /static from root/static
app.mount("/static", StaticFiles(directory=root_dir / "static"), name="static")

# Serve index.html from root/template/index.html
@app.get("/", response_class=HTMLResponse)
async def root():
    path = pathlib.Path(__file__).parent.parent / "template" / "index.html"
    return path.read_text(encoding="utf-8")

class Prompt(BaseModel):
    text: str

device = torch.device("cpu")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2").to(device)

def generate_text(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            temperature=0.7,
            top_k=50,
            do_sample=True
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/generate")
def generate_endpoint(prompt: Prompt):
    text = prompt.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Empty prompt")
    output = generate_text(text)
    return {"output": output}