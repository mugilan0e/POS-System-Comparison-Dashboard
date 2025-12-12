# Datasets for POS System Comparison Dashboard

This folder contains 5 Excel datasets ready for Power BI import.

## Files

### 1. POS_Systems_Comparison.xlsx
**Records:** 3 systems  
**Columns:** 12  
**Description:** Core comparison data for Ginesis, Logic, and Wondersoft POS systems

**Fields:**
- System_ID, SystemName, Vendor, PricingModel
- MonthlyFee, SetupCost, HardwareCost
- OverallScore, EaseOfUse, CustomizationScore, IntegrationScore, SupportRating

### 2. POS_Features_Matrix.xlsx
**Records:** 30 features  
**Columns:** 7  
**Description:** Detailed feature support matrix across all systems

**Fields:**
- Feature_ID, SystemName, FeatureCategory, FeatureName
- Supported (Yes/Partial/No), Rating (1-10), Notes

**Categories:**
- Eyewear Workflow (6 features per system)
- Integration (3 features per system)
- Customization (1 feature per system)

### 3. Eyewear_Workflow_Steps.xlsx
**Records:** 21 workflow steps  
**Columns:** 8  
**Description:** 7-step eyewear customization workflow analysis for each system

**Fields:**
- Step_ID, StepNumber, StepName, Description, SystemName
- TimeToComplete_Seconds, ErrorRate_Percent, StaffTrainingRequired_Hours

**Workflow Steps:**
1. Frame Selection
2. Lens Type Selection
3. Coating Selection
4. Lens Index Selection
5. Corridor Selection
6. Price Calculation
7. Order Finalization

### 4. Integration_Requirements.xlsx
**Records:** 12 requirements  
**Columns:** 9  
**Description:** Easyecom integration analysis for each system

**Fields:**
- Requirement_ID, SystemName, IntegrationType, RequirementName
- Complexity (Low/Medium/High), DevelopmentDays, Cost_USD, Status, Priority

**Requirements:**
- Inventory Sync
- Order Push
- Customer Data Sync
- Real-time Price Updates

### 5. Cost_Analysis.xlsx
**Records:** 18 cost items  
**Columns:** 8  
**Description:** 3-year total cost of ownership breakdown

**Fields:**
- Cost_ID, SystemName, CostCategory
- Year1, Year2, Year3, TotalCost_3Years, Notes

**Cost Categories:**
- Setup Cost
- Hardware
- Monthly Subscription
- Integration Development
- Training
- Support

## Data Relationships

All datasets connect through the **SystemName** field:
- POS_Systems_Comparison (1) → POS_Features_Matrix (Many)
- POS_Systems_Comparison (1) → Eyewear_Workflow_Steps (Many)
- POS_Systems_Comparison (1) → Integration_Requirements (Many)
- POS_Systems_Comparison (1) → Cost_Analysis (Many)

## Regenerating Datasets

If you need to regenerate the Excel files:

```bash
cd ../scripts
python generate_excel_datasets.py
```

This will recreate all 5 Excel files with the same data structure.

## Data Quality

All datasets have been validated for:
- Correct data types
- No missing values in key fields
- Consistent naming across tables
- Proper Excel formatting

## Import to Power BI

1. Open Power BI Desktop
2. Get Data → Excel Workbook
3. Navigate to this folder
4. Select each .xlsx file
5. Load all tables
6. Create relationships in Model view

See **POWERBI_IMPLEMENTATION_GUIDE.md** for detailed instructions.

---

**Total Records:** 84 across all datasets  
**Last Generated:** December 9, 2025  
**Format:** Excel (.xlsx) with single 'Data' sheet per file
