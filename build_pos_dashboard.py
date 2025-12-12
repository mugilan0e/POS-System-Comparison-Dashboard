"""
POS System Comparison Dashboard - Automated Builder
Creates a complete Power BI dashboard from Excel data
"""

import pandas as pd
import os
import json
from pathlib import Path
from datetime import datetime

# Define the path to your datasets
DATA_PATH = r"C:\Users\Lenovo\Self_projects\PowerBi Dashboard\POS-System-Comparison-Dashboard\0_Datasets"

print("=" * 60)
print("POS SYSTEM COMPARISON DASHBOARD - AUTOMATED BUILDER")
print("=" * 60)

# Check if path exists
if not os.path.exists(DATA_PATH):
    print(f"❌ ERROR: Path not found: {DATA_PATH}")
    print("Please verify the path and try again.")
    exit(1)

print(f"\n✓ Found datasets folder: {DATA_PATH}\n")

# List available files
excel_files = [f for f in os.listdir(DATA_PATH) if f.endswith('.xlsx')]
print(f"Found {len(excel_files)} Excel files:")
for file in excel_files:
    filepath = os.path.join(DATA_PATH, file)
    size = os.path.getsize(filepath) / 1024  # Size in KB
    print(f"  ✓ {file} ({size:.1f} KB)")

print("\n" + "=" * 60)
print("VALIDATING DATA FILES:")
print("=" * 60)

# Read and validate each file
tables_info = {}
required_files = [
    'Cost_Analysis.xlsx',
    'POS_Systems_Comparison.xlsx', 
    'POS_Features_Matrix.xlsx',
    'Eyewear_Workflow_Steps.xlsx',
    'Integration_Requirements.xlsx'
]

all_files_valid = True

for file in required_files:
    filepath = os.path.join(DATA_PATH, file)
    if os.path.exists(filepath):
        try:
            df = pd.read_excel(filepath, sheet_name=0)
            tables_info[file] = {
                'rows': len(df),
                'columns': len(df.columns),
                'fields': list(df.columns),
                'data': df
            }
            print(f"\n✓ {file}")
            print(f"  Rows: {len(df)}")
            print(f"  Columns: {len(df.columns)}")
            print(f"  Key Fields: {', '.join(df.columns[:4])}...")
            
            # Validate key fields
            if 'SystemName' in df.columns:
                systems = df['SystemName'].unique()
                print(f"  Systems: {', '.join(systems)}")
            
        except Exception as e:
            print(f"\n❌ {file}: Error - {e}")
            all_files_valid = False
    else:
        print(f"\n⚠ {file}: Not found")
        all_files_valid = False

if not all_files_valid:
    print("\n❌ Some required files are missing or invalid.")
    print("Please ensure all 5 Excel files are present and valid.")
    exit(1)

print("\n" + "=" * 60)
print("GENERATING POWER BI TEMPLATE:")
print("=" * 60)

# Create Power BI template structure
pbi_template = {
    "version": "1.0",
    "name": "POS System Comparison Dashboard",
    "description": "Automated dashboard comparing Ginesis, Logic, and Wondersoft POS systems",
    "created": datetime.now().isoformat(),
    "tables": {},
    "relationships": [],
    "measures": {},
    "pages": []
}

# Add table definitions
for file, info in tables_info.items():
    table_name = file.replace('.xlsx', '').replace('_', '')
    pbi_template["tables"][table_name] = {
        "source": file,
        "rows": info['rows'],
        "columns": info['fields']
    }

# Define relationships
relationships = [
    {
        "from": "POSSystemsComparison[SystemName]",
        "to": "POSFeaturesMatrix[SystemName]",
        "cardinality": "OneToMany"
    },
    {
        "from": "POSSystemsComparison[SystemName]", 
        "to": "EyewearWorkflowSteps[SystemName]",
        "cardinality": "OneToMany"
    },
    {
        "from": "POSSystemsComparison[SystemName]",
        "to": "IntegrationRequirements[SystemName]", 
        "cardinality": "OneToMany"
    },
    {
        "from": "POSSystemsComparison[SystemName]",
        "to": "CostAnalysis[SystemName]",
        "cardinality": "OneToMany"
    }
]

pbi_template["relationships"] = relationships

# Define DAX measures
measures = {
    "OverallScore": """
    OverallScore = 
    VAR EaseOfUse = AVERAGE(POS_Systems_Comparison[EaseOfUse])
    VAR Customization = AVERAGE(POS_Systems_Comparison[CustomizationScore])
    VAR Integration = AVERAGE(POS_Systems_Comparison[IntegrationScore])
    VAR Support = AVERAGE(POS_Systems_Comparison[SupportRating])
    RETURN
        (EaseOfUse * 0.25) +
        (Customization * 0.20) +
        (Integration * 0.35) +
        (Support * 0.20)
    """,
    
    "TCO_3Years": """
    TCO_3Years = 
    SUMX(
        Cost_Analysis,
        Cost_Analysis[Year1] + Cost_Analysis[Year2] + Cost_Analysis[Year3]
    )
    """,
    
    "FeatureCoverage": """
    FeatureCoverage = 
    DIVIDE(
        COUNTROWS(
            FILTER(
                POS_Features_Matrix,
                POS_Features_Matrix[Supported] = "Yes"
            )
        ),
        COUNTROWS(POS_Features_Matrix),
        0
    ) * 100
    """,
    
    "IntegrationReadiness": """
    IntegrationReadiness = 
    VAR AvgComplexity = AVERAGE(Integration_Requirements[Complexity_Numeric])
    VAR AvgDays = AVERAGE(Integration_Requirements[DevelopmentDays])
    RETURN
        10 - ((AvgComplexity * AvgDays) / 10)
    """,
    
    "WorkflowEfficiency": """
    WorkflowEfficiency = 
    VAR AvgTime = AVERAGE(Eyewear_Workflow_Steps[TimeToComplete_Seconds])
    VAR AvgError = AVERAGE(Eyewear_Workflow_Steps[ErrorRate_Percent])
    RETURN
        DIVIDE(1, (AvgTime * AvgError), 0) * 10000
    """,
    
    "TotalIntegrationCost": """
    TotalIntegrationCost = SUM(Integration_Requirements[Cost_USD])
    """,
    
    "TotalTrainingHours": """
    TotalTrainingHours = SUM(Eyewear_Workflow_Steps[StaffTrainingRequired_Hours])
    """,
    
    "ErrorRateIndex": """
    ErrorRateIndex = AVERAGE(Eyewear_Workflow_Steps[ErrorRate_Percent])
    """
}

pbi_template["measures"] = measures

# Define dashboard pages
pages = [
    {
        "name": "Executive Summary",
        "visuals": [
            {
                "type": "Card",
                "title": "Ginesis Overall Score",
                "measure": "OverallScore",
                "filter": "SystemName = 'Ginesis'",
                "conditional_formatting": {
                    ">=8": "Green",
                    ">=6": "Yellow", 
                    "<6": "Red"
                }
            },
            {
                "type": "Card",
                "title": "Logic Overall Score", 
                "measure": "OverallScore",
                "filter": "SystemName = 'Logic'",
                "conditional_formatting": {
                    ">=8": "Green",
                    ">=6": "Yellow",
                    "<6": "Red"
                }
            },
            {
                "type": "Card",
                "title": "Wondersoft Overall Score",
                "measure": "OverallScore", 
                "filter": "SystemName = 'Wondersoft'",
                "conditional_formatting": {
                    ">=8": "Green",
                    ">=6": "Yellow",
                    "<6": "Red"
                }
            },
            {
                "type": "ColumnChart",
                "title": "3-Year Total Cost of Ownership",
                "x_axis": "SystemName",
                "y_axis": "TCO_3Years",
                "format": "Currency"
            },
            {
                "type": "StackedBar",
                "title": "Feature Coverage",
                "axis": "SystemName", 
                "values": "FeatureCoverage",
                "legend": "Supported"
            }
        ]
    }
]

pbi_template["pages"] = pages

# Save template
template_file = os.path.join(os.path.dirname(DATA_PATH), "pbi_template.json")
with open(template_file, 'w') as f:
    json.dump(pbi_template, f, indent=2)

print(f"✓ Power BI template created: {template_file}")

print("\n" + "=" * 60)
print("CREATING POWER BI IMPORT SCRIPT:")
print("=" * 60)

# Create Power BI import script
import_script = f'''
# Power BI Desktop Import Script
# Copy and paste these commands into Power BI Desktop

# 1. IMPORT DATA TABLES
Get Data -> Excel Workbook -> Navigate to:
{DATA_PATH}

Import these files in order:
1. POS_Systems_Comparison.xlsx
2. POS_Features_Matrix.xlsx  
3. Eyewear_Workflow_Steps.xlsx
4. Integration_Requirements.xlsx
5. Cost_Analysis.xlsx

# 2. CREATE RELATIONSHIPS (Model View)
POS_Systems_Comparison[SystemName] -> POS_Features_Matrix[SystemName] (1:*)
POS_Systems_Comparison[SystemName] -> Eyewear_Workflow_Steps[SystemName] (1:*)
POS_Systems_Comparison[SystemName] -> Integration_Requirements[SystemName] (1:*)
POS_Systems_Comparison[SystemName] -> Cost_Analysis[SystemName] (1:*)

# 3. CREATE CALCULATED COLUMNS
# In Integration_Requirements table:
Complexity_Numeric = SWITCH(Integration_Requirements[Complexity], "Low", 1, "Medium", 2, "High", 3, 0)

# In POS_Features_Matrix table:
Supported_Numeric = SWITCH(POS_Features_Matrix[Supported], "Yes", 1, "Partial", 0.5, "No", 0, 0)

# 4. CREATE MEASURES (Copy each DAX formula)
'''

for measure_name, dax_formula in measures.items():
    import_script += f"\n# {measure_name}\n{dax_formula.strip()}\n"

import_script += '''

# 5. CREATE VISUALS (Page 1: Executive Summary)

VISUAL 1-3: System Scorecards
- Insert → Card (3 times)
- Add OverallScore measure
- Filter each to one system (Ginesis, Logic, Wondersoft)
- Apply conditional formatting (Green ≥8, Yellow ≥6, Red <6)

VISUAL 4: TCO Comparison
- Insert -> Clustered Column Chart
- X-axis: SystemName
- Y-axis: TCO_3Years
- Format as currency

VISUAL 5: Feature Coverage
- Insert -> 100% Stacked Bar Chart
- Axis: SystemName
- Values: Count of Supported
- Legend: Supported field

# 6. APPLY THEME
Colors:
- Ginesis: #0078D4 (Blue)
- Logic: #107C10 (Green)  
- Wondersoft: #FF8C00 (Orange)
'''

script_file = os.path.join(os.path.dirname(DATA_PATH), "powerbi_import_guide.txt")
with open(script_file, 'w', encoding='utf-8') as f:
    f.write(import_script)

print(f"✓ Import script created: {script_file}")

print("\n" + "=" * 60)
print("EXPECTED DASHBOARD VALUES:")
print("=" * 60)

# Calculate expected values from actual data
if 'POS_Systems_Comparison.xlsx' in tables_info:
    systems_df = tables_info['POS_Systems_Comparison.xlsx']['data']
    
    print("\nSystem Scorecards (OverallScore):")
    for _, row in systems_df.iterrows():
        if all(col in row for col in ['EaseOfUse', 'CustomizationScore', 'IntegrationScore', 'SupportRating']):
            overall = (row['EaseOfUse'] * 0.25 + 
                      row['CustomizationScore'] * 0.20 + 
                      row['IntegrationScore'] * 0.35 + 
                      row['SupportRating'] * 0.20)
            color = "Green" if overall >= 8 else "Yellow" if overall >= 6 else "Red"
            print(f"  {row['SystemName']}: {overall:.1f} ({color})")

if 'Cost_Analysis.xlsx' in tables_info:
    cost_df = tables_info['Cost_Analysis.xlsx']['data']
    
    print("\n3-Year TCO by System:")
    for system in ['Ginesis', 'Logic', 'Wondersoft']:
        system_costs = cost_df[cost_df['SystemName'] == system]
        if not system_costs.empty and all(col in system_costs.columns for col in ['Year1', 'Year2', 'Year3']):
            total_tco = (system_costs['Year1'].sum() + 
                        system_costs['Year2'].sum() + 
                        system_costs['Year3'].sum())
            print(f"  {system}: ${total_tco:,.0f}")

if 'POS_Features_Matrix.xlsx' in tables_info:
    features_df = tables_info['POS_Features_Matrix.xlsx']['data']
    
    print("\nFeature Coverage by System:")
    for system in ['Ginesis', 'Logic', 'Wondersoft']:
        system_features = features_df[features_df['SystemName'] == system]
        if not system_features.empty and 'Supported' in system_features.columns:
            yes_count = len(system_features[system_features['Supported'] == 'Yes'])
            total_count = len(system_features)
            coverage = (yes_count / total_count) * 100 if total_count > 0 else 0
            print(f"  {system}: {coverage:.0f}% ({yes_count}/{total_count} features)")

print("\n" + "=" * 60)
print("NEXT STEPS:")
print("=" * 60)

print("""
OPTION 1: Power BI Desktop (Recommended - 15 minutes)
  1. Download Power BI Desktop: https://powerbi.microsoft.com/desktop/
  2. Open the import guide: powerbi_import_guide.txt
  3. Follow step-by-step instructions
  4. Your dashboard will be ready in 15 minutes!

OPTION 2: Power BI Online (Manual - 30 minutes)  
  1. Continue with your current Power BI Online
  2. Manually add remaining tables via "Enter data"
  3. Create measures using DAX formulas above
  4. Build visuals through web interface

OPTION 3: Request Corporate Access (Fastest if available)
  1. Ask IT for Power BI Pro license or OneDrive upgrade
  2. Upload Excel files directly to Power BI Online
  3. Build dashboard in web interface
""")

print("\n" + "=" * 60)
print("✓ DASHBOARD BUILD PACKAGE READY!")
print("=" * 60)

print(f"""
Generated Files:
  ✓ Power BI Template: {template_file}
  ✓ Import Guide: {script_file}
  ✓ All Excel Data: {DATA_PATH}

Your data is validated and ready. Choose your preferred method above!

Questions? All DAX formulas and step-by-step instructions are in:
  → powerbi_import_guide.txt
""")

print(f"\nScript completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")