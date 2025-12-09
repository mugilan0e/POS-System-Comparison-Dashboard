# POS System Comparison - Data Dictionary

## Overview
This dataset is designed to evaluate three retail POS systems (Ginesis, Logic, Wondersoft) for eyewear retail stores with custom lens selection workflows and Easyecom integration requirements.

## 1. POS_Systems_Comparison.xlsx
Core comparison of the three POS systems.

| Column | Description | Data Type |
|--------|-------------|-----------|
| **System_ID** | Unique identifier for the POS system. | String |
| **SystemName** | Name of the POS system (Ginesis, Logic, Wondersoft). | String |
| **Vendor** | Vendor/company name. | String |
| **PricingModel** | Pricing structure (Subscription, One-time, etc.). | String |
| **MonthlyFee** | Monthly subscription cost. | Currency |
| **SetupCost** | One-time setup/implementation cost. | Currency |
| **HardwareCost** | Cost of required hardware. | Currency |
| **OverallScore** | Composite score (1-10 scale). | Decimal |
| **EaseOfUse** | User experience rating (1-10). | Integer |
| **CustomizationScore** | Customization capability (1-10). | Integer |
| **IntegrationScore** | Integration capability (1-10). | Integer |
| **SupportRating** | Vendor support quality (1-10). | Integer |

## 2. POS_Features_Matrix.xlsx
Detailed feature comparison across systems.

| Column | Description | Data Type |
|--------|-------------|-----------|
| **Feature_ID** | Unique identifier for the feature. | String |
| **SystemName** | POS system name. | String |
| **FeatureCategory** | Category (Eyewear Workflow, Integration, Customization). | String |
| **FeatureName** | Specific feature name. | String |
| **Supported** | Whether feature is supported (Yes/No/Partial). | String |
| **Rating** | Feature quality rating (1-10). | Integer |
| **Notes** | Additional details about the feature. | String |

## 3. Eyewear_Workflow_Steps.xlsx
Step-by-step workflow analysis for eyewear customization process.

| Column | Description | Data Type |
|--------|-------------|-----------|
| **Step_ID** | Unique identifier for the workflow step. | String |
| **StepNumber** | Sequential step number (1-7). | Integer |
| **StepName** | Name of the workflow step. | String |
| **Description** | Detailed description of the step. | String |
| **SystemName** | POS system name. | String |
| **TimeToComplete_Seconds** | Average time to complete step. | Integer |
| **ErrorRate_Percent** | Error rate percentage for this step. | Decimal |
| **StaffTrainingRequired_Hours** | Training hours needed for staff. | Decimal |

## 4. Integration_Requirements.xlsx
Easyecom integration analysis.

| Column | Description | Data Type |
|--------|-------------|-----------|
| **Requirement_ID** | Unique identifier for integration requirement. | String |
| **SystemName** | POS system name. | String |
| **IntegrationType** | Integration platform (Easyecom). | String |
| **RequirementName** | Specific integration requirement. | String |
| **Complexity** | Development complexity (Low/Medium/High). | String |
| **DevelopmentDays** | Estimated development time in days. | Integer |
| **Cost_USD** | Development cost in USD. | Currency |
| **Status** | Implementation status (Pre-built/Feasible/Complex). | String |
| **Priority** | Business priority (High/Medium/Low). | String |

## 5. Cost_Analysis.xlsx
3-year total cost of ownership analysis.

| Column | Description | Data Type |
|--------|-------------|-----------|
| **Cost_ID** | Unique identifier for cost item. | String |
| **SystemName** | POS system name. | String |
| **CostCategory** | Type of cost (Setup, Hardware, Subscription, etc.). | String |
| **Year1** | Cost in first year. | Currency |
| **Year2** | Cost in second year. | Currency |
| **Year3** | Cost in third year. | Currency |
| **TotalCost_3Years** | Total cost over 3 years. | Currency |
| **Notes** | Additional cost details. | String |

## Eyewear Workflow Steps
The typical retail flow for eyewear orders:
1. **Frame Selection** - Customer chooses frame from catalog
2. **Lens Type Selection** - Single vision, bifocal, or progressive
3. **Coating Selection** - Anti-reflective, blue light filter, photochromic, etc.
4. **Lens Index Selection** - 1.5, 1.6, 1.67, 1.74 based on prescription
5. **Corridor Selection** - For progressive lenses (short, medium, long)
6. **Price Calculation** - System calculates final price based on all selections
7. **Order Finalization** - Complete order and process payment
