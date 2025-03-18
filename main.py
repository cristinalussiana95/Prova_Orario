import random
import tkinter as tk
from tkinter import ttk

#vincoli giorni e orari
def generate_schedule(teachers):
    days = ["Lunedi", "Martedi", "Mercoledi'", "Giovedi'", "Venerdi'"]
    primary_schedule = ["8:00-9:15", "9:15-10:10", "10:10-11:15", "11:15-12:10", "12:10-13:00"]
    middle_schedule = ["8:05-9:00", "9:00-9:50", "9:50-10:05", "10:05-11:00", "11:00-11:55", "12:10-13:05", "13:05-14:00"]
    high_schedule = ["8:00-8:50", "8:50-9:40", "9:40-11:20", "11:40-12:20", "12:20-13:20", "13:20-14:10"]
    
    #no sovrapposizione orario
    all_schedules = {day: set() for day in days}  
    schedule = {teacher: {day: [] for day in days} for teacher in teachers}
    
    for teacher, levels in teachers.items():
        available_slots = {
            "Primaria": list(primary_schedule),
            "Medie": list(middle_schedule),
            "Liceo": list(high_schedule)
        }
        
        for day in days:
            assigned_slots = []
            for level, hours in levels.items():
                for _ in range(hours // len(days) + (1 if random.random() > 0.5 else 0)):
                    if available_slots[level]:
                        random.shuffle(available_slots[level])
                        for slot in available_slots[level]:
                            if slot not in all_schedules[day]:  
                                available_slots[level].remove(slot)
                                all_schedules[day].add(slot)
                                assigned_slots.append(f"{level}: {slot}")
                                break
            schedule[teacher][day] = assigned_slots
    
    return schedule

#interfaccia dell'orario
def display_schedule():
    teachers = {}
    for i in range(len(teacher_entries)):
        name = teacher_entries[i].get()
        if name:
            teachers[name] = {
                "Primaria": int(primary_entries[i].get() or 0),
                "Medie": int(middle_entries[i].get() or 0),
                "Liceo": int(high_entries[i].get() or 0),
            }
    
    schedule = generate_schedule(teachers)
    result_text.delete(1.0, tk.END)
    for teacher, days in schedule.items():
        result_text.insert(tk.END, f"{teacher}: \n")
        for day, slots in days.items():
            result_text.insert(tk.END, f"  {day}:\n")
            for slot in slots:
                result_text.insert(tk.END, f"    - {slot}\n")
        result_text.insert(tk.END, "\n")

#aggiungere docente
def add_teacher_entry():
    row = len(teacher_entries)
    teacher_entries.append(ttk.Entry(root))
    teacher_entries[-1].grid(row=row+1, column=0)
    primary_entries.append(ttk.Entry(root, width=5))
    primary_entries[-1].grid(row=row+1, column=1)
    middle_entries.append(ttk.Entry(root, width=5))
    middle_entries[-1].grid(row=row+1, column=2)
    high_entries.append(ttk.Entry(root, width=5))
    high_entries[-1].grid(row=row+1, column=3)

root = tk.Tk()
root.title("School Schedule Generator")

# Top interfaccia
ttk.Label(root, text="Nome Docente").grid(row=0, column=0)
ttk.Label(root, text="Ore Primaria").grid(row=0, column=1)
ttk.Label(root, text="Ore Medie").grid(row=0, column=2)
ttk.Label(root, text="Ore Liceo").grid(row=0, column=3)

teacher_entries = []
primary_entries = []
middle_entries = []
high_entries = []

add_teacher_entry()
