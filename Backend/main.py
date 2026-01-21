from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import uvicorn
import os

# --- 1. SETUP ---
app = FastAPI()

# --- 1.1 CORS SETUP ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# IMPORTANT: Use environment variables for API keys
apiKey = os.getenv("GEMINI_API_KEY")
if not apiKey:
    print("Warning: GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=apiKey)

# Choose the model
model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

# --- 2. DATA MODELS ---
class ChatRequest(BaseModel):
    user_message: str
    history: str = "" # Optional: previous chat history

class ChatResponse(BaseModel):
    agent_message: str

# --- 3. THE STUDENT PERSONA ---
# This is the "System Prompt" that gives the child their personality.
# You can change this to make them "bored," "smart," or "shy."
STUDENT_PERSONA = """
You are Liam, a 10th-grade student in a classroom.
Personality: You are bored, slightly rebellious, and struggling with the subject.
Tone: Speak like a teenager. Use short sentences. Don't be overly helpful.
Goal: The teacher is trying to teach you. You engage but are reluctant.
"""

# --- 4. API ENDPOINT ---
@app.post("/api/chat", response_model=ChatResponse)
async def chat_with_student(request: ChatRequest):
    try:
        # Construct the full prompt for the LLM
        # We combine the Persona + History + New Message
        full_prompt = f"{STUDENT_PERSONA}\n\nChat History:\n{request.history}\n\nTeacher: {request.user_message}\nLiam:"

        # Call Gemini
        response = model.generate_content(full_prompt)
        
        # Get the text
        agent_text = response.text
        
        return {"agent_message": agent_text}

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)