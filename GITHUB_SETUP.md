# How to Push Your Code to GitHub

## Step-by-Step Guide

### Step 1: Create GitHub Repository

1. Go to **https://github.com**
2. Sign in (or create account)
3. Click **"+"** → **"New repository"**
4. Name it: `loan-default-prediction` (or any name)
5. Make it **Public** (for free Streamlit Cloud)
6. **Don't** initialize with README
7. Click **"Create repository"**

### Step 2: Initialize Git in Your Project

Open terminal in your `ML_PROJECT` folder:

```bash
cd "/Users/vakavenkatabhargavareddy/Desktop/project/END_to_END Data science project/ML_PROJECT"

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Loan Default Prediction ML Project"

# Rename branch to main
git branch -M main

# Add GitHub repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/loan-default-prediction.git

# Push to GitHub
git push -u origin main
```

### Step 3: What Files to Include

**✅ Include these:**
- `streamlit_app.py`
- `predict.py`
- `app.py`
- `requirements.txt`
- `README.md`
- `models/` folder (with all .pkl files)
- `mlproject.ipynb` (optional, but good to include)

**❌ Don't include:**
- `__pycache__/` folders
- `.pyc` files
- Large data files (if any)
- Personal API keys

### Step 4: Create .gitignore (Optional but Recommended)

Create `.gitignore` file:

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
.DS_Store
*.log
.env
venv/
env/
```

---

## Alternative: Using GitHub Desktop (Easier)

If you prefer a GUI:

1. Download **GitHub Desktop**: https://desktop.github.com/
2. Sign in with GitHub
3. Click **"File"** → **"Add Local Repository"**
4. Select your `ML_PROJECT` folder
5. Click **"Publish repository"**
6. Choose name and make it **Public**
7. Click **"Publish"**

---

## After Pushing to GitHub

Once your code is on GitHub:

1. Go to **https://share.streamlit.io/**
2. Sign in with GitHub
3. Click **"New app"**
4. Select your repository: `loan-default-prediction`
5. Main file: `streamlit_app.py`
6. Click **"Deploy"**

**That's it!** Your app will be live in 2-3 minutes.

---

## Quick Command Summary

```bash
# Navigate to project
cd ML_PROJECT

# Initialize and push
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/loan-default-prediction.git
git push -u origin main
```

**Note:** Replace `YOUR_USERNAME` with your actual GitHub username!
