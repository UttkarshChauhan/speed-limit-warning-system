import tkinter as tk
from tkinter import messagebox


def get_speed_alert(speed_limit, current_speed):
    """
    Returns a tuple: (icon, message)
    """
    try:
        lmt = float(speed_limit)
        crnt = float(current_speed)
        if crnt <= lmt:
            return "✅", f"OK. Your speed ({crnt:.1f}) is within the limit ({lmt:.1f})."

        exceeded_by = crnt - lmt

        #  Alert 
        if 0 < exceeded_by <= 5:
            icon = "⚠️"
            message = f"WARNING! exceeded the limit by {exceeded_by:.1f}."
        elif 5 < exceeded_by <= 15:
            icon = "🚨"
            message = f"ALERT!  speed detected. Over limit by {exceeded_by:.1f}."
        else: # exceeded by > 15
            icon = "🛑"
            message = f"CRITICAL! Dangerous speed detected. Over limit by {exceeded_by:.1f}."

        return icon, message

    except ValueError:
        return "❌", "Error: Please enter valid numbers for both speeds."
    except Exception as e:
        return "❓", f"An unexpected error occurred: {e}"



class SpeedAlertApp:
    def __init__(self, master):
        self.master = master
        master.title("🚗 Speed Alert Simulator")
        master.geometry("400x300")
        master.config(bg="#f0f0f0")

        # --- Variables ---
        self.limit_var = tk.StringVar(master, value="50")
        self.speed_var = tk.StringVar(master, value="55")
        
        # Result label to show the output
        self.result_var = tk.StringVar(master)
        self.result_var.set("Enter speeds and click 'Check Speed'")

        # --- Widgets Layout ---

        # 1. Speed Limit Input
        tk.Label(master, text="Speed Limit:", bg="#f0f0f0", font=('Arial', 10, 'bold')).pack(pady=(10, 0))
        self.limit_entry = tk.Entry(master, textvariable=self.limit_var, justify='center', font=('Arial', 12))
        self.limit_entry.pack(pady=5, padx=20)

        # 2. Current Speed Input
        tk.Label(master, text="Current Speed:", bg="#f0f0f0", font=('Arial', 10, 'bold')).pack(pady=(10, 0))
        self.speed_entry = tk.Entry(master, textvariable=self.speed_var, justify='center', font=('Arial', 12))
        self.speed_entry.pack(pady=5, padx=20)
        
        # 3. Check Button
        self.check_button = tk.Button(master, 
                                      text="Check Speed", 
                                      command=self.check_speed, 
                                      bg="#4CAF50", 
                                      fg="white", 
                                      font=('Arial', 12, 'bold'))
        self.check_button.pack(pady=20)

        # 4. Result Display Label
        self.result_label = tk.Label(master, 
                                     textvariable=self.result_var, 
                                     bg="#e0e0e0", 
                                     fg="#333", 
                                     wraplength=350,
                                     padx=10, 
                                     pady=10,
                                     font=('Arial', 11))
        self.result_label.pack(pady=10, fill='x', padx=20)
        
        # Bind the Enter key to the check_speed function for convenience
        master.bind('<Return>', lambda event: self.check_speed())
        

    def check_speed(self):
        """
        Retrieves input, runs the backend logic, and updates the GUI.
        """
        lmt = self.limit_var.get()
        spd = self.speed_var.get()
        
        # Call the modified backend function
        icon, message = get_speed_alert(lmt, spd)
        
        # Update the result label
        full_message = f"{icon} {message}"
        self.result_var.set(full_message)



if __name__ == '__main__':
    root = tk.Tk()
    app = SpeedAlertApp(root)
    root.mainloop()
