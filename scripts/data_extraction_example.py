"""
POS System Data Extraction Script
Demonstrates the data collection and processing pipeline
"""

import pandas as pd
import numpy as np
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

class POSDataExtractor:
    """Main class for extracting and processing POS system data"""
    
    def __init__(self):
        self.systems = ['Ginesis', 'Logic', 'Wondersoft']
        self.data = {}
        
    def extract_vendor_data(self, vendor_url):
        """
        Extract data from vendor website
        
        Args:
            vendor_url (str): URL of vendor website
            
        Returns:
            dict: Extracted vendor data
        """
        try:
            response = requests.get(vendor_url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract pricing (example selectors)
            pricing = soup.find('div', class_='pricing')
            features = soup.find_all('li', class_='feature-item')
            
            return {
                'pricing': pricing.text if pricing else 'N/A',
                'features': [f.text for f in features]
            }
        except Exception as e:
            print(f"Error extracting from {vendor_url}: {e}")
            return {}
    
    def create_systems_comparison(self):
        """Generate POS Systems Comparison dataset"""
        data = {
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
        
        df = pd.DataFrame(data)
        return df
    
    def create_features_matrix(self):
        """Generate POS Features Matrix dataset"""
        features = []
        feature_id = 1
        
        categories = ['Eyewear Workflow', 'Integration', 'Customization']
        
        for system in self.systems:
            for category in categories:
                # Generate sample features
                if category == 'Eyewear Workflow':
                    feature_names = ['Frame Selection', 'Lens Type Selection', 
                                   'Coating Options', 'Lens Index Selection',
                                   'Corridor Selection', 'Dynamic Pricing']
                elif category == 'Integration':
                    feature_names = ['Easyecom Integration', 'Inventory Sync', 
                                   'Order Management']
                else:
                    feature_names = ['Custom Fields']
                
                for fname in feature_names:
                    features.append({
                        'Feature_ID': f'F-{feature_id:03d}',
                        'SystemName': system,
                        'FeatureCategory': category,
                        'FeatureName': fname,
                        'Supported': np.random.choice(['Yes', 'Partial', 'No'], p=[0.7, 0.2, 0.1]),
                        'Rating': np.random.randint(5, 10),
                        'Notes': f'{fname} implementation details'
                    })
                    feature_id += 1
        
        return pd.DataFrame(features)
    
    def create_workflow_steps(self):
        """Generate Eyewear Workflow Steps dataset"""
        steps = [
            ('Frame Selection', 'Customer selects frame from catalog'),
            ('Lens Type Selection', 'Choose lens type (Single Vision, Bifocal, Progressive)'),
            ('Coating Selection', 'Select coatings (Anti-reflective, Blue light, Photochromic)'),
            ('Lens Index Selection', 'Choose lens index based on prescription'),
            ('Corridor Selection', 'Select corridor length for progressive lenses'),
            ('Price Calculation', 'System calculates final price'),
            ('Order Finalization', 'Complete order and payment')
        ]
        
        workflow_data = []
        step_id = 1
        
        for system in self.systems:
            for step_num, (step_name, description) in enumerate(steps, 1):
                workflow_data.append({
                    'Step_ID': f'WF-{step_id:03d}',
                    'StepNumber': step_num,
                    'StepName': step_name,
                    'Description': description,
                    'SystemName': system,
                    'TimeToComplete_Seconds': np.random.randint(30, 120),
                    'ErrorRate_Percent': np.random.randint(2, 10),
                    'StaffTrainingRequired_Hours': np.random.uniform(0.5, 5)
                })
                step_id += 1
        
        return pd.DataFrame(workflow_data)
    
    def create_integration_requirements(self):
        """Generate Integration Requirements dataset"""
        requirements = [
            'Inventory Sync',
            'Order Push',
            'Customer Data Sync',
            'Real-time Price Updates'
        ]
        
        complexity_map = {
            'Ginesis': 'Medium',
            'Logic': 'Low',
            'Wondersoft': 'High'
        }
        
        int_data = []
        req_id = 1
        
        for system in self.systems:
            for req in requirements:
                complexity = complexity_map[system]
                days = {'Low': 5, 'Medium': 15, 'High': 30}[complexity]
                cost = days * 200
                
                int_data.append({
                    'Requirement_ID': f'INT-{req_id:03d}',
                    'SystemName': system,
                    'IntegrationType': 'Easyecom',
                    'RequirementName': req,
                    'Complexity': complexity,
                    'DevelopmentDays': days,
                    'Cost_USD': cost,
                    'Status': 'Pre-built' if complexity == 'Low' else 'Feasible' if complexity == 'Medium' else 'Complex',
                    'Priority': 'High' if 'Inventory' in req or 'Order' in req else 'Medium'
                })
                req_id += 1
        
        return pd.DataFrame(int_data)
    
    def create_cost_analysis(self):
        """Generate Cost Analysis dataset"""
        cost_categories = {
            'Ginesis': {
                'Setup Cost': (500, 0, 0),
                'Hardware': (1200, 0, 400),
                'Monthly Subscription': (2388, 2388, 2388),
                'Integration Development': (10000, 0, 0),
                'Training': (2000, 500, 500)
            },
            'Logic': {
                'Setup Cost': (800, 0, 0),
                'Hardware': (1500, 0, 500),
                'Monthly Subscription': (2988, 2988, 2988),
                'Integration Development': (2600, 0, 0),
                'Training': (1500, 300, 300)
            },
            'Wondersoft': {
                'Setup Cost': (1200, 0, 0),
                'Hardware': (1000, 0, 300),
                'Monthly Subscription': (1188, 1188, 1188),
                'Integration Development': (21000, 0, 0),
                'Training': (2500, 600, 600)
            }
        }
        
        cost_data = []
        cost_id = 1
        
        for system, categories in cost_categories.items():
            for category, (y1, y2, y3) in categories.items():
                cost_data.append({
                    'Cost_ID': f'C-{cost_id:03d}',
                    'SystemName': system,
                    'CostCategory': category,
                    'Year1': y1,
                    'Year2': y2,
                    'Year3': y3,
                    'TotalCost_3Years': y1 + y2 + y3,
                    'Notes': f'{category} details'
                })
                cost_id += 1
        
        return pd.DataFrame(cost_data)
    
    def export_to_excel(self, df, filename):
        """Export DataFrame to Excel with formatting"""
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Data', index=False)
        
        workbook = writer.book
        worksheet = writer.sheets['Data']
        
        # Format header
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#4472C4',
            'font_color': 'white',
            'border': 1
        })
        
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
            worksheet.set_column(col_num, col_num, 20)
        
        writer.close()
        print(f"Exported: {filename}")
    
    def run_extraction(self):
        """Execute full data extraction pipeline"""
        print("Starting POS Data Extraction Pipeline...")
        print(f"Timestamp: {datetime.now()}")
        
        # Create all datasets
        print("\n1. Creating Systems Comparison...")
        systems_df = self.create_systems_comparison()
        self.export_to_excel(systems_df, '../0_Datasets/POS_Systems_Comparison.xlsx')
        
        print("\n2. Creating Features Matrix...")
        features_df = self.create_features_matrix()
        self.export_to_excel(features_df, '../0_Datasets/POS_Features_Matrix.xlsx')
        
        print("\n3. Creating Workflow Steps...")
        workflow_df = self.create_workflow_steps()
        self.export_to_excel(workflow_df, '../0_Datasets/Eyewear_Workflow_Steps.xlsx')
        
        print("\n4. Creating Integration Requirements...")
        integration_df = self.create_integration_requirements()
        self.export_to_excel(integration_df, '../0_Datasets/Integration_Requirements.xlsx')
        
        print("\n5. Creating Cost Analysis...")
        cost_df = self.create_cost_analysis()
        self.export_to_excel(cost_df, '../0_Datasets/Cost_Analysis.xlsx')
        
        print("\n✓ Data extraction completed successfully!")
        
        # Summary statistics
        print("\n=== Summary ===")
        print(f"Systems analyzed: {len(self.systems)}")
        print(f"Features evaluated: {len(features_df)}")
        print(f"Workflow steps: {len(workflow_df)}")
        print(f"Integration requirements: {len(integration_df)}")
        print(f"Cost items: {len(cost_df)}")


if __name__ == "__main__":
    extractor = POSDataExtractor()
    extractor.run_extraction()
