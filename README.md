# 💧 Hydration Buddy – Water Reminder

A simple and interactive Water Reminder Desktop App built using **Python, Tkinter and Pillow**.

Hydration Buddy reminds you to drink water, tracks your daily water intake, and provides an animated progress indicator after drinking water.

---

## ✨ Features

- 💧 Water drinking reminders
- ⏰ Choose reminder interval:
  - 30 Minutes
  - 1 Hour
- 🥤 Daily goal of 8 glasses
- 🎞️ Animated GIF reminder
- ✅ "YES, I DRANK" button
- 😴 "SNOOZE" option for 10 minutes
- 📊 Animated water intake progress circle
- 🎉 Confetti animation after drinking water
- 🖥️ Windows/macOS transparency support
- 🎨 Simple and clean GUI

---

## 🛠️ Technologies Used

- 🐍 Python
- 🖼️ Tkinter – GUI
- 🖼️ Pillow (PIL) – GIF/Image handling
- 🎲 Random – Confetti animation
- 💻 Platform – Operating-system detection

---

## 📂 Project Structure

```text
Hydration-Buddy/
│
├── water_reminder.py
├── water reminder.gif
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jayvansh/Hydration-Buddy.git
```

### 2. Open the Project Folder

```bash
cd Hydration-Buddy
```

### 3. Install Pillow

Pillow is required for loading and displaying the animated GIF.

```bash
pip install pillow
```

### 4. Run the Application

```bash
python water_reminder.py
```

---

## 🎮 How It Works

1. Open the application.
2. Select how often you want to receive reminders.
3. Choose **30 Minutes** or **1 Hour**.
4. Click **START TRACKER**.
5. The hydration reminder will appear.
6. Drink water and click **YES, I DRANK**.
7. Your water intake progress will increase.
8. A progress circle and confetti animation will appear.
9. If you don't want to drink water immediately, click **SNOOZE**.
10. The reminder will return after 10 minutes.

---

## 📊 Water Intake Tracking

The application starts with a daily goal of **8 glasses**.

Every time you click **YES, I DRANK**:

- 🥤 Your glass count increases
- 📈 The progress circle updates
- 🎉 Confetti animation appears
- 🔄 The next reminder is scheduled

### Example

```text
3 / 8
```

This means you have consumed **3 glasses out of your daily goal of 8 glasses**.

---

## 😴 Snooze Feature

Don't want to drink water right now?

Click the:

```text
SNOOZE
```

button.

The application will remind you again after **10 minutes**.

---

## 🎞️ Animated GIF

The project uses an animated GIF to display the hydration character inside the reminder window.

Make sure the GIF is present in the same folder as the Python program:

```text
water reminder.gif
```

The application automatically loads and animates the GIF when the reminder appears.

---

## 🖥️ User Interface

The application includes:

- 💧 Hydration reminder popup
- 🎞️ Animated character
- 🥤 Water intake tracker
- 📊 Circular progress indicator
- 🎉 Confetti animation
- ✅ Interactive "YES, I DRANK" button
- 😴 Snooze button
- 🎨 Clean desktop interface

---

## ⚙️ Main Settings

```text
Daily Goal: 8 glasses

Reminder Options:
- 30 Minutes
- 1 Hour

Snooze:
- 10 Minutes
```

---

## 📦 Requirements

Before running the project, make sure you have:

```text
Python 3.x
Pillow
Tkinter
```

### Python

Download and install **Python 3.x** on your computer.

### Pillow

Install Pillow using:

```bash
pip install pillow
```

### Tkinter

Tkinter is used to create the desktop GUI.

It is normally included with standard Python installations.

---

## 🧩 Project Files

### `water_reminder.py`

The main Python file containing:

- GUI
- Reminder system
- Timer
- Water intake tracking
- Progress indicator
- Confetti animation
- Snooze functionality
- GIF animation

### `water reminder.gif`

The animated hydration character displayed in the reminder popup.

### `README.md`

This documentation file containing project information and setup instructions.

---

## 🔄 Reminder System

The application allows the user to select a reminder interval.

Available options:

```text
30 Minutes
1 Hour
```

After the selected time, the hydration reminder appears automatically.

---

## 🎉 Success Animation

After clicking **YES, I DRANK**, the application displays:

- 🥤 Updated water intake
- 📊 Circular progress animation
- 🎉 "GOOD JOB!" message
- 🎊 Confetti animation

This provides visual feedback whenever you record a glass of water.

---

## 💤 Snooze System

If you click **SNOOZE**, the current reminder is closed and the application schedules another reminder after:

```text
10 Minutes
```

---

## 🖥️ Platform Support

The application includes platform-specific window transparency handling for:

- 🪟 Windows
- 🍎 macOS
- 💻 Other desktop platforms

---

## 🎯 Future Improvements

Possible improvements for future versions:

- 📅 Daily and weekly water history
- 💾 Save water intake data
- 📊 Detailed hydration statistics
- 🔔 Custom notification sounds
- ⚙️ Custom daily water goals
- 🕐 Custom reminder intervals
- 🎨 More UI themes
- 🌙 Dark mode
- 🏆 Hydration streak system
- 📈 Weekly/monthly progress charts

---

## 🚀 Future Version Ideas

### Version 2.0

- User-defined water goal
- Custom reminder time
- Better notification system
- Data persistence

### Version 3.0

- Hydration statistics
- Streak tracking
- Weekly reports
- More animations
- Improved UI

---

## 👨‍💻 Author

**Jayvansh Baria**

Made with ❤️ and Python 🐍

---

## ⭐ Support

If you like this project, consider giving the repository a ⭐ on GitHub!

---

## 🏷️ GitHub Topics

```text
python
tkinter
water-reminder
hydration
desktop-app
python-project
pillow
gui
beginner-python
water-tracker
python-gui
hydration-app
```

---

## 📄 License

This project is created for learning and personal use.

Feel free to explore, modify and improve the project.
