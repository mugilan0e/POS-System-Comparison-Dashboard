@echo off
echo ========================================
echo GitHub Repository Setup Script
echo ========================================
echo.

set /p username="Enter your GitHub username: "
set /p reponame="Enter repository name (default: POS-System-Comparison-Dashboard): "

if "%reponame%"=="" set reponame=POS-System-Comparison-Dashboard

echo.
echo Creating repository URL...
set repourl=https://github.com/%username%/%reponame%.git

echo.
echo Repository URL: %repourl%
echo.
echo Please create the repository on GitHub first:
echo 1. Go to https://github.com/new
echo 2. Repository name: %reponame%
echo 3. Description: Power BI dashboard comparing retail POS systems for eyewear stores
echo 4. Choose Public or Private
echo 5. DO NOT initialize with README
echo 6. Click "Create repository"
echo.
pause

echo.
echo Adding remote origin...
git remote remove origin 2>nul
git remote add origin %repourl%

echo.
echo Renaming branch to main...
git branch -M main

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo Done! Check your repository at:
echo https://github.com/%username%/%reponame%
echo ========================================
pause
