# Step-by-Step: Push to GitHub

## ✅ Your Repository
**URL:** https://github.com/vbhargava25/loan-default-prediction.git

---

## Step 1: Open Terminal

Open Terminal on your Mac (Applications → Utilities → Terminal)

---

## Step 2: Navigate to Your Project

Copy and paste this command:

```bash
cd "/Users/vakavenkatabhargavareddy/Desktop/project/END_to_END Data science project/ML_PROJECT"
```

Press **Enter**

---

## Step 3: Initialize Git

```bash
git init
```

Press **Enter**

You should see: `Initialized empty Git repository in ...`

---

## Step 4: Add All Files

```bash
git add .
```

Press **Enter**

This adds all your files to Git.

---

## Step 5: Create First Commit

```bash
git commit -m "Initial commit: Loan Default Prediction ML Project"
```

Press **Enter**

You should see files being committed.

---

## Step 6: Set Branch to Main

```bash
git branch -M main
```

Press **Enter**

---

## Step 7: Connect to Your GitHub Repository

```bash
git remote add origin https://github.com/vbhargava25/loan-default-prediction.git
```

Press **Enter**

---

## Step 8: Push to GitHub

```bash
git push -u origin main
```

Press **Enter**

**⚠️ Important:** You may be asked to authenticate:
- If asked for username: Enter `vbhargava25`
- If asked for password: Use a **Personal Access Token** (not your GitHub password)

---

## If You Get Authentication Error

### Option A: Use Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Name it: `streamlit-deploy`
4. Check: `repo` (full control)
5. Click **"Generate token"**
6. **Copy the token** (you won't see it again!)
7. When asked for password, paste the token

### Option B: Use GitHub Desktop (Easier)

1. Download: https://desktop.github.com/
2. Sign in
3. File → Add Local Repository
4. Select your `ML_PROJECT` folder
5. Click "Publish repository"
6. Done!

---

## Step 9: Verify It Worked

1. Go to: https://github.com/vbhargava25/loan-default-prediction
2. You should see all your files there!

---

## Step 10: Deploy to Streamlit Cloud

1. Go to: **https://share.streamlit.io/**
2. Click **"Sign in"** (use GitHub)
3. Click **"New app"**
4. Select repository: `vbhargava25/loan-default-prediction`
5. Main file path: `streamlit_app.py`
6. Click **"Deploy"**
7. Wait 2-3 minutes
8. Your app will be live! 🎉

---

## Quick Copy-Paste (All Commands at Once)

```bash
cd "/Users/vakavenkatabhargavareddy/Desktop/project/END_to_END Data science project/ML_PROJECT"
git init
git add .
git commit -m "Initial commit: Loan Default Prediction ML Project"
git branch -M main
git remote add origin https://github.com/vbhargava25/loan-default-prediction.git
git push -u origin main
```

---

## Troubleshooting

### "Repository not found"
- Make sure the repository exists at: https://github.com/vbhargava25/loan-default-prediction
- Check you're signed in to GitHub

### "Authentication failed"
- Use Personal Access Token (see Step 8 above)
- Or use GitHub Desktop

### "Remote origin already exists"
Run this first:
```bash
git remote remove origin
```
Then continue with Step 7.

---

## ✅ Success Checklist

- [ ] All files pushed to GitHub
- [ ] Repository visible at: https://github.com/vbhargava25/loan-default-prediction
- [ ] Streamlit app deployed at: https://share.streamlit.io/

Good luck! 🚀
