# Detailed Visual Creation Steps
## System Scorecards with Conditional Formatting

**Complete step-by-step instructions with screenshots references**

---

# Creating System Scorecards (3 Cards)

## Overview
We'll create 3 card visuals, one for each POS system, showing their OverallScore with color-coded conditional formatting.

---

# CARD 1: GINESIS SCORECARD

## Step 1: Insert Card Visual

1. **Go to Report view** (click Report icon on left sidebar)
2. **Click on blank canvas** (make sure nothing is selected)
3. **Go to Insert tab** (top ribbon)
4. **Click "Card"** (in the Visualizations section)
5. **You should see:** Empty card visual appears on canvas

---

## Step 2: Add Data to Card

1. **In Fields pane** (right side), expand **"Measures"** table
2. **Find "OverallScore"** measure (has fx icon)
3. **Drag "OverallScore"** to the card visual
   - OR click the checkbox next to OverallScore
4. **You should see:** Card now shows a number (around 7-8)

---

## Step 3: Filter to Ginesis Only

### Method 1: Using Filters Pane

1. **Click on the card** to select it
2. **Look at Filters pane** (right side, below Fields)
3. **Click "Add data field"** under "Filters on this visual"
4. **Expand POS_Systems_Comparison** table
5. **Drag "SystemName"** to the filter area
6. **You should see:** SystemName filter appears
7. **Click the dropdown** next to SystemName
8. **Uncheck "Select all"**
9. **Check only "Ginesis"**
10. **Click "Apply filter"**
11. **You should see:** Card now shows only Ginesis score

### Method 2: Using Visual Level Filter (Alternative)

1. **Click on the card** to select it
2. **In Visualizations pane** (right side), look for **"Filters"** section
3. **Drag SystemName** from Fields to "Filters on this visual"
4. **Follow steps 7-11 above**

---

## Step 4: Format the Card

### Basic Formatting

1. **Click on the card** to select it
2. **In Visualizations pane** (right side), click **"Format visual"** icon (paint roller)
3. **You should see:** Format options appear

### Set Title

1. **Expand "General"** section
2. **Find "Title"** option
3. **Toggle "Title" to ON** (if not already)
4. **Click in "Title text" field**
5. **Type:** "Ginesis Overall Score"
6. **You should see:** Title appears above the card

### Format Title

1. **Still in Title section**
2. **Set Font:** Segoe UI (or your preference)
3. **Set Size:** 14
4. **Set Color:** Black
5. **Toggle Bold:** ON

### Format Data Label (The Big Number)

1. **Expand "Data label"** section
2. **Set Font:** Segoe UI
3. **Set Size:** 48
4. **Toggle Bold:** ON
5. **Set Color:** We'll set this with conditional formatting (next step)

### Set Background

1. **Expand "Effects"** section
2. **Find "Background"** option
3. **Toggle Background:** ON
4. **Set Color:** Light gray (#F3F2F1)

---

## Step 5: Add Conditional Formatting

### Access Conditional Formatting

1. **Make sure card is selected**
2. **In Format visual pane**, expand **"Data label"** section
3. **Look for "Font color"** option
4. **Click the "fx" button** next to Font color
5. **You should see:** Conditional formatting dialog opens

### Set Up Rules

1. **In the dialog, set:**
   - **Format style:** Rules
   - **What field should we base this on:** OverallScore
   - **Summarization:** Don't summarize (should be default)

### Create Rule 1: Green for >= 8

1. **Click "New rule"**
2. **Set the rule:**
   - **If value:** is greater than or equal to
   - **Value:** 8
   - **Color:** Green (#107C10)
3. **Click "OK"**

### Create Rule 2: Yellow for >= 6

1. **Click "New rule"**
2. **Set the rule:**
   - **If value:** is greater than or equal to
   - **Value:** 6
   - **Color:** Yellow (#FFB900)
3. **Click "OK"**

### Create Rule 3: Red for < 6

1. **Click "New rule"**
2. **Set the rule:**
   - **If value:** is less than
   - **Value:** 6
   - **Color:** Red (#D13438)
3. **Click "OK"**

### Apply Formatting

1. **Click "OK"** to close the conditional formatting dialog
2. **You should see:** The number in your card is now colored based on its value
   - Ginesis (7.5) should be **Yellow**

---

## Step 6: Final Card Formatting

### Add Border

1. **In Format visual pane**, expand **"Effects"** section
2. **Find "Border"** option
3. **Toggle Border:** ON
4. **Set Color:** Light gray (#EDEBE9)
5. **Set Width:** 1

### Adjust Size and Position

1. **Click and drag** the card to position it
2. **Drag corners** to resize
3. **Recommended size:** About 200px wide × 150px tall

---

# CARD 2: LOGIC SCORECARD

## Quick Steps (Same Process)

1. **Insert new Card visual**
2. **Add OverallScore measure**
3. **Filter to SystemName = "Logic"**
4. **Set title:** "Logic Overall Score"
5. **Apply same formatting:**
   - Font size: 48pt, Bold
   - Background: Light gray
   - Same conditional formatting rules
6. **You should see:** Logic score (8.2) in **Green** color

---

# CARD 3: WONDERSOFT SCORECARD

## Quick Steps (Same Process)

1. **Insert new Card visual**
2. **Add OverallScore measure**
3. **Filter to SystemName = "Wondersoft"**
4. **Set title:** "Wondersoft Overall Score"
5. **Apply same formatting:**
   - Font size: 48pt, Bold
   - Background: Light gray
   - Same conditional formatting rules
6. **You should see:** Wondersoft score (7.8) in **Yellow** color

---

# ALTERNATIVE: Copy and Modify Method

## Faster Approach

### Create First Card (Ginesis)
Follow all steps above for the Ginesis card.

### Copy for Logic
1. **Right-click on Ginesis card**
2. **Select "Copy"**
3. **Right-click on blank canvas**
4. **Select "Paste"**
5. **Click on the new card**
6. **Change filter:** SystemName = "Logic"
7. **Change title:** "Logic Overall Score"

### Copy for Wondersoft
1. **Right-click on Logic card**
2. **Select "Copy"**
3. **Right-click on blank canvas**
4. **Select "Paste"**
5. **Click on the new card**
6. **Change filter:** SystemName = "Wondersoft"
7. **Change title:** "Wondersoft Overall Score"

---

# TROUBLESHOOTING

## Card Shows Wrong Number

**Problem:** Card shows total of all systems instead of one system  
**Solution:** Check the filter - make sure only one system is selected

## Conditional Formatting Not Working

**Problem:** Number doesn't change color  
**Solution:** 
1. Check that you're formatting "Font color" not "Background color"
2. Verify the rules are set correctly (>= 8, >= 6, < 6)
3. Make sure "What field should we base this on" is set to OverallScore

## Card Shows Blank

**Problem:** No number appears  
**Solution:**
1. Check that OverallScore measure exists and works
2. Verify relationships are set up correctly
3. Try removing and re-adding the measure

## Colors Are Wrong

**Expected Colors:**
- **Ginesis (7.5):** Yellow (between 6 and 8)
- **Logic (8.2):** Green (>= 8)
- **Wondersoft (7.8):** Yellow (between 6 and 8)

**If colors are wrong:**
1. Check the conditional formatting rules
2. Verify the threshold values (8, 6)
3. Make sure you're using the right colors

---

# FINAL LAYOUT

## Arrange Cards

1. **Position cards side by side**
2. **Align them horizontally**
3. **Leave some space between them**
4. **Recommended layout:**
   ```
   [Ginesis]  [Logic]  [Wondersoft]
   ```

## Add Page Title

1. **Insert Text Box** (Insert tab → Text box)
2. **Type:** "Executive Summary"
3. **Format:** 24pt, Bold, Center aligned
4. **Position:** Top of page

---

# VERIFICATION CHECKLIST

After completing all 3 cards:

- [ ] **Ginesis card** shows ~7.5 in **Yellow**
- [ ] **Logic card** shows ~8.2 in **Green**
- [ ] **Wondersoft card** shows ~7.8 in **Yellow**
- [ ] All cards have proper titles
- [ ] All cards have light gray background
- [ ] All cards have 48pt bold numbers
- [ ] Cards are aligned and spaced nicely

---

# NEXT STEPS

After completing the scorecards:

1. **Save your work** (Ctrl+S)
2. **Test the conditional formatting** by changing the rules
3. **Move on to next visual:** TCO Comparison Chart
4. **Add slicers** if you want interactive filtering

---

**You now have professional-looking scorecards with dynamic color coding!**

The conditional formatting will automatically update if the underlying data changes, making your dashboard truly dynamic.