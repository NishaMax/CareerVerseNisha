# 🎓 CareerVerse - AI-Powered Career Exploration Platform

An immersive career exploration platform combining React frontend, FastAPI backend with Google Gemini AI, and Unity WebGL simulation.

## 🏗️ Project Structure

```
CareerVerse/
├── Frontend/              # React + Vite application
│   ├── src/
│   │   ├── pages/        # Home, About pages
│   │   └── components/   # Reusable components
│   └── public/
│       └── simulation/   # Unity WebGL build (deployed)
├── Backend/              # FastAPI + Gemini AI
│   ├── main.py          # API endpoints
│   └── requirements.txt # Python dependencies
└── SDGP Teacher Role/   # Unity source project (not deployed)
```

## 🚀 Local Development

### Prerequisites
- Node.js 18+
- Python 3.11+
- Unity 2022+ (for rebuilding simulation)

### Frontend Setup
```bash
cd Frontend
npm install
npm run dev
```
Runs on `http://localhost:5173`

### Backend Setup
```bash
cd Backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
Runs on `http://localhost:8000`

### Unity Development
1. Open `SDGP Teacher Role` in Unity
2. Make changes
3. Build for WebGL to `Frontend/public/simulation/`
4. Update `ChatManager.cs` with backend URL if needed

## 🌐 Deployment

- **Frontend**: Deployed on Vercel
- **Backend**: Deployed on Render
- **Auto-deploys**: Push to GitHub triggers automatic deployment

See `deployment_guide.md` for detailed instructions.

## 🎮 Features

- Interactive career simulations
- AI-powered virtual student (Liam) using Google Gemini
- Real-time chat with AI in Unity simulation
- Beautiful responsive UI with dark mode
- 5 career paths: Developer, Teacher, Game Designer, Doctor, Lawyer

## 🛠️ Tech Stack

- **Frontend**: React, Vite, TailwindCSS
- **Backend**: FastAPI, Python, Google Gemini AI
- **Simulation**: Unity WebGL, C#
- **Hosting**: Vercel (Frontend), Render (Backend)

## 📝 License

Educational project for SDGP course.
