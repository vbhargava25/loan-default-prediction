#!/bin/bash

# Update GitHub with all changes
# This includes: deleted .md files, updated model, updated requirements.txt

echo "🔄 Updating GitHub repository..."
echo ""

cd "$(dirname "$0")"

# Add all changes (including deletions)
echo "➕ Staging all changes..."
git add -A

# Commit changes
echo "💾 Committing changes..."
git commit -m "Clean up: Remove extra .md files, update model with scikit-learn 1.3.2, fix version compatibility"

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git push

echo ""
echo "✅ Done! All changes pushed to GitHub."
echo "🌐 View at: https://github.com/vbhargava25/loan-default-prediction"
echo ""
echo "Streamlit will auto-redeploy with the updated model!"
