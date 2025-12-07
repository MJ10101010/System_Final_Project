# Systems Final Project - Michelle's LLM Chat

## 1) Executive Summary
- **Problem:** Users and students need a simple, accessible interface to explore and interact with a Large Language Model (LLM) for text generation and instruction following, without relying on complex external APIs or paid services.
- **Solution:** This project creates a personal, private AI chat experience that allows users to interact with a smart language model directly on their own computer. Instead of connecting to a remote server or paid cloud service, the entire application—from the intelligent "brain" (a fine-tuned version of GPT-2) to the colorful user interface—is packaged together in a way that is easy to download and run. By bringing this technology down to the local level, it offers a hands-on way to explore how computers generate text and follow instructions, prioritizing data privacy and simplicity so that students and enthusiasts can understand the building blocks of modern AI without needing complex technical setups.

## 2) System Overview
**Course Concepts:** 
- LLM serving
- Containerization with Docker
- FastAPI
- Communicate with a locally hosted LLM using HTTP
- Model health via /api/health

**Architecture Diagram:**
![Architecture Diagram](assets/architecture.png)

**Data/Models/Services:**
- **Model:** `vicgalle/gpt2-open-instruct-v1` (derived from GPT-2, fine-tuned on Open Instruct dataset)
- **Service:** FastAPI backend serving the model and static files
- **Frontend:** HTML
- *No private data or user-specific information is used

## 3) How to Run (Local)
### Docker

```bash
# Build the container
docker build -t gpt2-app:latest .

# Run the container
docker run -p 8000:5000 michellejar10/gpt2-app

# Health check
curl http://localhost:8000/health

Then open:
http://localhost:8000
```


## 4) Design Decisions
**Why this concept?**
I chose to host a local LLM to demonstrate the capability of serving transformer models within a lightweight containerized environment. This avoids the latency and cost of external APIs like OpenAI, maintaining data privacy. GPT-2 was selected as a small, free, and open model that is easy to host inside a container.

**Alternatives considered:**
- *Flask:* Simpler but slower and less ergonomic for async APIs
- *vLLM or Hugging Face Text Generation Inference:* More performant but unnecessarily large for a single-container assignment
- *Larger LLMs:* Would exceed Docker image size limits and RAM constraints

**Tradeoffs:**
- *Performance vs. Quality:* GPT-2 is faster and lighter than Llama 3 but produces lower quality text
- *Complexity:* Running the model inside the app container is simpler than a separate inference server (e.g., TGI/vLLM) but scales poorly

**Security & Privacy:**
- No secrets stored in code
- No user data is stored persistently
- Input validation ensured non-empty prompts

**Ops:**
- Logs are output to stdout/stderr for Docker monitoring
- Scalability is limited by CPU inference speed (single worker)

## 5) Results & Evaluation

**Sample Output:**
![Sample Output](assets/sample_output.png)

## 6) What’s Next
**I plan to improve:**
- Model Upgrade from GPT-2
- GPU Acceleration
- Chat History
- Further embellish UI

## 7) Links
**GitHub Repo:** https://github.com/MJ10101010/System_Final_Project
