import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import os
import platform
import random

class WaterReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hydration Buddy")
        self.root.geometry("350x200") 
        self.root.configure(bg="#ffffff") 

        try:
            self.root.eval('tk::PlaceWindow . center')
        except tk.TclError:
            pass 

        self.glasses_drunk = 0
        self.daily_goal = 8

        self.interval = tk.IntVar(value=60) 

        tk.Label(root, text="How often should I remind you?", 
                 font=("Segoe UI", 12, "bold"), bg="#ffffff", fg="#2c3e50").pack(pady=(25, 15))
        
        radio_frame = tk.Frame(root, bg="#ffffff")
        radio_frame.pack(pady=5)
        
        radio_kwargs = {"bg": "#ffffff", "font": ("Segoe UI", 11), "activebackground": "#ffffff", "cursor": "hand2"}
        tk.Radiobutton(radio_frame, text="30 Mins", variable=self.interval, value=30, **radio_kwargs).pack(side=tk.LEFT, padx=15)
        tk.Radiobutton(radio_frame, text="1 Hour", variable=self.interval, value=60, **radio_kwargs).pack(side=tk.LEFT, padx=15)

        start_btn = tk.Button(root, text="START TRACKER", command=self.test_reminder, 
                              font=("Segoe UI", 10, "bold"), bg="#3498db", fg="white", 
                              activebackground="#2980b9", activeforeground="white",
                              relief="flat", padx=20, pady=8, cursor="hand2", bd=0)
        start_btn.pack(pady=(20, 10))

        self.reminder_window = None
        self.timer_id = None
        
        self.gif_frames = []
        self.current_frame = 0
        self.gif_loop_id = None
        self.gif_label = None 

    def test_reminder(self):
        self.root.withdraw() 
        self.show_reminder()

    def schedule_reminder(self, minutes):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        ms = minutes * 60 * 1000 
        self.timer_id = self.root.after(ms, self.show_reminder)

    def show_reminder(self):
        if self.reminder_window is not None and self.reminder_window.winfo_exists():
            return 

        self.reminder_window = tk.Toplevel(self.root)
        self.reminder_window.title("Hydrate!")
        self.reminder_window.overrideredirect(True)
        self.reminder_window.attributes("-topmost", True) 

        self.trans_color = '#000001' 
        
        if platform.system() == "Windows":
            self.reminder_window.configure(bg=self.trans_color)
            self.reminder_window.attributes("-transparentcolor", self.trans_color)
        elif platform.system() == "Darwin":
            self.reminder_window.configure(bg='systemTransparent')
            self.reminder_window.attributes("-transparent", True)
            self.trans_color = 'systemTransparent' 
        else:
            self.reminder_window.configure(bg=self.trans_color)

        self.window_width = 320
        self.window_height = 450
        self.screen_width = self.reminder_window.winfo_screenwidth()
        self.screen_height = self.reminder_window.winfo_screenheight()
        
        x_pos = self.screen_width - self.window_width - 50
        y_pos = self.screen_height - self.window_height - 100 
        self.reminder_window.geometry(f"{self.window_width}x{self.window_height}+{x_pos}+{y_pos}")

        self.msg_frame = tk.Frame(self.reminder_window, bg="white", highlightbackground="black", highlightthickness=2)
        self.msg_frame.place(relx=0.5, y=60, anchor="center")
        
        self.msg_label = tk.Label(self.msg_frame, text="TIME TO DRINK WATER TO\nKEEP YOUR SKIN GLOWING!", 
                                  font=("Courier", 10, "bold"), bg="white", fg="black", padx=15, pady=10, justify="center")
        self.msg_label.pack()

        self.gif_label = tk.Label(self.reminder_window, bg=self.trans_color)
        self.gif_label.place(relx=0.5, y=240, anchor="center") 

        self.btn_frame = tk.Frame(self.reminder_window, bg=self.trans_color)
        self.btn_frame.place(relx=0.5, y=410, anchor="center")
        
        yes_btn = tk.Label(self.btn_frame, text="YES, I DRANK", font=("Courier", 10, "bold"),
                           bg="#00E676", fg="black", highlightbackground="black", highlightthickness=2, padx=15, pady=8, cursor="hand2")
        yes_btn.pack(side=tk.LEFT, padx=10)
        yes_btn.bind("<Button-1>", self.drank_water) 

        snooze_btn = tk.Label(self.btn_frame, text="SNOOZE", font=("Courier", 10, "bold"),
                              bg="#E0E0E0", fg="black", highlightbackground="black", highlightthickness=2, padx=25, pady=8, cursor="hand2")
        snooze_btn.pack(side=tk.LEFT, padx=10)
        snooze_btn.bind("<Button-1>", self.snooze)

        # APNI FILE KA NAAM
        self.load_and_play_gif("water reminder.gif") 

    def load_and_play_gif(self, file_path):
        if self.gif_loop_id:
            self.reminder_window.after_cancel(self.gif_loop_id)

        try:
            if not os.path.exists(file_path):
                 self.msg_label.config(text=f"Image missing!")
                 return

            img = Image.open(file_path)
            self.gif_frames = []
            
            for frame in ImageSequence.Iterator(img):
                frame = frame.convert("RGBA")
                resized_frame = frame.resize((160, 220)) 
                photo_image = ImageTk.PhotoImage(resized_frame)
                self.gif_frames.append(photo_image)
                
            self.current_frame = 0
            self.animate_gif()
        except Exception as e:
            pass

    def animate_gif(self):
        if self.gif_frames and self.reminder_window and self.reminder_window.winfo_exists():
            frame = self.gif_frames[self.current_frame]
            self.gif_label.configure(image=frame)
            self.gif_label.image = frame 
            
            if len(self.gif_frames) > 1:
                self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
                self.gif_loop_id = self.reminder_window.after(40, self.animate_gif)

    def drank_water(self, event=None):
        previous_glasses = self.glasses_drunk
        self.glasses_drunk += 1
        if self.glasses_drunk > self.daily_goal:
             self.glasses_drunk = self.daily_goal

        self.btn_frame.place_forget() 
        self.gif_label.place_forget()
        self.msg_label.config(text="GOOD JOB!", fg="#27ae60")
        
        self.success_canvas = tk.Canvas(self.reminder_window, width=200, height=250, bg=self.trans_color, highlightthickness=0)
        self.success_canvas.place(relx=0.5, y=240, anchor="center")


        self.success_canvas.create_oval(25, 50, 175, 200, outline="#e0e0e0", width=15)
        
        self.success_canvas.create_oval(34, 59, 166, 191, fill="white", outline="")
        
        self.start_angle = -(previous_glasses / self.daily_goal) * 360
        self.target_angle = -(self.glasses_drunk / self.daily_goal) * 360
        self.current_angle = self.start_angle
        
        self.arc_id = self.success_canvas.create_arc(25, 50, 175, 200, start=90, extent=self.current_angle, outline="#00E676", width=15, style=tk.ARC)

        self.success_canvas.create_text(100, 125, text=f"{self.glasses_drunk}/{self.daily_goal}", font=("Courier", 24, "bold"), fill="black")

        self.confetti_data = []
        colors = ["#3498db", "#e74c3c", "#f1c40f", "#2ecc71", "#9b59b6", "#FF9800"]
        
        for _ in range(40):
            x = random.randint(40, 160)
            y = random.randint(-20, 80) 
            c_color = random.choice(colors)
            rect_id = self.success_canvas.create_rectangle(x, y, x+7, y+7, fill=c_color, outline="")
            
            vx = random.uniform(-2, 2)  
            vy = random.uniform(1, 4)   
            
            self.confetti_data.append({'id': rect_id, 'vx': vx, 'vy': vy})

        self.animate_success()

        self.root.after(4000, lambda: self.reset_main_timer(self.interval.get()))

    def animate_success(self):
        if not hasattr(self, 'success_canvas') or not self.success_canvas.winfo_exists():
            return

        diff = self.target_angle - self.current_angle
        if abs(diff) > 0.5:
            self.current_angle += diff * 0.15 
            self.success_canvas.itemconfigure(self.arc_id, extent=self.current_angle)
        else:
            self.success_canvas.itemconfigure(self.arc_id, extent=self.target_angle)

        for c in self.confetti_data:
            self.success_canvas.move(c['id'], c['vx'], c['vy'])
            c['vy'] += 0.25 
            c['vx'] += random.uniform(-0.5, 0.5) 

        self.root.after(20, self.animate_success)

    def snooze(self, event=None):
        self.btn_frame.place_forget() 
        self.msg_label.config(text="I'LL COME BACK\nIN 10 MINS!", fg="black")
        self.root.after(2000, lambda: self.reset_main_timer(10))

    def reset_main_timer(self, next_interval):
        if self.gif_loop_id:
            try: self.reminder_window.after_cancel(self.gif_loop_id)
            except: pass
        if self.reminder_window and self.reminder_window.winfo_exists():
            self.reminder_window.destroy()
        
        self.schedule_reminder(next_interval)

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterReminderApp(root)
    root.mainloop()