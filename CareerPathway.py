import tkinter as tk
from tkinter import scrolledtext, font

def get_career_plan(career):
    plans = {
        "software engineer": [
            "Complete a Bachelor's degree in Computer Science or a related field.",
            "Learn programming languages such as Python, Java, and C#.",
            "Contribute to open-source projects to gain practical experience.",
            "Apply for internships to gain real-world experience.",
            "Build a portfolio of projects to showcase in interviews."
        ],
        "graphic designer": [
            "Earn a degree or certification in graphic design.",
            "Master design software like Adobe Photoshop, Illustrator, and InDesign.",
            "Create a strong portfolio of your designs.",
            "Start freelancing to build client relationships and experience.",
            "Stay updated with the latest design trends and technologies."
        ],
        "doctor": [
            "Complete a Bachelor’s degree with a pre-med focus.",
            "Pass the MCAT and apply to medical school.",
            "Earn your medical degree and complete residency.",
            "Obtain a license to practice medicine in your state.",
            "Consider specialization through further fellowship training."
        ],
        "civil engineer": [
            "Obtain a Bachelor's degree in Civil Engineering.",
            "Participate in internships during college to gain hands-on experience.",
            "Pass the Fundamentals of Engineering (FE) exam.",
            "Work as an Engineer-in-Training or Engineer Intern to gain experience.",
            "Pass the Principles and Practice of Engineering (PE) exam to become a licensed Professional Engineer."
        ],
        "financial analyst": [
            "Earn a bachelor’s degree in finance, economics, or a related field.",
            "Gain experience through internships in financial institutions.",
            "Consider earning a Master’s degree for advanced positions.",
            "Obtain certifications like the Chartered Financial Analyst (CFA) certification.",
            "Stay abreast of current economic conditions and understand how they influence the market."
        ],
        "teacher (K-12)": [
            "Complete a Bachelor’s degree in Education or in a specific subject with a teaching credential.",
            "Pass your state’s required exams for teacher certification.",
            "Complete student teaching experience.",
            "Apply for a teaching license in your state.",
            "Continuously update your skills with professional development."
        ]
    }
    return plans.get(career.lower(), "No plan available for this career. Try another one.")

def show_plan():
    career = career_var.get()
    if career == "Select a career":
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select a career from the list.")
        result_text.config(state=tk.DISABLED)
    else:
        steps = get_career_plan(career)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        if isinstance(steps, list):
            formatted_steps = "\n".join(f"- {step}" for step in steps)
            result_text.insert(tk.END, formatted_steps)
        else:
            result_text.insert(tk.END, steps)
        result_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Career Plan Advisor")
app.geometry("500x400")

background_color = "#f0f0f0"
text_color = "#333333"
button_color = "#a6a6a6"

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=12)
app.option_add("*Font", default_font)
app.config(bg=background_color)

career_var = tk.StringVar(app)
career_var.set("Select a career")

career_menu = tk.OptionMenu(app, career_var, *["Software Engineer", "Graphic Designer", "Doctor", "Civil Engineer", "Financial Analyst",  "Teacher (K-12)"])
career_menu.config(width=20, font=default_font, bg=background_color, fg=text_color, borderwidth=2)
career_menu.pack(pady=20, padx=10, fill=tk.X)

show_button = tk.Button(app, text="Show Career Plan", command=show_plan, bg=button_color, fg="black", padx=10, pady=5) 
show_button.pack(pady=10, padx=10, fill=tk.X)

result_text = scrolledtext.ScrolledText(app, width=60, height=10, wrap=tk.WORD, state=tk.DISABLED, borderwidth=2, relief="sunken", bg="#d0d0d0", fg=text_color)
result_text.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

app.mainloop()


