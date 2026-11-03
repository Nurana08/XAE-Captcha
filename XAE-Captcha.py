# Do your coding here
# Segment 1
# 1. Create variables, each with a comment naming its data type
APP_NAME = "XAE-Captcha"            # text (string)
YEAR = 2050                         # whole number (integer)
MAX_PIN_ATTEMPTS = 3                # whole number (integer)
MIN_CREDENTIAL = 30                 # whole number (integer)
BORDERLINE_MARGIN = 10.0            # decimal (float)
SHOW_BARS = True                    # True/False (boolean)
# 2. Create LAYERS, a list of tuples: (layer name, weight, short description)
# The weights must add up to 1.0 (0.35 + 0.25 + 0.15 + 0.15 + 0.10 = 1.0)
LAYERS = [
    ("Credential", 0.35, "PIN verification"),
    ("Biometric", 0.25, "Speed and code reaction"),
    ("Behavior", 0.15, "Usual habits & patterns"),
    ("Vouching", 0.15, "Trusted network check"),
    ("In-person anchor", 0.10, "Physical registration data"),
]
# 3. Create REGISTRY, a list of tuples (one per registered person)
# Format: (username, pin, usual time, usual device, usual city, list of vouchers, in-person year, in-person office)
REGISTRY = [
    ("aina", "482913", "morning", "NeuralLink-X", "Neo-Kuala Lumpur", ["zack", "nova"], 2048, "Sector 7"),
    ("alex", "123456", "night", "Quantum-Tab", "Cyber-Penang", ["aina", "neo"], 2049, "Sector 3")
]
# 4. Create three lists that line up by position for risk levels
RISK_LEVELS = ["low", "medium", "high"]                                    # Risk levels
RISK_EXAMPLES = ["Routine check", "Standard verification", "High security alert"] # Examples
RISK_THRESHOLDS = [50, 65, 80]                                             # Threshold scores
#checking
print(len(LAYERS))     #should print 5
print(REGISTRY[0][0])  #should print Aina
# Segment 2

# Segment 3

# Segment 4

# Segment 5

# Segment 6
