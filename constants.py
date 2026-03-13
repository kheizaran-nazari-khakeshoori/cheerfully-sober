"""Constants for BAC Calculator Application"""

# Widmark factor constants
R_MAN = 0.68
R_WOMAN = 0.55

# Alcohol properties
ETHANOL_DENSITY_G_ML = 0.789  # g/mL

# Metabolism constants
ELIMINATION_RATE_PER_HR = 0.015  # % per hour

# BAC level thresholds and descriptions
BAC_LEVELS = [
    (0.02, "Minimal effects.", "#27ae60"),  # Green
    (0.05, "Mild relaxation; avoid driving.", "#f39c12"),  # Yellow-orange
    (0.08, "Noticeable impairment; do not drive.", "#e67e22"),  # Orange
    (0.15, "Marked impairment; stay safe and hydrated.", "#d35400"),  # Dark orange
    (0.30, "Severe impairment; danger present.", "#c0392b"),  # Red
    (float('inf'), "Potentially life-threatening BAC! Seek help immediately.", "#8b0000")  # Dark red
]

# GUI Configuration
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 600
WINDOW_TITLE = "cheerfully-sober"

# Colors
HEADER_COLOR = "#2c3e50"
BUTTON_CALCULATE_BG = "#27ae60"
BUTTON_MIRAB_BG = "#e67e22"
BUTTON_TEXT_COLOR = "white"
RESULT_DEFAULT_COLOR = "#34495e"
RESULT_BG_COLOR = "#ecf0f1"
