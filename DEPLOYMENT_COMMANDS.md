# CareerVerse - GitHub Setup & Deployment Commands

## 📦 Initial GitHub Setup

### Step 1: Initialize Git
```bash
cd "d:\Oroginal Project SDGP CareerVerse"
git init
git add .
git commit -m "Initial commit: Frontend, Backend, and Unity WebGL build"
```

### Step 2: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `CareerVerse`
3. Description: "AI-Powered Career Exploration Platform"
4. Make it **Public** or **Private** (your choice)
5. **DON'T** initialize with README (we already have one)
6. Click "Create repository"

### Step 3: Push to GitHub
```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/CareerVerse.git
git branch -M main
git push -u origin main
```

---

## 🚀 Deploy to Vercel (Frontend)

### Option A: Via Vercel Website (Easiest)
1. Go to https://vercel.com
2. Sign in with GitHub
3. Click "Add New Project"
4. Select your `CareerVerse` repository
5. **Important Settings:**
   - Framework Preset: **Vite**
   - Root Directory: **Frontend**
   - Build Command: `npm run build`
   - Output Directory: `dist`
6. Click "Deploy"
7. Done! You'll get a URL like `https://careerverse.vercel.app`

### Option B: Via Vercel CLI
```bash
cd Frontend
npm install -g vercel
vercel login
vercel
```

---

## 🔧 Deploy to Render (Backend)

### Via Render Website
1. Go to https://render.com
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Select your `CareerVerse` repository
5. **Important Settings:**
   - Name: `careerverse-backend`
   - Root Directory: **Backend**
   - Environment: **Python 3**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add Environment Variable:
   - Key: `GEMINI_API_KEY`
   - Value: `AIzaSyCF99FqKSVbHuLXUow3AlV9z42aW6Cv9pQ`
7. Click "Create Web Service"
8. **Copy your backend URL** (e.g., `https://careerverse-backend.onrender.com`)

---

## 🔄 After Backend is Deployed

### Update Unity to use production backend:
1. Open `SDGP Teacher Role/Assets/ChatManager.cs`
2. Change line 27:
   ```csharp
   private string apiUrl = "https://YOUR-BACKEND-URL.onrender.com/api/chat"
   ```
3. **Rebuild Unity for WebGL** to `Frontend/public/simulation/`
4. Push updated build:
   ```bash
   git add Frontend/public/simulation/
   git commit -m "Updated Unity with production backend URL"
   git push
   ```
5. Vercel will auto-deploy! ✅

---

## 🔄 Future Updates (Auto-Deploy)

### After making changes:
```bash
# Stage changes
git add .

# Commit with message
git commit -m "Your change description"

# Push to GitHub
git push

# That's it! Vercel & Render auto-deploy 🎉
```

### When you rebuild Unity:
```bash
# Unity rebuilds to Frontend/public/simulation/
git add Frontend/public/simulation/
git commit -m "Updated Unity simulation"
git push
# Vercel auto-deploys the new Unity build ✅
```

---

## 📋 Checklist

- [ ] Git initialized
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Backend deployed to Render
- [ ] Backend URL copied
- [ ] Unity updated with backend URL
- [ ] Unity rebuilt for WebGL
- [ ] Frontend deployed to Vercel
- [ ] Tested live deployment!

---

## 🐛 Troubleshooting

### Git not found
```bash
# Install Git: https://git-scm.com/download/win
```

### Permission denied on push
```bash
# Use GitHub Personal Access Token instead of password
# Create token: https://github.com/settings/tokens
```

### Vercel build fails
- Check if `Frontend/package.json` exists
- Ensure `npm install` works locally first

### Render build fails
- Check if `Backend/requirements.txt` exists
- Ensure all dependencies are listed

---

Good luck! 🚀
