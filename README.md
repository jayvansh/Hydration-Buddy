💧 Hydration Buddy – Water Reminder

A simple and interactive Water Reminder Desktop App built using Python, Tkinter and Pillow.
It reminds you to drink water, tracks your daily water intake, and shows an animated progress indicator after drinking water.

✨ Features
💧 Water drinking reminders
⏰ Choose reminder interval:
30 Minutes
1 Hour
🥤 Daily goal of 8 glasses
🎞️ Animated GIF reminder
✅ "YES, I DRANK" button
😴 "SNOOZE" option for 10 minutes
📊 Animated water intake progress circle
🎉 Confetti animation after drinking water
🖥️ Windows/macOS transparency support
🎨 Simple and clean GUI
🛠️ Technologies Used
Python
Tkinter – GUI
Pillow (PIL) – GIF/image handling
Random – Confetti animation
Platform – Operating-system detection

The project imports Tkinter, Pillow's image modules, OS/platform utilities, and random for the application's functionality.

📂 Project Structure
Hydration-Buddy/
│
├── water_reminder.py
├── water reminder.gif
└── README.md

🚀 Installation
1. Clone the repository
git clone https://github.com/jayvansh/Hydration-Buddy.git
cd Hydration-Buddy
2. Install Pillow
pip install pillow
3. Run the application
python water_reminder.py
🎮 How It Works
Open the application.
Select 30 Mins or 1 Hour.
Click START TRACKER.
A hydration reminder will appear.
Click YES, I DRANK after drinking water.
Your progress will increase toward the 8-glass daily goal.
If you don't want to drink yet, click SNOOZE.
The reminder will return after 10 minutes.

The app starts with a daily goal of 8 glasses and lets the user select a 30-minute or 1-hour interval.

📈 Progress Tracking

After clicking YES, I DRANK, the application:

Increases the number of glasses consumed
Updates the circular progress indicator
Displays the current progress, such as 3/8
Shows a confetti animation
Starts the next reminder cycle

😴 Snooze

Don't want to drink water right now?

Click SNOOZE and the application will remind you again after 10 minutes.

🖼️ GIF Support

The application loads water reminder.gif, converts its frames and displays them as an animation inside the reminder window.

📌 Requirements
Python 3.x
Pillow
Tkinter

Tkinter is usually included with standard Python installations.

👨‍💻 Author

Jayvansh Baria

Made with ❤️ using Python 🐍