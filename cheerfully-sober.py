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
                color = "#27ae60"  # Green
            elif bac < 0.05:
                desc = "Mild relaxation; avoid driving."
                color = "#f39c12"  # Yellow-orange
            elif bac < 0.08:
                desc = "Noticeable impairment; do not drive."
                color = "#e67e22"  # Orange
            elif bac < 0.15:
                desc = "Marked impairment; stay safe and hydrated."
                color = "#d35400"  # Dark orange
            elif bac < 0.30:
                desc = "Severe impairment; danger present."
                color = "#c0392b"  # Red
            else:
                desc = "Potentially life-threatening BAC! Seek help immediately."
                color = "#8b0000"  # Dark red

            self.result_label.config(
                text=f"Estimated BAC: {bac:.3f}%\n\n{desc}",
                fg=color,
                font=("Arial", 11, "bold")
            )

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
    
    def mirab_button_click(self):
        """Display Mirab's message"""
        messagebox.showinfo("Mirab Says...", "It looks like dashagh Robert!")
    
    def build_ui(self, root):
        """Build the user interface"""
        self.root = root
        root.title("cheerfully-sober")
        
        # Configure window
        root.resizable(False, False)
        root.geometry("450x600")
        
        # Header
        header = tk.Label(root, text="🍺 BAC Calculator 🍺", font=("Arial", 16, "bold"), fg="#2c3e50")
        header.grid(row=0, column=0, columnspan=2, pady=(20, 10))
        
        # Personal Information Frame
        personal_frame = tk.LabelFrame(root, text="Personal Information", font=("Arial", 10, "bold"), pady=10)
        personal_frame.grid(row=1, column=0, columnspan=2, padx=15, pady=(5, 10), sticky="ew")
        
        # Input fields - Personal Info
        tk.Label(personal_frame, text="Weight (kg):").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.weight_entry = tk.Entry(personal_frame, width=20)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(personal_frame, text="Height (cm):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.height_entry = tk.Entry(personal_frame, width=20)
        self.height_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(personal_frame, text="Age (years):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.age_entry = tk.Entry(personal_frame, width=20)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(personal_frame, text="Sex:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.sex_var = tk.StringVar(value="male")
        tk.OptionMenu(personal_frame, self.sex_var, "male", "female").grid(row=3, column=1, sticky="ew", padx=10, pady=5)
        
        # Drink Information Frame
        drink_frame = tk.LabelFrame(root, text="Drink Information", font=("Arial", 10, "bold"), pady=10)
        drink_frame.grid(row=2, column=0, columnspan=2, padx=15, pady=(5, 10), sticky="ew")
        
        # Input fields - Drink Info
        tk.Label(drink_frame, text="Drink volume (ml):").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.drink_volume_entry = tk.Entry(drink_frame, width=20)
        self.drink_volume_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(drink_frame, text="Drink ABV (%):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.drink_abv_entry = tk.Entry(drink_frame, width=20)
        self.drink_abv_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(drink_frame, text="Hours since first drink:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.hours_entry = tk.Entry(drink_frame, width=20)
        self.hours_entry.grid(row=2, column=1, padx=10, pady=5)

        # Calculate button
        tk.Button(
            root, 
            text="Calculate BAC", 
            command=self.calculate_bac,
            bg="#27ae60",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=8,
            cursor="hand2"
        ).grid(row=3, column=0, columnspan=2, pady=15, padx=10, sticky="ew")

        # Mirab button (for fun!)
        tk.Button(
            root, 
            text="Mirab", 
            command=self.mirab_button_click, 
            bg="#e67e22", 
            fg="white",
            font=("Arial", 9),
            padx=10,
            pady=5,
            cursor="hand2"
        ).grid(row=4, column=0, columnspan=2, pady=5, padx=10)

        # Result display
        self.result_label = tk.Label(
            root, 
            text="Enter your information and click Calculate", 
            justify="center", 
            fg="#34495e",
            font=("Arial", 10),
            bg="#ecf0f1",
            relief="solid",
            borderwidth=1,
            pady=15,
            wraplength=350
        )
        self.result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    
    def run(self):
        """Run the application"""
        root = tk.Tk()
        self.build_ui(root)
        root.mainloop()



# Module-level entry point
if __name__ == "__main__":
    app = BACCalculatorApp()
    app.run()