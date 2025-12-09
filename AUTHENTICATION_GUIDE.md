# GitHub Authentication Guide

## The Issue
Git is trying to use cached credentials for "thecloudsstudio" instead of your account (mugilan0e).

## Solution: Use Personal Access Token

### Step 1: Create a Personal Access Token

1. Go to: https://github.com/settings/tokens/new
2. Fill in:
   - **Note**: `POS Dashboard Push`
   - **Expiration**: 30 days (or your preference)
   - **Select scopes**: Check `repo` (Full control of private repositories)
3. Click "Generate token"
4. **COPY THE TOKEN** - you won't see it again!

### Step 2: Push Using Token

Open Command Prompt or PowerShell and run:

```bash
cd "C:\Users\Lenovo\Self_projects\PowerBi Dashboard\POS-System-Comparison-Dashboard"

git remote remove origin

git remote add origin https://YOUR_TOKEN@github.com/mugilan0e/POS-System-Comparison-Dashboard.git

git push -u origin main
```

Replace `YOUR_TOKEN` with the token you copied.

### Alternative: Use GitHub Desktop

1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your mugilan0e account
3. File → Add Local Repository
4. Select: `C:\Users\Lenovo\Self_projects\PowerBi Dashboard\POS-System-Comparison-Dashboard`
5. Click "Publish repository"

### Alternative: Manual Upload

1. Go to: https://github.com/mugilan0e/POS-System-Comparison-Dashboard
2. Click "uploading an existing file"
3. Drag and drop all folders/files from `POS-System-Comparison-Dashboard`
4. Commit changes

## What Will Be Pushed

✓ 0_Datasets/ (5 Excel files)
✓ 3_Documentation/ (5 markdown files)
✓ scripts/ (1 Python file)
✓ README.md
✓ requirements.txt
✓ .gitignore
✓ PROJECT_SUMMARY.md
✓ GITHUB_SETUP.md

Total: 16 files

## Quick Command (with token)

```bash
cd "C:\Users\Lenovo\Self_projects\PowerBi Dashboard\POS-System-Comparison-Dashboard"
git remote set-url origin https://YOUR_TOKEN@github.com/mugilan0e/POS-System-Comparison-Dashboard.git
git push -u origin main
```

## Verify Success

After pushing, visit:
https://github.com/mugilan0e/POS-System-Comparison-Dashboard

You should see all files!
