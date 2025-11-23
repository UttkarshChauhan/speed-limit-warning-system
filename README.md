# ???? Project Title: Speed Limit Alert Simulator

## ???? Description

This project is a simple simulation of a vehicle speed limit alert system. It requires the input of the **official speed limit** and the **current vehicle speed**, and it gives the user instant feedback about the speed, categorizing it as **OK**, **Warning**, **Alert**, or **Critical** based on predefined thresholds.

It includes both a **Command-Line Interface (CLI)** version for an initial implementation and also a **Graphical User Interface (GUI)** version, implemented using Tkinter.

Features

* **GUI Interface:** User-friendly input fields, immediate visual feedback using **Tkinter.
• **Tiered Alert System**: Distinguishes between minor and critical speed offenses.
* **Warning ⚠️:** Up to 5 units over the limit.
* **Alert (????):** 5 to 15 units over the limit.
* **Critical :** More than 15 units over the limit.

* **Strong Input**: Includes error handling in case of non-numeric input.

Getting Started

Prerequisites

To run this simulator, you need to have Python installed on your system.

* **Python 3.x

* **Tkinter** (Usually included with standard Python installations)
Installation
1. **Clone the repository:
```bash
git clone https://github.com/yourusername/speed-alert-simulator.git

cd speed-alert-simulator

```

2. **Save the Code:** Save the given Python code containing the core logic and the Tkinter implementation in a file named `speed_alert_app.py`.

Usage #### 1. Running the GUI Version Run the main Python file to start the graphical interface: ```bash python speed_alert_app.py
