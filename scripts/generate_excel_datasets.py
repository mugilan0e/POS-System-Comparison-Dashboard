"""
Generate Excel Datasets for POS System Comparison Dashboard
Run this script to create all required Excel files
"""

import pandas as pd
import os

# Create output directory if it doesn't exist
output_dir = '../0_Datasets'
os.makedirs(output_dir, exist_ok=True)

print("Generating POS System Comparison Datasets...")
print("=" * 50)

# Dataset 1: POS Systems Comparison
print("\n1. Creating POS_Systems_Comparison.xlsx...")
systems_data = {
    'System_ID': ['POS-001', 'POS-002', 'POS-003'],
    'SystemName': ['Ginesis', 'Logic', 'Wondersoft'],
    'Vendor': ['Ginesis Technologies', 'Logic Retail Solutions', 'Wondersoft Systems'],
    'PricingModel': ['Subscription', 'Subscription', 'One-time + Support'],
    'MonthlyFee': [199, 249, 99],
    'SetupCost': [500, 800, 1200],
    'HardwareCost': [1200, 1500, 1000],
    'OverallScore': [7.5, 8.2, 7.8],
    'EaseOfUse': [8, 9, 7],
    'CustomizationScore': [7, 8, 9],
    'IntegrationScore': [8, 7, 6],
    'SupportRating': [7, 9, 8]
}
df_systems = pd.DataFrame(systems_data)
df_systems.to_excel(f'{output_dir}/POS_Systems_Comparison.xlsx', index=False, sheet_name='Data')
print(f"   ✓ Created with {len(df_systems)} records")

# Dataset 2: POS Features Matrix
print("\n2. Creating POS_Features_Matrix.xlsx...")
features_data = []
feature_id = 1

# Ginesis features
features_data.extend([
    ['F-001', 'Ginesis', 'Eyewear Workflow', 'Frame Selection', 'Yes', 8, 'Basic frame catalog with search'],
    ['F-002', 'Ginesis', 'Eyewear Workflow', 'Lens Type Selection', 'Yes', 7, 'Standard lens types supported'],
    ['F-003', 'Ginesis', 'Eyewear Workflow', 'Coating Options', 'Yes', 8, 'Multiple coating types'],
    ['F-004', 'Ginesis', 'Eyewear Workflow', 'Lens Index Selection', 'Yes', 7, '1.5, 1.6, 1.67, 1.74 supported'],
    ['F-005', 'Ginesis', 'Eyewear Workflow', 'Corridor Selection', 'Yes', 6, 'Limited corridor options'],
    ['F-006', 'Ginesis', 'Eyewear Workflow', 'Dynamic Pricing', 'Yes', 8, 'Price updates based on selections'],
    ['F-007', 'Ginesis', 'Integration', 'Easyecom Integration', 'Partial', 5, 'API available, custom development needed'],
    ['F-008', 'Ginesis', 'Integration', 'Inventory Sync', 'Yes', 7, 'Real-time sync with delays'],
    ['F-009', 'Ginesis', 'Integration', 'Order Management', 'Yes', 8, 'Good order tracking'],
    ['F-010', 'Ginesis', 'Customization', 'Custom Fields', 'Yes', 7, 'Limited custom fields'],
])

# Logic features
features_data.extend([
    ['F-011', 'Logic', 'Eyewear Workflow', 'Frame Selection', 'Yes', 9, 'Advanced catalog with images'],
    ['F-012', 'Logic', 'Eyewear Workflow', 'Lens Type Selection', 'Yes', 9, 'Comprehensive lens library'],
    ['F-013', 'Logic', 'Eyewear Workflow', 'Coating Options', 'Yes', 9, 'Extensive coating options'],
    ['F-014', 'Logic', 'Eyewear Workflow', 'Lens Index Selection', 'Yes', 8, 'All standard indices'],
    ['F-015', 'Logic', 'Eyewear Workflow', 'Corridor Selection', 'Yes', 8, 'Multiple corridor lengths'],
    ['F-016', 'Logic', 'Eyewear Workflow', 'Dynamic Pricing', 'Yes', 9, 'Real-time price calculation'],
    ['F-017', 'Logic', 'Integration', 'Easyecom Integration', 'Yes', 7, 'Pre-built connector available'],
    ['F-018', 'Logic', 'Integration', 'Inventory Sync', 'Yes', 9, 'Real-time bidirectional sync'],
    ['F-019', 'Logic', 'Integration', 'Order Management', 'Yes', 9, 'Advanced order workflow'],
    ['F-020', 'Logic', 'Customization', 'Custom Fields', 'Yes', 8, 'Flexible custom fields'],
])

# Wondersoft features
features_data.extend([
    ['F-021', 'Wondersoft', 'Eyewear Workflow', 'Frame Selection', 'Yes', 8, 'Good catalog management'],
    ['F-022', 'Wondersoft', 'Eyewear Workflow', 'Lens Type Selection', 'Yes', 8, 'Standard lens options'],
    ['F-023', 'Wondersoft', 'Eyewear Workflow', 'Coating Options', 'Yes', 9, 'Highly customizable coatings'],
    ['F-024', 'Wondersoft', 'Eyewear Workflow', 'Lens Index Selection', 'Yes', 8, 'All indices supported'],
    ['F-025', 'Wondersoft', 'Eyewear Workflow', 'Corridor Selection', 'Yes', 9, 'Extensive corridor options'],
    ['F-026', 'Wondersoft', 'Eyewear Workflow', 'Dynamic Pricing', 'Yes', 8, 'Formula-based pricing'],
    ['F-027', 'Wondersoft', 'Integration', 'Easyecom Integration', 'No', 3, 'No direct integration'],
    ['F-028', 'Wondersoft', 'Integration', 'Inventory Sync', 'Partial', 6, 'Manual sync required'],
    ['F-029', 'Wondersoft', 'Integration', 'Order Management', 'Yes', 7, 'Basic order management'],
    ['F-030', 'Wondersoft', 'Customization', 'Custom Fields', 'Yes', 9, 'Highly customizable'],
])

df_features = pd.DataFrame(features_data, columns=[
    'Feature_ID', 'SystemName', 'FeatureCategory', 'FeatureName', 
    'Supported', 'Rating', 'Notes'
])
df_features.to_excel(f'{output_dir}/POS_Features_Matrix.xlsx', index=False, sheet_name='Data')
print(f"   ✓ Created with {len(df_features)} records")

# Dataset 3: Eyewear Workflow Steps
print("\n3. Creating Eyewear_Workflow_Steps.xlsx...")
workflow_data = []
step_id = 1

steps = [
    (1, 'Frame Selection', 'Customer selects frame from catalog'),
    (2, 'Lens Type Selection', 'Choose lens type (Single Vision, Bifocal, Progressive)'),
    (3, 'Coating Selection', 'Select coatings (Anti-reflective, Blue light, Photochromic)'),
    (4, 'Lens Index Selection', 'Choose lens index based on prescription'),
    (5, 'Corridor Selection', 'Select corridor length for progressive lenses'),
    (6, 'Price Calculation', 'System calculates final price'),
    (7, 'Order Finalization', 'Complete order and payment')
]

times = {
    'Ginesis': [120, 45, 60, 30, 40, 5, 90],
    'Logic': [90, 35, 45, 25, 30, 3, 75],
    'Wondersoft': [110, 40, 50, 28, 35, 8, 85]
}

errors = {
    'Ginesis': [5, 3, 4, 8, 10, 2, 3],
    'Logic': [3, 2, 2, 4, 5, 1, 2],
    'Wondersoft': [4, 3, 3, 6, 6, 3, 4]
}

training = {
    'Ginesis': [2, 3, 2, 4, 5, 1, 2],
    'Logic': [1.5, 2, 1.5, 3, 3, 0.5, 1.5],
    'Wondersoft': [2, 2.5, 2, 3.5, 4, 2, 2]
}

for system in ['Ginesis', 'Logic', 'Wondersoft']:
    for idx, (step_num, step_name, description) in enumerate(steps):
        workflow_data.append([
            f'WF-{step_id:03d}',
            step_num,
            step_name,
            description,
            system,
            times[system][idx],
            errors[system][idx],
            training[system][idx]
        ])
        step_id += 1

df_workflow = pd.DataFrame(workflow_data, columns=[
    'Step_ID', 'StepNumber', 'StepName', 'Description', 'SystemName',
    'TimeToComplete_Seconds', 'ErrorRate_Percent', 'StaffTrainingRequired_Hours'
])
df_workflow.to_excel(f'{output_dir}/Eyewear_Workflow_Steps.xlsx', index=False, sheet_name='Data')
print(f"   ✓ Created with {len(df_workflow)} records")

# Dataset 4: Integration Requirements
print("\n4. Creating Integration_Requirements.xlsx...")
integration_data = []
req_id = 1

requirements = [
    'Inventory Sync',
    'Order Push',
    'Customer Data Sync',
    'Real-time Price Updates'
]

complexity_map = {
    'Ginesis': ('Medium', 15, 3000, 'Feasible'),
    'Logic': ('Low', 5, 500, 'Pre-built'),
    'Wondersoft': ('High', 30, 6000, 'Complex')
}

for system in ['Ginesis', 'Logic', 'Wondersoft']:
    complexity, base_days, base_cost, status = complexity_map[system]
    for req in requirements:
        priority = 'High' if 'Inventory' in req or 'Order' in req else 'Medium'
        integration_data.append([
            f'INT-{req_id:03d}',
            system,
            'Easyecom',
            req,
            complexity,
            base_days,
            base_cost,
            status,
            priority
        ])
        req_id += 1

df_integration = pd.DataFrame(integration_data, columns=[
    'Requirement_ID', 'SystemName', 'IntegrationType', 'RequirementName',
    'Complexity', 'DevelopmentDays', 'Cost_USD', 'Status', 'Priority'
])
df_integration.to_excel(f'{output_dir}/Integration_Requirements.xlsx', index=False, sheet_name='Data')
print(f"   ✓ Created with {len(df_integration)} records")

# Dataset 5: Cost Analysis
print("\n5. Creating Cost_Analysis.xlsx...")
cost_data = []
cost_id = 1

cost_categories = {
    'Ginesis': {
        'Setup Cost': (500, 0, 0, 'One-time setup'),
        'Hardware': (1200, 0, 400, 'Initial + replacement'),
        'Monthly Subscription': (2388, 2388, 2388, '$199/month'),
        'Integration Development': (10000, 0, 0, 'Easyecom integration'),
        'Training': (2000, 500, 500, 'Staff training'),
        'Support': (0, 0, 0, 'Included in subscription')
    },
    'Logic': {
        'Setup Cost': (800, 0, 0, 'One-time setup'),
        'Hardware': (1500, 0, 500, 'Initial + replacement'),
        'Monthly Subscription': (2988, 2988, 2988, '$249/month'),
        'Integration Development': (2600, 0, 0, 'Pre-built connector'),
        'Training': (1500, 300, 300, 'Staff training'),
        'Support': (0, 0, 0, 'Included in subscription')
    },
    'Wondersoft': {
        'Setup Cost': (1200, 0, 0, 'One-time setup'),
        'Hardware': (1000, 0, 300, 'Initial + replacement'),
        'Monthly Subscription': (1188, 1188, 1188, '$99/month support'),
        'Integration Development': (21000, 0, 0, 'Complex custom integration'),
        'Training': (2500, 600, 600, 'Staff training'),
        'Support': (0, 0, 0, 'Included in subscription')
    }
}

for system, categories in cost_categories.items():
    for category, (y1, y2, y3, notes) in categories.items():
        cost_data.append([
            f'C-{cost_id:03d}',
            system,
            category,
            y1,
            y2,
            y3,
            y1 + y2 + y3,
            notes
        ])
        cost_id += 1

df_cost = pd.DataFrame(cost_data, columns=[
    'Cost_ID', 'SystemName', 'CostCategory', 'Year1', 'Year2', 'Year3',
    'TotalCost_3Years', 'Notes'
])
df_cost.to_excel(f'{output_dir}/Cost_Analysis.xlsx', index=False, sheet_name='Data')
print(f"   ✓ Created with {len(df_cost)} records")

print("\n" + "=" * 50)
print("✓ All datasets created successfully!")
print("\nGenerated files:")
print("  - POS_Systems_Comparison.xlsx (3 systems)")
print("  - POS_Features_Matrix.xlsx (30 features)")
print("  - Eyewear_Workflow_Steps.xlsx (21 workflow steps)")
print("  - Integration_Requirements.xlsx (12 requirements)")
print("  - Cost_Analysis.xlsx (18 cost items)")
print("\nFiles are ready for Power BI import!")
