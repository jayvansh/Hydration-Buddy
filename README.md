# 💧 Hydration Buddy – Water Reminder

A simple and interactive Water Reminder Desktop App built using **Python**, **Tkinter**, and **Pillow**. It reminds you to drink water, tracks your daily water intake, and displays an animated progress indicator with celebrations after each glass!

---

## ✨ Features

* 💧 **Water Drinking Reminders:** Timely alerts to keep you hydrated throughout the day.
* ⏰ **Customizable Intervals:** Choose between **30 Minutes** or **1 Hour** reminder frequencies.
* 🥤 **Daily Goal Tracker:** Targets a daily goal of **8 glasses**.
* 🎞️ **Animated GIF Alerts:** Displays frame-by-frame GIF animations inside reminder windows.
* ✅ **One-Click Tracking:** Quick `"YES, I DRANK"` button to register intake.
* 😴 **Snooze Option:** Snooze reminders for **10 minutes** if you're busy.
* 📊 **Animated Progress Circle:** Visual circular indicator tracking your daily intake progress (e.g., `3/8`).
* 🎉 **Confetti Animation:** Fun celebratory animation triggered upon drinking water.
* 🖥️ **Cross-Platform:** Includes transparency support tailored for Windows and macOS.
* 🎨 **Clean GUI:** Simple, lightweight, and modern user interface.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Tkinter** – Standard Python library for GUI development
* **Pillow (PIL)** – Image and animated GIF handling
* **Random** – Confetti animation physics/rendering
* **Platform** – OS detection for platform-specific UI adjustments

---

## 📂 Project Structure

```text
Hydration-Buddy/
│
├── water_reminder.py
├── water reminder.gif
└── README.md

🚀 Installation
1. Clone the Repository
git clone https://github.com/jayvansh/Hydration-Buddy.git
2. Open the Project Folder
cd Hydration-Buddy
3. Install Pillow

Pillow is required for loading and displaying the animated GIF.

pip install pillow
4. Run the Application
python water_reminder.py
🎮 How It Works
Open the application.
Select how often you want to receive reminders.
Choose 30 Minutes or 1 Hour.
Click START TRACKER.
The hydration reminder will appear.
Drink water and click YES, I DRANK.
Your water intake progress will increase.
A progress circle and confetti animation will appear.
If you don't want to drink water immediately, click SNOOZE.
The reminder will return after 10 minutes.
📊 Water Intake Tracking

The application starts with a daily goal of 8 glasses.

Every time you click YES, I DRANK:

🥤 Your glass count increases
📈 The progress circle updates
🎉 Confetti animation appears
🔄 The next reminder is scheduled

Example:

3 / 8

This means you have consumed 3 glasses out of your daily goal of 8 glasses.

😴 Snooze Feature

Don't want to drink water right now?

Click the:

SNOOZE

button.

The application will remind you again after 10 minutes.

🎞️ Animated GIF

The project uses an animated GIF to display the hydration character inside the reminder window.

Make sure the GIF is present in the same folder as the Python program:

water reminder.gif

The application automatically loads and animates the GIF when the reminder appears.

🖥️ User Interface

The application includes:

💧 Hydration reminder popup
🎞️ Animated character
🥤 Water intake tracker
📊 Circular progress indicator
🎉 Confetti animation
✅ Interactive "YES, I DRANK" button
😴 Snooze button
🎨 Clean desktop interface
⚙️ Main Settings
Daily Goal: 8 glasses

Reminder Options:
- 30 Minutes
- 1 Hour

Snooze:
- 10 Minutes
📦 Requirements

Before running the project, make sure you have:

Python 3.x
Pillow
Tkinter
Python

Download and install Python 3.x on your computer.

Pillow

Install Pillow using:

pip install pillow
Tkinter

Tkinter is used to create the desktop GUI.

It is normally included with standard Python installations.

🧩 Project Files
water_reminder.py

The main Python file containing:

GUI
Reminder system
Timer
Water intake tracking
Progress indicator
Confetti animation
Snooze functionality
GIF animation
water reminder.gif

The animated hydration character displayed in the reminder popup.

README.md

This documentation file containing project information and setup instructions.

🔄 Reminder System

The application allows the user to select a reminder interval.

Available options:

30 Minutes
1 Hour

After the selected time, the hydration reminder appears automatically.

🎉 Success Animation

After clicking YES, I DRANK, the application displays:

Updated water intake
Circular progress animation
"GOOD JOB!" message
Confetti animation

This provides visual feedback whenever you record a glass of water.

💤 Snooze System

If you click SNOOZE, the current reminder is closed and the application schedules another reminder after:

10 Minutes
🖥️ Platform Support

The application includes platform-specific window transparency handling for:

Windows
macOS
Other desktop platforms
🎯 Future Improvements

Possible improvements for future versions:

📅 Daily and weekly water history
💾 Save water intake data
📊 Detailed hydration statistics
🔔 Custom notification sounds
⚙️ Custom daily water goals
🕐 Custom reminder intervals
🎨 More UI themes
🌙 Dark mode
🏆 Hydration streak system
📈 Weekly/monthly progress charts
🚀 Future Version Ideas
Version 2.0
User-defined water goal
Custom reminder time
Better notification system
Data persistence
Version 3.0
Hydration statistics
Streak tracking
Weekly reports
More animations
Improved UI
👨‍💻 Author

Jayvansh Baria

Made with ❤️ and Python 🐍
