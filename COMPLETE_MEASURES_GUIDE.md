# Complete Guide: Creating All Measures Successfully

## Good News!

I can see you successfully created the "Measure Table"! It's visible in your Tables list on the right side.

Now let's create all the measures properly.

---

## Step-by-Step: Create Each Measure

### Important: Select Measure Table First!

1. In the Tables list (right side), click on **"Measure Table"**
2. Make sure it's highlighted/selected
3. Now you're ready to create measures

---

## Creating Measures - One by One

For EACH measure below:

1. Make sure **"Measure Table"** is selected
2. Go to **Modeling** tab
3. Click **"New measure"**
4. Copy the ENTIRE formula (including the name)
5. Paste it in the formula bar
6. Press **Enter**

---

## Measure 1: OverallScore

**Copy this ENTIRE line:**

```dax
OverallScore = CALCULATE((AVERAGE(POS_Systems_Comparison[EaseOfUse]) * 0.25) + (AVERAGE(POS_Systems_Comparison[CustomizationScore]) * 0.20) + (AVERAGE(POS_Systems_Comparison[IntegrationScore]) * 0.35) + (AVERAGE(POS_Systems_Comparison[SupportRating]) * 0.20))
```

**Test it:**
- Insert a Card visual
- Drag OverallScore to it
- Should show a number between 7-9

---

## Measure 2: TCO_3Years

```dax
TCO_3Years = SUMX(Cost_Analysis, Cost_Analysis[Year1] + Cost_Analysis[Year2] + Cost_Analysis[Year3])
```

**Test it:**
- Card visual should show values like 16,964 or 22,664 or 31,064

---

## Measure 3: AvgWorkflowTime

```dax
AvgWorkflowTime = SUM(Eyewear_Workflow_Steps[TimeToComplete_Seconds]) / 60
```

**Test it:**
- Should show values in minutes (around 6-8 minutes)

---

## Measure 4: WorkflowEfficiency

```dax
WorkflowEfficiency = VAR AvgTime = AVERAGE(Eyewear_Workflow_Steps[TimeToComplete_Seconds]) VAR AvgError = AVERAGE(Eyewear_Workflow_Steps[ErrorRate_Percent]) RETURN DIVIDE(1, (AvgTime * AvgError), 0) * 10000
```

**Note:** This is all ONE line - no line breaks!

---

## Measure 5: IntegrationReadiness

```dax
IntegrationReadiness = VAR AvgComplexity = AVERAGE(Integration_Requirements[Complexity_Numeric]) VAR AvgDays = AVERAGE(Integration_Requirements[DevelopmentDays]) RETURN 10 - ((AvgComplexity * AvgDays) / 10)
```

**Important:** Make sure you created the Complexity_Numeric column first!

**Test it:**
- Should show values between 0-10
- Logic should have highest score (around 9.5)
- Wondersoft should have lowest (around 1)

---

## Measure 6: FeatureCoverage

```dax
FeatureCoverage = DIVIDE(COUNTROWS(FILTER(POS_Features_Matrix, POS_Features_Matrix[Supported] = "Yes")), COUNTROWS(POS_Features_Matrix), 0) * 100
```

**Test it:**
- Should show percentages (around 70-90%)

---

## Measure 7: ErrorRateIndex

```dax
ErrorRateIndex = AVERAGE(Eyewear_Workflow_Steps[ErrorRate_Percent])
```

**Test it:**
- Should show values between 2-10

---

## Measure 8: TotalTrainingHours

```dax
TotalTrainingHours = SUM(Eyewear_Workflow_Steps[StaffTrainingRequired_Hours])
```

**Test it:**
- Should show values around 15-25 hours

---

## Measure 9: CostPerFeature

```dax
CostPerFeature = DIVIDE([TCO_3Years], COUNTROWS(FILTER(POS_Features_Matrix, POS_Features_Matrix[Supported] = "Yes")), 0)
```

**Note:** This uses [TCO_3Years] measure, so create TCO_3Years first!

---

## Measure 10: ROI_Score

```dax
ROI_Score = DIVIDE(([WorkflowEfficiency] * [FeatureCoverage]), ([TCO_3Years] / 10000), 0)
```

**Note:** This uses other measures, so create those first!

---

## Measure 11: TotalIntegrationCost

```dax
TotalIntegrationCost = SUM(Integration_Requirements[Cost_USD])
```

**Test it:**
- Ginesis: $10,000
- Logic: $2,600
- Wondersoft: $21,000

---

## Measure 12: TotalIntegrationDays

```dax
TotalIntegrationDays = SUM(Integration_Requirements[DevelopmentDays])
```

**Test it:**
- Ginesis: 60 days
- Logic: 20 days
- Wondersoft: 120 days

---

## Measure 13: RecommendedSystem (for Page 5)

```dax
RecommendedSystem = VAR MaxROI = MAXX(ALL(POS_Systems_Comparison), [ROI_Score]) RETURN CALCULATE(MAX(POS_Systems_Comparison[SystemName]), FILTER(ALL(POS_Systems_Comparison), [ROI_Score] = MaxROI))
```

**Test it:**
- Should show "Logic" (the system with best ROI)

---

## Verification Checklist

After creating all measures, verify:

### Check 1: All Measures Exist

In your Measure Table, you should see:
- [ ] OverallScore
- [ ] TCO_3Years
- [ ] AvgWorkflowTime
- [ ] WorkflowEfficiency
- [ ] IntegrationReadiness
- [ ] FeatureCoverage
- [ ] ErrorRateIndex
- [ ] TotalTrainingHours
- [ ] CostPerFeature
- [ ] ROI_Score
- [ ] TotalIntegrationCost
- [ ] TotalIntegrationDays
- [ ] RecommendedSystem

All should have a calculator (fx) icon.

### Check 2: Test with Table Visual

1. Insert a Table visual
2. Add these fields:
   - POS_Systems_Comparison[SystemName]
   - OverallScore
   - TCO_3Years
   - FeatureCoverage
   - IntegrationReadiness
3. Should show 3 rows (Ginesis, Logic, Wondersoft)
4. All values should be numbers (not blank)

### Check 3: Expected Values

| System | OverallScore | TCO_3Years | FeatureCoverage |
|--------|--------------|------------|-----------------|
| Ginesis | ~7.5 | ~22,664 | ~70-80% |
| Logic | ~8.2 | ~16,964 | ~80-90% |
| Wondersoft | ~7.8 | ~31,064 | ~70-80% |

If your values are close to these, SUCCESS!

---

## Common Errors & Fixes

### Error: "Column 'Complexity_Numeric' cannot be found"

**Fix:**
1. Go to Data view
2. Click Integration_Requirements table
3. Create the Complexity_Numeric calculated column first
4. Then come back and create the measure

### Error: "Measure shows blank"

**Fix:**
1. Go to Model view
2. Check all relationships exist
3. Verify SystemName connects all tables
4. Refresh the visual

### Error: "Circular dependency detected"

**Fix:**
1. Delete the measure causing the error
2. Make sure you created measures in order
3. Recreate the measure

### Error: "Syntax error"

**Fix:**
1. Make sure formula is ONE line (no line breaks)
2. Check for straight quotes " not curly quotes " "
3. Copy formula exactly from this guide

---

## Pro Tips

### Tip 1: Create in Order
Create measures in the order listed above. Some measures depend on others.

### Tip 2: Test Each One
After creating each measure, test it with a Card visual immediately.

### Tip 3: Save Frequently
Save your Power BI file after every 2-3 measures.

### Tip 4: Use Autocomplete
When typing formulas, use the autocomplete dropdown to select table/column names.

### Tip 5: Format Measures
After creating, right-click measure → Format:
- TCO_3Years: Currency, $ English (United States)
- FeatureCoverage: Percentage, 1 decimal
- OverallScore: Decimal number, 1 decimal

---

## Quick Test: Create a Summary Table

After all measures are created:

1. Insert a **Table** visual
2. Add ALL measures to it
3. Add SystemName
4. You should see a complete comparison table!

This is a great way to verify everything works.

---

## Next Steps

After all measures are created successfully:

1. **Save your file!**
2. Move on to creating visuals (Page 1: Executive Summary)
3. Use the measures in Cards, Charts, and Gauges
4. Build the complete dashboard

---

## Need Help?

If you get stuck:

1. **Check which measure is causing the error**
   - Look at the error message
   - Note which table/column it mentions

2. **Verify prerequisites**
   - Calculated columns created?
   - Relationships set up?
   - Table names correct?

3. **Take a screenshot showing:**
   - The formula bar with your DAX
   - The error message
   - The Measure Table selected

4. **Try the measure in a different table**
   - Instead of Measure Table, try POS_Systems_Comparison
   - Sometimes this helps identify the issue

---

**You're doing great! The Measure Table is created. Now just create each measure one by one, testing as you go!**
