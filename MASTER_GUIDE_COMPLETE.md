# Power BI Dashboard - Complete Master Guide
## POS System Comparison Dashboard

**Everything you need in one document: Understanding + Implementation + Troubleshooting**

---

# TABLE OF CONTENTS

1. [Understanding the Dashboard - WHY & HOW](#part-1-understanding-the-dashboard)
2. [Data Setup - Import & Relationships](#part-2-data-setup)
3. [Calculated Columns - Step by Step](#part-3-calculated-columns)
4. [Measures - All Formulas with Explanations](#part-4-measures)
5. [Building Visuals - Page by Page](#part-5-building-visuals)
6. [Troubleshooting Common Errors](#part-6-troubleshooting)
7. [Quick Reference - All Formulas](#part-7-quick-reference)

---

# PART 1: UNDERSTANDING THE DASHBOARD

## The Big Picture

We're building a **decision-making dashboard** to compare 3 POS systems (Ginesis, Logic, Wondersoft) for eyewear retail stores.

**Goal:** Transform 84 rows of raw data into a clear recommendation: "Which system should we buy?"

---

## Why 5 Different Excel Files?

Each file represents a different aspect of the comparison:

### 1. POS_Systems_Comparison.xlsx (3 rows)
**What:** Master list of the 3 systems  
**Why:** Contains basic info and scores  
**Example:** Ginesis: $199/month, EaseOfUse=8, Integration=8

### 2. POS_Features_Matrix.xlsx (30 rows)
**What:** Feature checklist (10 features × 3 systems)  
**Why:** Shows which features each system supports  
**Example:** Ginesis supports "Frame Selection": Yes, Rating 8

### 3. Eyewear_Workflow_Steps.xlsx (21 rows)
**What:** Performance data (7 steps × 3 systems)  
**Why:** Measures speed and accuracy  
**Example:** Ginesis: Frame Selection takes 120 seconds, 5% error rate

### 4. Integration_Requirements.xlsx (12 rows)
**What:** Easyecom integration analysis (4 requirements × 3 systems)  
**Why:** Integration is critical for business  
**Example:** Ginesis: Medium complexity, 15 days, $3,000

### 5. Cost_Analysis.xlsx (18 rows)
**What:** Complete cost breakdown (6 categories × 3 systems)  
**Why:** Need total investment, not just monthly fee  
**Example:** Ginesis Year 1: $16,088 (includes $10K integration)

---

## Data Structure Visual

```
┌─────────────────────────────────────────────────────────┐
│         POS_Systems_Comparison (Master Table)           │
│         Ginesis | Logic | Wondersoft                    │
└────────────────────┬────────────────────────────────────┘
                     │ (Connected by SystemName)
        ┌────────────┼────────────┬────────────┐
        │            │            │            │
        ▼            ▼            ▼            ▼
   Features      Workflow    Integration    Costs
   (30 rows)     (21 rows)   (12 rows)     (18 rows)
```

---

## Calculated Columns vs Measures

### Calculated Columns
- **What:** Convert text to numbers
- **Example:** "Low" → 1, "Medium" → 2, "High" → 3
- **When:** Created once when data loads
- **Where:** Stored in table (takes space)
- **We create:** 2 columns

### Measures
- **What:** Dynamic calculations
- **Example:** TCO changes based on selected system
- **When:** Calculated on-the-fly
- **Where:** Not stored (calculated dynamically)
- **We create:** 13 measures

---

## The 13 Measures Explained

### Cost Analysis (How much?)
1. **TCO_3Years** - Total cost over 3 years
2. **CostPerFeature** - Cost divided by features (value for money)
3. **TotalIntegrationCost** - Just integration costs
4. **TotalIntegrationDays** - Time to integrate

### Performance (How good?)
5. **AvgWorkflowTime** - Time to complete an order
6. **WorkflowEfficiency** - Speed + accuracy combined
7. **ErrorRateIndex** - How often mistakes happen
8. **TotalTrainingHours** - Time to train staff

### Features (What can it do?)
9. **FeatureCoverage** - % of features supported
10. **IntegrationReadiness** - How easy to integrate (0-10)

### Overall Scores (What's best?)
11. **OverallScore** - Weighted average of 4 ratings
12. **ROI_Score** - Benefits divided by cost
13. **RecommendedSystem** - Automatic recommendation

---

# PART 2: DATA SETUP

## Step 1: Import Data

### Import All 5 Excel Files

1. Open Power BI Desktop
2. Click **"Get Data"** → **"Excel Workbook"**
3. Navigate to `/0_Datasets/` folder
4. Select **POS_Systems_Comparison.xlsx**
5. Check the data sheet
6. Click **"Load"**

**Repeat for:**
- POS_Features_Matrix.xlsx
- Eyewear_Workflow_Steps.xlsx
- Integration_Requirements.xlsx
- Cost_Analysis.xlsx

### Verify Import

1. Click **"Data"** view (left sidebar)
2. Check all 5 tables appear in Fields pane
3. Verify data looks correct

---

## Step 2: Create Relationships

### Switch to Model View

1. Click **"Model"** view icon (left sidebar)
2. You'll see all 5 tables

### Create 4 Relationships

All relationships connect through **SystemName** field.

#### Relationship 1: Systems → Features
1. Drag **SystemName** from POS_Systems_Comparison
2. Drop onto **SystemName** in POS_Features_Matrix
3. Settings:
   - Cardinality: **One to Many (1:*)**
   - Cross filter: **Single**
4. Click **OK**

#### Relationship 2: Systems → Workflow
- From: POS_Systems_Comparison[SystemName]
- To: Eyewear_Workflow_Steps[SystemName]
- Cardinality: One to Many (1:*)

#### Relationship 3: Systems → Integration
- From: POS_Systems_Comparison[SystemName]
- To: Integration_Requirements[SystemName]
- Cardinality: One to Many (1:*)

#### Relationship 4: Systems → Cost
- From: POS_Systems_Comparison[SystemName]
- To: Cost_Analysis[SystemName]
- Cardinality: One to Many (1:*)

### Verify Relationships

- All relationships show as solid lines
- All are 1:* (One to Many)
- No circular dependencies

---

# PART 3: CALCULATED COLUMNS

## Column 1: Complexity_Numeric

### Purpose
Convert "Low/Medium/High" to numbers (1/2/3) for calculations.

### Steps

1. Click on **Data** view
2. Select **Integration_Requirements** table (in Fields pane)
3. Go to **"Table tools"** or **"Column tools"** tab
4. Click **"New column"**
5. Paste this formula (ONE LINE):

```dax
Complexity_Numeric = SWITCH(Integration_Requirements[Complexity], "Low", 1, "Medium", 2, "High", 3, 0)
```

6. Press **Enter**

### Verify
- New column appears in Integration_Requirements table
- Values should be: 1, 2, or 3
- Logic = 1, Ginesis = 2, Wondersoft = 3

### Why This Works
```
SWITCH(column, value1, result1, value2, result2, default)
"Low" → 1
"Medium" → 2
"High" → 3
Anything else → 0
```

---

## Column 2: Supported_Numeric

### Purpose
Convert "Yes/Partial/No" to numbers (1/0.5/0) for calculations.

### Steps

1. Select **POS_Features_Matrix** table
2. Click **"New column"**
3. Paste this formula (ONE LINE):

```dax
Supported_Numeric = SWITCH(POS_Features_Matrix[Supported], "Yes", 1, "Partial", 0.5, "No", 0, 0)
```

4. Press **Enter**

### Verify
- New column appears in POS_Features_Matrix table
- Values: 1 (Yes), 0.5 (Partial), 0 (No)

---

# PART 4: MEASURES

## Creating the Measures Table

### Why a Measures Table?
- Organizes all measures in one place
- Keeps Fields pane clean
- Best practice in Power BI

### Steps

1. Click on blank space (deselect all tables)
2. Go to **"Modeling"** tab
3. Click **"New table"**
4. Type exactly: `Measures = {1}`
5. Press **Enter**

### Verify
- "Measures" table appears in Fields pane
- Has one column "Value" with number 1
- This is correct!

---

## Creating Each Measure

**For EACH measure below:**
1. Select **Measures** table
2. Click **"New measure"** (Modeling tab)
3. Copy the ENTIRE formula
4. Paste in formula bar
5. Press **Enter**
6. Test with a Card visual

---

## Measure 1: OverallScore

### What It Does
Combines 4 ratings into one weighted score.

### Formula
```dax
OverallScore = CALCULATE((AVERAGE(POS_Systems_Comparison[EaseOfUse]) * 0.25) + (AVERAGE(POS_Systems_Comparison[CustomizationScore]) * 0.20) + (AVERAGE(POS_Systems_Comparison[IntegrationScore]) * 0.35) + (AVERAGE(POS_Systems_Comparison[SupportRating]) * 0.20))
```

### How It Works
```
(EaseOfUse × 25%) +           // User experience
(Customization × 20%) +        // Flexibility
(Integration × 35%) +          // Most important!
(Support × 20%)                // Service quality
```

### Why These Weights?
- Integration 35%: Critical for Easyecom connection
- Ease of Use 25%: Staff use daily
- Support 20%: Need help when issues arise
- Customization 20%: Nice to have

### Expected Results
- Ginesis: ~7.5
- Logic: ~8.2 (highest)
- Wondersoft: ~7.8

---

## Measure 2: TCO_3Years

### What It Does
Calculates total cost of ownership over 3 years.

### Formula
```dax
TCO_3Years = SUMX(Cost_Analysis, Cost_Analysis[Year1] + Cost_Analysis[Year2] + Cost_Analysis[Year3])
```

### How It Works
- SUMX: Iterates through each row
- Adds Year1 + Year2 + Year3 for each cost item
- Sums everything up

### Why 3 Years?
- Year 1: Expensive (setup, integration, training)
- Years 2-3: Cheaper (just subscription)
- Shows true cost, not just sticker price

### Expected Results
- Ginesis: $22,664
- Logic: $16,964 (lowest!)
- Wondersoft: $31,064 (highest!)

### Key Insight
Wondersoft has lowest monthly fee ($99) but highest total cost due to $21K integration!

---

## Measure 3: AvgWorkflowTime

### What It Does
Calculates total time to complete an eyewear order (in minutes).

### Formula
```dax
AvgWorkflowTime = SUM(Eyewear_Workflow_Steps[TimeToComplete_Seconds]) / 60
```

### How It Works
- SUM: Adds up all 7 workflow steps
- / 60: Converts seconds to minutes

### Why This Matters
- Faster = more customers served per day
- Faster = better customer experience
- Time is money in retail

### Expected Results
- Ginesis: ~6.5 minutes
- Logic: ~5.05 minutes (fastest!)
- Wondersoft: ~5.93 minutes

---

## Measure 4: WorkflowEfficiency

### What It Does
Combines speed AND accuracy into one score.

### Formula
```dax
WorkflowEfficiency = VAR AvgTime = AVERAGE(Eyewear_Workflow_Steps[TimeToComplete_Seconds]) VAR AvgError = AVERAGE(Eyewear_Workflow_Steps[ErrorRate_Percent]) RETURN DIVIDE(1, (AvgTime * AvgError), 0) * 10000
```

### How It Works
```
1. Calculate average time
2. Calculate average error rate
3. Efficiency = 1 / (time × error) × 10000
```

### Why This Formula?
- Fast but error-prone = bad
- Slow but accurate = bad
- Fast AND accurate = good
- × 10000: Makes number readable

### Expected Results
- Logic: Highest (fastest + most accurate)
- Ginesis: Medium
- Wondersoft: Medium

---

## Measure 5: IntegrationReadiness

### What It Does
Scores how easy it is to integrate with Easyecom (0-10 scale).

### Formula
```dax
IntegrationReadiness = VAR AvgComplexity = AVERAGE(Integration_Requirements[Complexity_Numeric]) VAR AvgDays = AVERAGE(Integration_Requirements[DevelopmentDays]) RETURN 10 - ((AvgComplexity * AvgDays) / 10)
```

### How It Works
```
1. Get average complexity (1-3)
2. Get average days
3. Score = 10 - (complexity × days / 10)
```

### Example Calculation
- Logic: 10 - ((1 × 5) / 10) = 9.5 (excellent!)
- Ginesis: 10 - ((2 × 15) / 10) = 7.0 (good)
- Wondersoft: 10 - ((3 × 30) / 10) = 1.0 (poor)

### Expected Results
- Logic: ~9.5 (pre-built integration!)
- Ginesis: ~7.0
- Wondersoft: ~1.0 (complex custom work)

---

## Measure 6: FeatureCoverage

### What It Does
Calculates what % of required features are supported.

### Formula
```dax
FeatureCoverage = DIVIDE(COUNTROWS(FILTER(POS_Features_Matrix, POS_Features_Matrix[Supported] = "Yes")), COUNTROWS(POS_Features_Matrix), 0) * 100
```

### How It Works
```
1. Count features with "Yes"
2. Count total features
3. Divide and multiply by 100 for percentage
```

### Why This Matters
- 100% = does everything you need
- 50% = only does half
- Higher is better

### Expected Results
- Logic: ~100%
- Ginesis: ~90%
- Wondersoft: ~80%

---

## Measure 7: ErrorRateIndex

### What It Does
Average error rate across all workflow steps.

### Formula
```dax
ErrorRateIndex = AVERAGE(Eyewear_Workflow_Steps[ErrorRate_Percent])
```

### Why This Matters
- Errors = wrong orders = unhappy customers
- Lower is better
- Industry standard: under 5% is good

### Expected Results
- Logic: ~2.7% (excellent!)
- Ginesis: ~5.0% (acceptable)
- Wondersoft: ~4.1% (good)

---

## Measure 8: TotalTrainingHours

### What It Does
Sums up training time needed for staff.

### Formula
```dax
TotalTrainingHours = SUM(Eyewear_Workflow_Steps[StaffTrainingRequired_Hours])
```

### Why This Matters
- Training time = staff not serving customers
- Training time = cost
- Less training = faster deployment

### Expected Results
- Logic: ~11.5 hours (easiest!)
- Ginesis: ~19 hours
- Wondersoft: ~18 hours

---

## Measure 9: CostPerFeature

### What It Does
Calculates value for money.

### Formula
```dax
CostPerFeature = DIVIDE([TCO_3Years], COUNTROWS(FILTER(POS_Features_Matrix, POS_Features_Matrix[Supported] = "Yes")), 0)
```

### How It Works
```
Cost Per Feature = Total Cost / Number of Features
```

### Why This Matters
- Shows if you're getting good value
- Lower = better value
- Helps compare systems with different pricing

### Expected Results
- Logic: ~$1,696 per feature (best value!)
- Ginesis: ~$2,518 per feature
- Wondersoft: ~$3,883 per feature

---

## Measure 10: ROI_Score

### What It Does
Combines efficiency and features vs cost - the ultimate "which to buy" metric.

### Formula
```dax
ROI_Score = DIVIDE(([WorkflowEfficiency] * [FeatureCoverage]), ([TCO_3Years] / 10000), 0)
```

### How It Works
```
ROI = (Benefits) / (Cost)
Benefits = Efficiency × Features
Cost = TCO / 10000 (normalized)
```

### Why This Is Important
- Considers both performance AND cost
- Higher = better return on investment
- The ultimate decision metric

### Expected Results
- Logic: Highest (best ROI)
- Ginesis: Medium
- Wondersoft: Lowest

---

## Measure 11: TotalIntegrationCost

### What It Does
Sums up all integration costs.

### Formula
```dax
TotalIntegrationCost = SUM(Integration_Requirements[Cost_USD])
```

### Expected Results
- Ginesis: $10,000
- Logic: $2,600 (cheapest!)
- Wondersoft: $21,000 (most expensive!)

---

## Measure 12: TotalIntegrationDays

### What It Does
Sums up integration time.

### Formula
```dax
TotalIntegrationDays = SUM(Integration_Requirements[DevelopmentDays])
```

### Expected Results
- Ginesis: 60 days
- Logic: 20 days (fastest!)
- Wondersoft: 120 days (slowest)

---

## Measure 13: RecommendedSystem

### What It Does
Automatically picks the best system based on ROI.

### Formula
```dax
RecommendedSystem = VAR MaxROI = MAXX(ALL(POS_Systems_Comparison), [ROI_Score]) RETURN CALCULATE(MAX(POS_Systems_Comparison[SystemName]), FILTER(ALL(POS_Systems_Comparison), [ROI_Score] = MaxROI))
```

### How It Works
```
1. Find the maximum ROI score
2. Return the system name with that score
```

### Expected Result
- Should show: "Logic"

---

# PART 5: BUILDING VISUALS

## Page 1: Executive Summary

### Visual 1: System Scorecards (3 Cards)

**Create:**
1. Insert → Card
2. Add: OverallScore
3. Filter: SystemName = "Ginesis"
4. Format:
   - Title: "Ginesis Overall Score"
   - Font size: 48pt, Bold
   - Background: Light gray
   - Conditional formatting:
     - >= 8: Green
     - >= 6: Yellow
     - < 6: Red

**Repeat for Logic and Wondersoft**

---

### Visual 2: TCO Comparison (Column Chart)

**Create:**
1. Insert → Clustered Column Chart
2. X-axis: SystemName
3. Y-axis: TCO_3Years
4. Format:
   - Title: "3-Year Total Cost of Ownership"
   - Data labels: ON, Currency format
   - Colors: Ginesis (Blue), Logic (Green), Wondersoft (Orange)

---

### Visual 3: Feature Coverage (Stacked Bar)

**Create:**
1. Insert → 100% Stacked Bar Chart
2. Axis: SystemName
3. Values: Count of Supported
4. Legend: Supported field
5. Format:
   - Title: "Feature Support Coverage"
   - Data labels: Percentage
   - Colors: Yes (Green), Partial (Yellow), No (Red)

---

### Visual 4: Integration Readiness (3 Gauges)

**Create:**
1. Insert → Gauge
2. Value: IntegrationReadiness
3. Filter: SystemName = "Ginesis"
4. Format:
   - Maximum: 10
   - Target: 7
   - Colors: 0-4 (Red), 4-7 (Yellow), 7-10 (Green)

**Repeat for Logic and Wondersoft**

---

## Page 2: Workflow Analysis

### Visual 1: Workflow Time by Step

**Create:**
1. Insert → Clustered Column Chart
2. X-axis: StepName
3. Y-axis: TimeToComplete_Seconds
4. Legend: SystemName
5. Format:
   - Title: "Time to Complete Each Step"
   - Data labels: ON

---

### Visual 2: Error Rate by Step

**Create:**
1. Insert → Line Chart
2. X-axis: StepNumber
3. Y-axis: ErrorRate_Percent
4. Legend: SystemName
5. Format:
   - Title: "Error Rate by Step"
   - Markers: ON

---

## Page 3: Feature Deep Dive

### Visual 1: Feature Matrix Heatmap

**Create:**
1. Insert → Matrix
2. Rows: FeatureName
3. Columns: SystemName
4. Values: Rating
5. Format:
   - Conditional formatting: Gradient Red (1) to Green (10)
   - Grid: ON

---

## Page 4: Integration & Cost

### Visual 1: Integration Complexity

**Create:**
1. Insert → Clustered Column Chart
2. X-axis: RequirementName
3. Y-axis: DevelopmentDays
4. Legend: SystemName

---

### Visual 2: Cost Breakdown

**Create:**
1. Insert → Stacked Bar Chart
2. Axis: SystemName
3. Values: Cost_USD
4. Legend: RequirementName

---

## Page 5: Recommendation

### Visual 1: Final Recommendation Card

**Create:**
1. Insert → Card
2. Add: RecommendedSystem
3. Format:
   - Font: 72pt, Bold
   - Title: "Recommended System"
   - Center aligned

---

### Visual 2: ROI Comparison (3 Gauges)

**Create:**
1. Insert → Gauge
2. Value: ROI_Score
3. Filter by SystemName
4. Format with color thresholds

---

## Global Formatting

### Apply Theme
1. View → Themes
2. Choose professional theme

### System Colors
- Ginesis: #0078D4 (Blue)
- Logic: #107C10 (Green)
- Wondersoft: #FF8C00 (Orange)

### Add Slicers
1. Insert → Slicer
2. Field: SystemName
3. Style: Tile
4. Sync across all pages

---

# PART 6: TROUBLESHOOTING

## Error: "The syntax for '...' is incorrect"

### Cause
You're in the wrong table or column name doesn't exist.

### Solution
1. Check you're in the correct table
2. Verify column names match exactly (case-sensitive)
3. Make sure previous calculated columns exist first

---

## Error: "Column '...' cannot be found"

### Cause
Table or column name is misspelled.

### Solution
1. Check spelling exactly matches your data
2. Use autocomplete (start typing and select from dropdown)
3. Verify table was imported correctly

---

## Error: "Unable to resolve name 'Measures'"

### Cause
Measures table doesn't exist yet.

### Solution
1. Create Measures table first: `Measures = {1}`
2. Or create measures in any existing table (like POS_Systems_Comparison)

---

## Error: "The name of the object 'Table' cannot be renamed"

### Cause
You had a table selected when clicking "New table".

### Solution
1. Close the rename dialog
2. Click on blank space (deselect everything)
3. Then click "New table"
4. Type: `Measures = {1}`

---

## Error: Measure shows blank

### Cause
Relationships not set up correctly.

### Solution
1. Go to Model view
2. Check all relationships exist
3. Verify cardinality is 1:* (One to Many)
4. Ensure cross-filter direction is "Single"

---

## Error: "Circular dependency detected"

### Cause
Measures referencing each other incorrectly.

### Solution
1. Create measures in the order listed
2. Don't create calculated columns that reference measures

---

# PART 7: QUICK REFERENCE

## All Calculated Columns

### Complexity_Numeric (Integration_Requirements table)
```dax
Complexity_Numeric = SWITCH(Integration_Requirements[Complexity], "Low", 1, "Medium", 2, "High", 3, 0)
```

### Supported_Numeric (POS_Features_Matrix table)
```dax
Supported_Numeric = SWITCH(POS_Features_Matrix[Supported], "Yes", 1, "Partial", 0.5, "No", 0, 0)
```

---

## All Measures (Copy-Paste Ready)

### 1. OverallScore
```dax
OverallScore = CALCULATE((AVERAGE(POS_Systems_Comparison[EaseOfUse]) * 0.25) + (AVERAGE(POS_Systems_Comparison[CustomizationScore]) * 0.20) + (AVERAGE(POS_Systems_Comparison[IntegrationScore]) * 0.35) + (AVERAGE(POS_Systems_Comparison[SupportRating]) * 0.20))
```

### 2. TCO_3Years
```dax
TCO_3Years = SUMX(Cost_Analysis, Cost_Analysis[Year1] + Cost_Analysis[Year2] + Cost_Analysis[Year3])
```

### 3. AvgWorkflowTime
```dax
AvgWorkflowTime = SUM(Eyewear_Workflow_Steps[TimeToComplete_Seconds]) / 60
```

### 4. WorkflowEfficiency
```dax
WorkflowEfficiency = VAR AvgTime = AVERAGE(Eyewear_Workflow_Steps[TimeToComplete_Seconds]) VAR AvgError = AVERAGE(Eyewear_Workflow_Steps[ErrorRate_Percent]) RETURN DIVIDE(1, (AvgTime * AvgError), 0) * 10000
```

### 5. IntegrationReadiness
```dax
IntegrationReadiness = VAR AvgComplexity = AVERAGE(Integration_Requirements[Complexity_Numeric]) VAR AvgDays = AVERAGE(Integration_Requirements[DevelopmentDays]) RETURN 10 - ((AvgComplexity * AvgDays) / 10)
```

### 6. FeatureCoverage
```dax
FeatureCoverage = DIVIDE(COUNTROWS(FILTER(POS_Features_Matrix, POS_Features_Matrix[Supported] = "Yes")), COUNTROWS(POS_Features_Matrix), 0) * 100
```

### 7. ErrorRateIndex
```dax
ErrorRateIndex = AVERAGE(Eyewear_Workflow_Steps[ErrorRate_Percent])
```

### 8. TotalTrainingHours
```dax
TotalTrainingHours = SUM(Eyewear_Workflow_Steps[StaffTrainingRequired_Hours])
```

### 9. CostPerFeature
```dax
CostPerFeature = DIVIDE([TCO_3Years], COUNTROWS(FILTER(POS_Features_Matrix, POS_Features_Matrix[Supported] = "Yes")), 0)
```

### 10. ROI_Score
```dax
ROI_Score = DIVIDE(([WorkflowEfficiency] * [FeatureCoverage]), ([TCO_3Years] / 10000), 0)
```

### 11. TotalIntegrationCost
```dax
TotalIntegrationCost = SUM(Integration_Requirements[Cost_USD])
```

### 12. TotalIntegrationDays
```dax
TotalIntegrationDays = SUM(Integration_Requirements[DevelopmentDays])
```

### 13. RecommendedSystem
```dax
RecommendedSystem = VAR MaxROI = MAXX(ALL(POS_Systems_Comparison), [ROI_Score]) RETURN CALCULATE(MAX(POS_Systems_Comparison[SystemName]), FILTER(ALL(POS_Systems_Comparison), [ROI_Score] = MaxROI))
```

---

## Verification Checklist

### After Data Import
- [ ] All 5 Excel files imported
- [ ] All tables visible in Fields pane
- [ ] Data looks correct in Data view

### After Relationships
- [ ] 4 relationships created
- [ ] All are 1:* (One to Many)
- [ ] All connect through SystemName
- [ ] No circular dependencies

### After Calculated Columns
- [ ] Complexity_Numeric created in Integration_Requirements
- [ ] Supported_Numeric created in POS_Features_Matrix
- [ ] Both show correct values (numbers, not text)

### After Measures
- [ ] Measures table created
- [ ] All 13 measures created
- [ ] All have fx icon
- [ ] Test with Card visuals - all show values (not blank)

### After Visuals
- [ ] All 5 pages created
- [ ] Visuals on each page
- [ ] Slicers work
- [ ] Cross-filtering works
- [ ] Navigation buttons work

---

## Expected Results Summary

| System | OverallScore | TCO_3Years | IntegrationReadiness | ROI_Score | Recommended? |
|--------|--------------|------------|---------------------|-----------|--------------|
| Ginesis | 7.5 | $22,664 | 7.0 | Medium | No |
| Logic | 8.2 | $16,964 | 9.5 | Highest | YES ✓ |
| Wondersoft | 7.8 | $31,064 | 1.0 | Lowest | No |

**Conclusion:** Logic is recommended due to:
- Lowest TCO ($16,964)
- Best integration (pre-built, 5 days, $2,600)
- Highest overall score (8.2)
- Best ROI

---

## Tips for Success

1. **Work in order** - Follow this guide sequentially
2. **Save frequently** - Every 15-20 minutes
3. **Test as you build** - Don't wait until the end
4. **Use copy/paste** - For formulas (don't type manually)
5. **Check table selection** - Always verify correct table is selected
6. **One line formulas** - No line breaks in DAX
7. **Take breaks** - Fresh eyes catch errors

---

## Estimated Time

- Data Import: 15 minutes
- Relationships: 10 minutes
- Calculated Columns: 10 minutes
- Measures: 30 minutes
- Visuals: 3-4 hours
- **Total: 5-6 hours**

---

**You now have everything in one place! Good luck building your dashboard!**
