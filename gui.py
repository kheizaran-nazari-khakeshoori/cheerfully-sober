"""GUI Module for BAC Calculator Application"""

import tkinter as tk
from tkinter import ttk
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
    RESULT_BG_COLOR,
    WEIGHT_MIN,
    WEIGHT_MAX,
    HEIGHT_MIN,
    HEIGHT_MAX,
    AGE_MIN,
    AGE_MAX,
    VOLUME_MIN,
    VOLUME_MAX,
    ABV_MIN,
    ABV_MAX,
    HOURS_MIN,
    HOURS_MAX
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
        # Error labels for inline feedback
        self.error_label = None
    
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
    
    def validate_inputs(self):
        """
        Validate all input fields and return specific error messages.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            # Validate weight
            weight = float(self.weight_entry.get())
            if weight < WEIGHT_MIN or weight > WEIGHT_MAX:
                return False, f"Weight must be between {WEIGHT_MIN}-{WEIGHT_MAX} kg"
            
            # Validate height
            height = float(self.height_entry.get())
            if height < HEIGHT_MIN or height > HEIGHT_MAX:
                return False, f"Height must be between {HEIGHT_MIN}-{HEIGHT_MAX} cm"
            
            # Validate age
            age = float(self.age_entry.get())
            if age < AGE_MIN or age > AGE_MAX:
                return False, f"Age must be between {AGE_MIN}-{AGE_MAX} years"
            
            # Validate drink volume
            volume = float(self.drink_volume_entry.get())
            if volume <= VOLUME_MIN or volume > VOLUME_MAX:
                return False, f"Drink volume must be between {VOLUME_MIN} and {VOLUME_MAX} ml"
            
            # Validate ABV
            abv = float(self.drink_abv_entry.get())
            if abv <= ABV_MIN or abv > ABV_MAX:
                return False, f"ABV must be between {ABV_MIN} and {ABV_MAX}%"
            
            # Validate hours
            hours = float(self.hours_entry.get())
            if hours < HOURS_MIN or hours > HOURS_MAX:
                return False, f"Hours must be between {HOURS_MIN}-{HOURS_MAX} hours"
            
            return True, ""
            
        except ValueError:
            return False, "Please enter valid numbers for all fields"
    
    def calculate_bac_handler(self):
        """Handle BAC calculation from user inputs"""
        # Validate inputs first
        is_valid, error_message = self.validate_inputs()
        
        if not is_valid:
            # Display error in label
            self.error_label.config(text=f"⚠ {error_message}")
            # Also show popup for critical errors
            messagebox.showerror("Validation Error", error_message)
            return
        
        # Clear any previous error messages
        self.error_label.config(text="")
        
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
            error_msg = "Please enter valid numbers for all fields"
            self.error_label.config(text=f"⚠ {error_msg}")
            messagebox.showerror("Input Error", error_msg)
    
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
        
        # Configure ttk style for modern appearance
        style = ttk.Style()
        style.theme_use('clam')  # Modern, cross-platform theme
        
        # Configure custom styles
        style.configure('Header.TLabel', 
                       font=('Arial', 16, 'bold'),
                       foreground=HEADER_COLOR,
                       padding=10)
        style.configure('TLabelframe.Label', 
                       font=('Arial', 10, 'bold'))
        style.configure('Calculate.TButton',
                       font=('Arial', 11, 'bold'),
                       background=BUTTON_CALCULATE_BG,
                       foreground=BUTTON_TEXT_COLOR,
                       padding=10)
        style.configure('Mirab.TButton',
                       font=('Arial', 9),
                       background=BUTTON_MIRAB_BG,
                       foreground=BUTTON_TEXT_COLOR,
                       padding=8)
        
        # Register validation command
        validate_cmd = root.register(self.validate_positive_number)
        
        # Header
        header = ttk.Label(
            root, 
            text="🍺 BAC Calculator 🍺",
            style='Header.TLabel'
        )
        header.grid(row=0, column=0, columnspan=2, pady=(20, 10))
        
        # Personal Information Frame
        personal_frame = ttk.LabelFrame(
            root, 
            text="Personal Information",
            padding=(15, 10)
        )
        personal_frame.grid(row=1, column=0, columnspan=2, padx=15, pady=(5, 10), sticky="ew")
        
        # Input fields - Personal Info
        ttk.Label(personal_frame, text="Weight (kg):").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.weight_entry = ttk.Entry(
            personal_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.weight_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(personal_frame, text="Height (cm):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.height_entry = ttk.Entry(
            personal_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.height_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(personal_frame, text="Age (years):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.age_entry = ttk.Entry(
            personal_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(personal_frame, text="Sex:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.sex_var = tk.StringVar(value="male")
        sex_combo = ttk.Combobox(personal_frame, textvariable=self.sex_var, 
                                 values=["male", "female"], state="readonly", width=18)
        sex_combo.grid(row=3, column=1, sticky="ew", padx=10, pady=5)
        
        # Drink Information Frame
        drink_frame = ttk.LabelFrame(
            root, 
            text="Drink Information",
            padding=(15, 10)
        )
        drink_frame.grid(row=2, column=0, columnspan=2, padx=15, pady=(5, 10), sticky="ew")
        
        # Input fields - Drink Info
        ttk.Label(drink_frame, text="Drink volume (ml):").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.drink_volume_entry = ttk.Entry(
            drink_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.drink_volume_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(drink_frame, text="Drink ABV (%):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.drink_abv_entry = ttk.Entry(
            drink_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.drink_abv_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(drink_frame, text="Hours since first drink:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.hours_entry = ttk.Entry(
            drink_frame, 
            width=20,
            validate='key',
            validatecommand=(validate_cmd, '%P')
        )
        self.hours_entry.grid(row=2, column=1, padx=10, pady=5)

        # Calculate button
        calculate_btn = ttk.Button(
            root, 
            text="Calculate BAC", 
            command=self.calculate_bac_handler,
            style='Calculate.TButton',
            cursor="hand2"
        )
        calculate_btn.grid(row=3, column=0, columnspan=2, pady=15, padx=15, sticky="ew")

        # Results Frame
        results_frame = ttk.LabelFrame(
            root,
            text="Results",
            padding=(15, 10)
        )
        results_frame.grid(row=4, column=0, columnspan=2, padx=15, pady=(5, 10), sticky="ew")

        # Error message label
        self.error_label = tk.Label(
            results_frame,
            text="",
            font=("Arial", 9),
            fg="#c0392b",  # Red color for errors
            wraplength=380,
            justify="center"
        )
        self.error_label.grid(row=0, column=0, columnspan=2, padx=5, pady=(0, 5))

        # Mirab button (for fun!)
        mirab_btn = ttk.Button(
            root, 
            text="Mirab", 
            command=self.mirab_button_click,
            style='Mirab.TButton',
            cursor="hand2"
        )
        mirab_btn.grid(row=5, column=0, columnspan=2, pady=(5, 10), padx=15, sticky="ew")

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
            pady=20,
            padx=10,
            wraplength=380
        )
        self.result_label.grid(row=6, column=0, columnspan=2, padx=15, pady=(5, 15), sticky="ew")
    
    def run(self):
        """Run the application"""
        root = tk.Tk()
        self.build_ui(root)
        root.mainloop()
