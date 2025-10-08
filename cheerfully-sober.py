import tkinter as tk
from tkinter import messagebox

#constants 
R_man = 0.68
R_woman = 0.55
ETHANOL_DENSITY_G_ML = 0.789 # g/mL
ELIMINATION_RATE_PER_HR = 0.015 # % per hour


def calculate_bac():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = float(age_entry.get())
        sex = sex_var.get()
        volume= float(drink_volume_entry.get())
        abv = float(drink_abv_entry.get())
        hours = float(hours_entry.get())

        #conver drink to gram
        alcohol_grams = volume * (abv / 100) * ETHANOL_DENSITY_G_ML
        
       
        if sex.lower() == "male":
            r = R_man

        else:
            r = R_woman
             

        #BAC calculation 

        weight_g = weight * 1000
        bac = (alcohol_grams / (weight_g * r)) * 100
        bac -= ELIMINATION_RATE_PER_HR * hours 
        bac = max(bac, 0.0)

        #Descriotion 
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

        result_label.config(text=f"Estimated BAC: {bac:.3f}%\n{desc}")


    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")


def mirab_button_click():
    messagebox.showinfo("Mirab Says...", "It looks like dashagh Robert!")
  
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