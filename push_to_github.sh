#!/bin/bash

# Script to push ML_PROJECT to GitHub
# Repository: https://github.com/vbhargava25/loan-default-prediction.git

echo "🚀 Pushing code to GitHub..."
echo "Repository: https://github.com/vbhargava25/loan-default-prediction.git"
echo ""

# Navigate to ML_PROJECT directory
cd "$(dirname "$0")"

# Initialize git (if not already initialized)
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
fi

# Add all files
echo "➕ Adding files..."
git add .

# Create commit
echo "💾 Creating commit..."
git commit -m "Initial commit: Loan Default Prediction ML Project with FastAPI and Streamlit"

# Set branch to main
echo "🌿 Setting branch to main..."
git branch -M main

# Add remote (if not already added)
echo "🔗 Adding remote repository..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/vbhargava25/loan-default-prediction.git

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Done! Your code is now on GitHub!"
echo "🌐 View it at: https://github.com/vbhargava25/loan-default-prediction"
echo ""
echo "Next step: Deploy to Streamlit Cloud at https://share.streamlit.io/"
