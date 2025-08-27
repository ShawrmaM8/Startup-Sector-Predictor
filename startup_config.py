import os

# Paths
BASE_DIR = r"C:\Users\muzam\OneDrive\Desktop\PROJECTS\Education\Micro Projects\3) Startup Industry Categorizer"
DATA_PATH = os.path.join(BASE_DIR, "DaTA", "business_ideas.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "startup_classifier.pkl")

# Sectors for classification
# Expanded sectors for classification
SECTORS = [
    "EdTech",
    "FinTech",
    "HealthTech",
    "ECommerce",
    "AgriTech",
    "CleanTech",
    "PropTech",      
    "LegalTech",
    "GovTech",        
    "Media & Entertainment",
    "Gaming",
    "Cybersecurity",
    "AI & Data Science",
    "Robotics",
    "Manufacturing & Industry 4.0",
    "Energy & Utilities",
    "Transportation & Mobility",
    "Food & Beverage",
    "Retail",
    "Travel & Hospitality",
    "Logistics & Supply Chain",
    "Biotech & Pharma",
    "Consumer Electronics",
    "Social Impact / Non-Profit",
    "Other"
]
