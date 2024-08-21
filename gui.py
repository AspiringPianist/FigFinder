# gui.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import calendarAPI
import aiScheduler
import databaseAPI

class TravelCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Group Travel Calendar")
        
        # Frame for calendar synchronization
        self.sync_frame = ttk.LabelFrame(root, text="Calendar Synchronization", padding=10)
        self.sync_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.sync_button = ttk.Button(self.sync_frame, text="Sync Calendars", command=self.sync_calendars)
        self.sync_button.grid(row=0, column=0, padx=10, pady=10)

        # Frame for availability visualization
        self.avail_frame = ttk.LabelFrame(root, text="Availability Visualization", padding=10)
        self.avail_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.avail_button = ttk.Button(self.avail_frame, text="Show Availability", command=self.show_availability)
        self.avail_button.grid(row=0, column=0, padx=10, pady=10)

        self.avail_text = tk.Text(self.avail_frame, height=10, width=50)
        self.avail_text.grid(row=1, column=0, padx=10, pady=10)

        # Frame for scheduling suggestions
        self.suggest_frame = ttk.LabelFrame(root, text="Scheduling Suggestions", padding=10)
        self.suggest_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.suggest_button = ttk.Button(self.suggest_frame, text="Generate Suggestions", command=self.generate_suggestions)
        self.suggest_button.grid(row=0, column=0, padx=10, pady=10)

        self.suggest_text = tk.Text(self.suggest_frame, height=10, width=50)
        self.suggest_text.grid(row=1, column=0, padx=10, pady=10)

        # Frame for notifications
        self.notify_frame = ttk.LabelFrame(root, text="Notifications", padding=10)
        self.notify_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.notify_button = ttk.Button(self.notify_frame, text="Send Notifications", command=self.send_notifications)
        self.notify_button.grid(row=0, column=0, padx=10, pady=10)

    def sync_calendars(self):
        calendarAPI.sync_calendars('user_email@example.com')
        messagebox.showinfo("Sync", "Calendars synchronized successfully!")

    def show_availability(self):
        availability = aiScheduler.get_group_availability('group_id')
        self.avail_text.delete(1.0, tk.END)
        self.avail_text.insert(tk.END, f"Displaying availability: {availability}")

    def generate_suggestions(self):
        suggestions = aiScheduler.generate_scheduling_suggestions('group_id')
        self.suggest_text.delete(1.0, tk.END)
        self.suggest_text.insert(tk.END, f"Scheduling suggestions: {suggestions}")

    def send_notifications(self):
        databaseAPI.send_notifications()
        messagebox.showinfo("Notifications", "Notifications sent!")

def run_gui():
    root = tk.Tk()
    app = TravelCalendarApp(root)
    root.mainloop()