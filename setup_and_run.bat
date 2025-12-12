@echo off
echo ========================================
echo POS Dashboard Builder - Setup & Run
echo ========================================
echo.

echo Installing required Python packages...
pip install pandas openpyxl

echo.
echo Running dashboard builder...
cd "POS-System-Comparison-Dashboard"
python build_pos_dashboard.py

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Check the generated files:
echo   - powerbi_import_guide.txt
echo   - pbi_template.json
echo.
echo Next: Open Power BI Desktop and follow the import guide!
echo.
pause