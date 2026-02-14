# How to Run Streamlit on the Web

## Option 1: Run Locally (Opens in Browser)

### Step 1: Install Streamlit
```bash
pip install streamlit
```

### Step 2: Run the App
```bash
cd ML_PROJECT
streamlit run streamlit_app.py
```

### What Happens:
- Streamlit starts a local server
- **Automatically opens your browser** to `http://localhost:8501`
- The app is accessible on your local network
- Press `Ctrl+C` to stop

### Access from Other Devices:
If you want to access from your phone/tablet on the same WiFi:
```bash
streamlit run streamlit_app.py --server.address 0.0.0.0
```
Then access via: `http://YOUR_COMPUTER_IP:8501`

---

## Option 2: Deploy to Streamlit Cloud (FREE - Recommended)

Streamlit Cloud is **FREE** and perfect for portfolios!

### Step 1: Push Code to GitHub

1. **Create a GitHub repository:**
   ```bash
   cd ML_PROJECT
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/loan-prediction.git
   git push -u origin main
   ```

2. **Important files to include:**
   - `streamlit_app.py`
   - `predict.py`
   - `models/` folder (with all .pkl files)
   - `requirements.txt`

### Step 2: Deploy on Streamlit Cloud

1. Go to: **https://share.streamlit.io/**
2. Sign in with GitHub
3. Click **"New app"**
4. Select your repository
5. Set:
   - **Main file path**: `streamlit_app.py`
   - **Branch**: `main`
6. Click **"Deploy"**

### Step 3: Your App is Live!
- Streamlit Cloud gives you a URL like: `https://your-app-name.streamlit.app`
- **Anyone can access it!**
- Updates automatically when you push to GitHub

---

## Option 3: Deploy to Heroku

### Step 1: Create Files

**Create `Procfile`:**
```
web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
```

**Create `.streamlit/config.toml`:**
```toml
[server]
port = $PORT
address = "0.0.0.0"
```

### Step 2: Deploy
```bash
heroku create your-app-name
git push heroku main
```

---

## Option 4: Deploy to AWS/GCP/Azure

### AWS (EC2 or Elastic Beanstalk)
- Launch EC2 instance
- Install dependencies
- Run: `streamlit run streamlit_app.py --server.port 80`

### Google Cloud Platform
- Use Cloud Run
- Containerize with Docker
- Deploy container

### Azure
- Use Azure App Service
- Deploy via Azure CLI

---

## Quick Start (Local - Easiest)

```bash
# 1. Navigate to project
cd ML_PROJECT

# 2. Install streamlit (if not installed)
pip install streamlit

# 3. Run the app
streamlit run streamlit_app.py
```

**That's it!** Your browser will automatically open to:
- **Local URL**: http://localhost:8501

---

## Troubleshooting

### Port Already in Use?
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Model Not Found Error?
- Make sure you've run the notebook first
- Check that `models/` folder exists with all .pkl files

### Dependencies Missing?
```bash
pip install -r requirements.txt
```

---

## Best Option for You

**For Portfolio/Demo:** Use **Streamlit Cloud** (Option 2)
- ✅ FREE
- ✅ Easy setup
- ✅ Public URL
- ✅ Auto-updates from GitHub
- ✅ Perfect for showing to recruiters

**For Testing:** Use **Local** (Option 1)
- ✅ Fastest
- ✅ No setup needed
- ✅ Good for development
