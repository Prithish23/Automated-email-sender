import smtplib
from tkinter import *
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time
import threading

def send_email():
    try:
        sender_email = sender_entry.get()
        receiver_email = receiver_entry.get()
        password = password_entry.get()
        subject = subject_entry.get()
        body = body_entry.get("1.0", END)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

def schedule_email():
    scheduled_time = schedule_entry.get()
    current_time = datetime.now().strftime("%H:%M")
    
    while current_time != scheduled_time:
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(1)
    
    send_email()

def start_schedule_thread():
    threading.Thread(target=schedule_email).start()

# GUI setup
root = Tk()
root.title("Automated Email Sender")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# GUI Elements
Label(root, text="Automated Email Sender", font=("Arial", 20), bg="#282c34", fg="#61dafb").pack(pady=10)

Label(root, text="Sender Email:", bg="#f0f0f0").pack(pady=5)
sender_entry = Entry(root, width=50, bg="#ffffff", fg="#000000")
sender_entry.pack(pady=5)

Label(root, text="Receiver Email:", bg="#f0f0f0").pack(pady=5)
receiver_entry = Entry(root, width=50, bg="#ffffff", fg="#000000")
receiver_entry.pack(pady=5)

Label(root, text="Password:", bg="#f0f0f0").pack(pady=5)
password_entry = Entry(root, show="*", width=50, bg="#ffffff", fg="#000000")
password_entry.pack(pady=5)

Label(root, text="Subject:", bg="#f0f0f0").pack(pady=5)
subject_entry = Entry(root, width=50, bg="#ffffff", fg="#000000")
subject_entry.pack(pady=5)

Label(root, text="Body:", bg="#f0f0f0").pack(pady=5)
body_entry = Text(root, height=10, width=50, bg="#ffffff", fg="#000000")
body_entry.pack(pady=5)

Label(root, text="Schedule Time (HH:MM):", bg="#f0f0f0").pack(pady=5)
schedule_entry = Entry(root, width=50, bg="#ffffff", fg="#000000")
schedule_entry.pack(pady=5)

# Buttons with color
send_button = Button(root, text="Send Now", command=send_email, bg="#61dafb", fg="#ffffff", font=("Arial", 12))
send_button.pack(pady=10)

schedule_button = Button(root, text="Schedule Email", command=start_schedule_thread, bg="#61dafb", fg="#ffffff", font=("Arial", 12))
schedule_button.pack(pady=10)

root.mainloop()
