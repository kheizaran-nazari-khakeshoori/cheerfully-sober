"""GUI Module for BAC Calculator Application"""

import tkinter as tk
from tkinter import messagebox

from calculations import (
    calculate_alcohol_grams,
    calculate_bac,
    get_bac_description_and_color
)
from constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    HEADER_COLOR,
    BUTTON_CALCULATE_BG,
    BUTTON_MIRAB_BG,
    BUTTON_TEXT_COLOR,
    RESULT_DEFAULT_COLOR,
    RESULT_BG_COLOR
)


class BACCalculatorApp:
    """Blood Alcohol Content Calculator Application"""
    
    def __init__(self):
        """Initialize the BAC Calculator Application"""
        self.root = None
        self.weight_entry = None
        self.height_entry = None
        self.age_entry = None
        self.sex_var = None
        self.drink_volume_entry = None
        self.drink_abv_entry = None
        self.hours_entry = None
        self.result_label = None
    
    def validate_positive_number(self, new_value):
        """
        Validate that input is a positive number or empty.
        
        Args:
            new_value: The new value being entered
            
        Returns:
            True if valid, False otherwise
        """
        # Allow empty string (for clearing the field)
        if new_value == "":
            return True
        
        # Allow single decimal point
        if new_value == ".":
            return True
        
        try:
            # Try to convert to float
            value = float(new_value)
            # Reject negative numbers
            if value < 0:
                return False
            return True
        except ValueError:
            # Reject non-numeric input
            return False
    
    def calculate_bac_handler(self):
        """Handle BAC calculation from user inputs"""
        try:
            # Get user inputs
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            age = float(self.age_entry.get())
            sex = self.sex_var.get()
            volume = float(self.drink_volume_entry.get())
            abv = float(self.drink_abv_entry.get())
            hours = float(self.hours_entry.get())

            # Calculate alcohol grams
            alcohol_grams = calculate_alcohol_grams(volume, abv)
            
            # Calculate BAC
            bac = calculate_bac(weight, sex, alcohol_grams, hours)
            
            # Get description and color
            description, color = get_bac_description_and_color(bac)

            # Update result display
            self.result_label.config(
                text=f"Estimated BAC: {bac:.3f}%\n\n{description}",
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
        root.title(WINDOW_TITLE)
        
        # Configure window
        root.resizable(False, False)
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        
        # Register validation command
        validate_cmd = root.register(self.validate_positive_number)
        
        # Header
        header = tk.Label(
            root, 
            text="🍺 BAC Calculator 🍺", 
            font=("Arial", 16, "bold"), 
            fg=HEADER_COLOR
        )
        header.grid(row=0, column=0, columnspan=2, pady=(20, 10))
        
        # Personal Information Frame
        personal_frame = tk.LabelFrame(
            root, 
            text="Personal Information", 
            font=("Arial", 10, "bold"), 
            pady=10
        )
        personal_frame.grid(row=1, column=0, columnspan=2, padx=15, pady=(5, 10), sticky="ew")
        
        # Input fields - Personal Info
        tk.Label(personal_frame, text="Weight (kg):").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.weight_entry = tk.Entry(
            personal_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.weight_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(personal_frame, text="Height (cm):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.height_entry = tk.Entry(
            personal_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.height_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(personal_frame, text="Age (years):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.age_entry = tk.Entry(
            personal_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(personal_frame, text="Sex:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.sex_var = tk.StringVar(value="male")
        tk.OptionMenu(personal_frame, self.sex_var, "male", "female").grid(
            row=3, column=1, sticky="ew", padx=10, pady=5
        )
        
        # Drink Information Frame
        drink_frame = tk.LabelFrame(
            root, 
            text="Drink Information", 
            font=("Arial", 10, "bold"), 
            pady=10
        )
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
            command=self.calculate_bac_handler,
            bg=BUTTON_CALCULATE_BG,
            fg=BUTTON_TEXT_COLOR,
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
            bg=BUTTON_MIRAB_BG, 
            fg=BUTTON_TEXT_COLOR,
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
            fg=RESULT_DEFAULT_COLOR,
            font=("Arial", 10),
            bg=RESULT_BG_COLOR,
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
