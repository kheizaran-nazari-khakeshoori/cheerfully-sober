import tkinter as tk
from tkinter import messagebox


class BACCalculatorApp:
    """Blood Alcohol Content Calculator Application"""
    
    # Constants
    R_MAN = 0.68
    R_WOMAN = 0.55
    ETHANOL_DENSITY_G_ML = 0.789  # g/mL
    ELIMINATION_RATE_PER_HR = 0.015  # % per hour
    
    def __init__(self):
        """Initialize the BAC Calculator Application"""
        self.weight_entry = None
        self.height_entry = None
        self.age_entry = None
        self.sex_var = None
        self.drink_volume_entry = None
        self.drink_abv_entry = None
        self.hours_entry = None
        self.result_label = None
    
    def calculate_bac(self):
        """Calculate Blood Alcohol Content based on user inputs"""
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            age = float(self.age_entry.get())
            sex = self.sex_var.get()
            volume = float(self.drink_volume_entry.get())
            abv = float(self.drink_abv_entry.get())
            hours = float(self.hours_entry.get())

            # Convert drink to gram
            alcohol_grams = volume * (abv / 100) * self.ETHANOL_DENSITY_G_ML
            
            if sex.lower() == "male":
                r = self.R_MAN
            else:
                r = self.R_WOMAN
                 
            # BAC calculation 
            weight_g = weight * 1000
            bac = (alcohol_grams / (weight_g * r)) * 100
            bac -= self.ELIMINATION_RATE_PER_HR * hours 
            bac = max(bac, 0.0)

            # Description 
            if bac < 0.02:
                desc = "Minimal effects."
            elif bac < 0.05:
                desc = "Mild relaxation; avoid driving."
            elif bac < 0.08:
                desc = "Noticeable impairment; do not drive."
            elif bac < 0.15:
                desc = "Marked impairment; stay safe and hydrated."
            elif bac < 0.30:
                desc = "Severe impairment; danger present."
            else:
                desc = "Potentially life-threatening BAC! Seek help immediately."

            self.result_label.config(text=f"Estimated BAC: {bac:.3f}%\n{desc}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
    
    def mirab_button_click(self):
        """Display Mirab's message"""
        messagebox.showinfo("Mirab Says...", "It looks like dashagh Robert!")


# Module-level constants for backwards compatibility
R_man = BACCalculatorApp.R_MAN
R_woman = BACCalculatorApp.R_WOMAN
ETHANOL_DENSITY_G_ML = BACCalculatorApp.ETHANOL_DENSITY_G_ML
ELIMINATION_RATE_PER_HR = BACCalculatorApp.ELIMINATION_RATE_PER_HR

# Global app instance
app = BACCalculatorApp()


def calculate_bac():
    """Wrapper function for backwards compatibility"""
    app.calculate_bac()


def mirab_button_click():
    """Wrapper function for backwards compatibility"""
    app.mirab_button_click()
  
# Create main window
root = tk.Tk()
root.title("cheerfully-sober")

# Input fields

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

tk.Label(root, text="Height (cm):").grid(row=2, column=0, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1)

tk.Label(root, text="Age (years):").grid(row=3, column=0, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=3, column=1)

tk.Label(root, text="Sex:").grid(row=4, column=0, sticky="e")
sex_var = tk.StringVar(value="male")
tk.OptionMenu(root, sex_var, "male", "female").grid(row=4, column=1)

tk.Label(root, text="Drink volume (ml):").grid(row=5, column=0, sticky="e")
drink_volume_entry = tk.Entry(root)
drink_volume_entry.grid(row=5, column=1)

tk.Label(root, text="Drink ABV (%):").grid(row=6, column=0, sticky="e")
drink_abv_entry = tk.Entry(root)
drink_abv_entry.grid(row=6, column=1)

tk.Label(root, text="Hours since first drink:").grid(row=7, column=0, sticky="e")
hours_entry = tk.Entry(root)
hours_entry.grid(row=7, column=1)

# Calculate button
tk.Button(root, text="Calculate BAC", command=calculate_bac).grid(row=8, column=0, columnspan=2, pady=10)

# Mirab button (for fun!)
tk.Button(root, text="Mirab", command=mirab_button_click, bg="orange", fg="white").grid(row=9, column=0, columnspan=2, pady=5)

# Result display
result_label = tk.Label(root, text="", justify="left", fg="blue")
result_label.grid(row=10, column=0, columnspan=2)

root.mainloop()