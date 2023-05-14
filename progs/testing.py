import tkinter as tk
import numpy as np
from tkinter import *
import openai
from PIL import ImageTk, Image
from tkinter import filedialog
import shutil
import json
import os
import subprocess
global selected_file_path
selected_file_path = ""
# define the people_frame variable in the global scope
people_frame = None
# Create main window
root = tk.Tk()
root.title("Model Selector")
root.geometry("500x300")

# Define colors
bg_color = "#0a043c"
btn_color = "#ff69b4"

# Define function to display selected model name
def display_model(model_name):
    # Clear any previous content from right frame
    for widget in right_frame.winfo_children():
        widget.destroy()
    
    # Display selected model name
    model_label = tk.Label(right_frame, text=model_name, font=("Arial", 18), bg=bg_color, fg="white")
    model_label.pack(pady=50)
    
    # Only show name entry and submit button if model name is "Model 1"
    
    if model_name == "Register Student":
        create_name_entry()
    elif model_name == "Train-Model":
        train_entry()
    elif model_name == "Take-Attandance":
        find_face()
    # Show chat interface if model name is "Model 5"
    if model_name == "Chat":
        create_chat_interface()    
    elif model_name == "Display":
        # Load data from people_seen.npy and file.json
        people_seen = np.load("savedata/people_seen.npy")
        with open("loaddate/file.json", "r") as f:
            file_data = json.load(f)

        # Create a dictionary of names and image paths from file_data
        names_to_paths = {}
        for path, name in file_data.items():
            names_to_paths[name] = path

        # Create a list of names and image paths that match in both people_seen and file_data
        matched_names = []
        matched_paths = []
        for name in people_seen:
            if name in names_to_paths:
                matched_names.append(name)
                matched_paths.append(names_to_paths[name])

        # Create a canvas widget and a scrollbar widget
        canvas = tk.Canvas(right_frame, bg=bg_color)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame to contain the images and names
        images_frame = tk.Frame(canvas, bg=bg_color)
        canvas.create_window((0, 0), window=images_frame, anchor="nw")

        # Display images and names of matched people
        if matched_names:
            for i, name in enumerate(matched_names):
                img_path = matched_paths[i]
                img = Image.open(img_path)
                img = img.resize((250, 250), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)

                name_label = tk.Label(images_frame, text=name, font=("Arial", 14), bg=bg_color, fg="white")
                name_label.pack(side="top", padx=10, pady=10)

                img_label = tk.Label(images_frame, image=img, bg=bg_color)
                img_label.image = img
                img_label.pack(side="top", padx=10, pady=10)

            # Center the images and names in the middle of the canvas
            images_frame.update_idletasks()
            canvas_width = canvas.winfo_width()
            images_frame_width = images_frame.winfo_width()
            canvas.create_window((canvas_width-images_frame_width)/2, 0, window=images_frame, anchor="nw")

        else:
            no_match_label = tk.Label(right_frame, text="No matches found.", font=("Arial", 14), bg=bg_color, fg="white")
            no_match_label.pack()

        # Create a "Clear Screen" button
        clear_button = tk.Button(right_frame, text="Clear Screen", font=("Arial", 14), bg=btn_color, fg="white", command=lambda: images_frame.destroy())
        clear_button.pack(side="top", pady=1,padx=20)

def create_chat_interface():
    # Set up OpenAI API key
    openai.api_key = "apen-api-key" # REPLACE WITH YOUR OWN API KEY
    
    # Define function to get response from OpenAI API
    def get_response():
        question = input_field.get()
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Q: {question}\nA:",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response_text = response.choices[0].text.strip()
        
        # Add user question and model response to chat history
        history_box.insert("end", f"User: {question}\nModel: {response_text}\n\n")
        history_box.see("end") # Scroll to the bottom of the text box
        
        # Clear input field
        input_field.delete(0, "end")
    
    # Create button to send question and get response
    send_btn = tk.Button(right_frame, text="Send", font=("Arial", 14), bg=btn_color, fg="white", command=get_response)
    send_btn.pack(side="left",pady=5)
    # Create labels for chat interface
    chat_label = tk.Label(right_frame, text="Ask a question:", font=("Arial", 14), bg=bg_color, fg="white")
    chat_label.pack(pady=10)
    
    # Create scrollable text box to display chat history
    history_box = tk.Text(right_frame, font=("Arial", 12), bg="#333", fg="white")
    history_box.pack(expand=True, fill="both")
    
    # Create input field for user to type question
    input_field = tk.Entry(right_frame, font=("Arial", 14), width=50)
    input_field.pack(pady=10)
    
    # Create button to send question and get response
    send_btn = tk.Button(right_frame, text="Send", font=("Arial", 14), bg=btn_color, fg="white", command=get_response)
    send_btn.pack(side="left",pady=5)
    
    # Focus input field on startup
    input_field.focus()


def find_face():
    def run_command2():
        command = "python final2.py"  # Replace with the command you want to run
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                output_text.insert(tk.END, output.decode())
        process.wait()             
    run_btn = tk.Button(right_frame, text="FIND-IT", font=("Arial", 14), bg=btn_color, fg="white", command=run_command2)
    run_btn.pack(pady=10) 
    output_text = tk.Text(right_frame, height=10, width=50)
    output_text.pack(padx=10, pady=10)  
def train_entry():            
    def run_command1():
        command = "python final1.py"  # Replace with the command you want to run
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                output_text.insert(tk.END, output.decode())
        process.wait()

    # Create button to submit name
    run_btn = tk.Button(right_frame, text="TRAIN-IT", font=("Arial", 14), bg=btn_color, fg="white", command=run_command1)
    run_btn.pack(pady=10) 
    output_text = tk.Text(right_frame, height=10, width=50)
    output_text.pack(padx=10, pady=10)  
def create_name_entry():
    # Create input field to enter name
    name_label = tk.Label(right_frame, text="Enter your name:", font=("Arial", 14), bg=bg_color, fg="white")
    name_label.pack(pady=8)
    
    name_entry = tk.Entry(right_frame, font=("Arial", 14))
    name_entry.pack(pady=15)

    def select_file():
        global selected_file_path
        # Open the file dialog and allow the user to select a file
        file_path = filedialog.askopenfilename()

        # If a file was selected, store the file path and enable the submit button
        if file_path:
            selected_file_path = file_path
            submit_button.config(state="normal")
            file_label.config(text=os.path.basename(selected_file_path))

    def submit_file():
        global selected_file_path   # declare selected_file_path as global
        # Get the name entered by the user
        name = name_entry.get()

        # Copy the selected file to the desired folder with the entered name as the new filename
        filename = os.path.basename(selected_file_path)
        new_filepath = f"C:/Users/Stephne/Desktop/progs/images/{name}.jpg"
        shutil.copy(selected_file_path, new_filepath)

        # Add the name to a JSON file with the filename as the key
        data = {}
        with open("C:/Users/Stephne/Desktop/progs/loaddate/file.json", "r") as f:
            data = json.load(f)
        data["images/"+name+".jpg"] = name
        with open("C:/Users/Stephne/Desktop/progs/loaddate/file.json", "w") as f:
            json.dump(data, f)

        # Reset the GUI
        name_entry.delete(0, tk.END)
        submit_button.config(state="disabled")
        selected_file_path = ""

    # Create a button that opens the file dialog
    upload_button = tk.Button(right_frame, text="Upload Photo",font=("Arial", 14), bg=btn_color, fg="white", command=select_file, padx=10, pady=5)
    upload_button.pack(pady=9)

    file_label = tk.Label(right_frame, text="", font=("Arial", 14), bg=bg_color, fg="white")
    file_label.pack(pady=9)

    # Create a button that submits the selected file and the entered name
    submit_button = tk.Button(right_frame, text="Submit",font=("Arial", 14), bg=btn_color, fg="white", command=submit_file, state="disabled")
    submit_button.pack(pady=22)

# Create left frame to display model options
left_frame = tk.Frame(root, bg=bg_color)
left_frame.pack(side="left", fill="y")

heading_label = tk.Label(left_frame, text="Class Guardian", font=("Arial", 18), bg=bg_color, fg="white")
heading_label.pack(pady=20)

model_names = ["Register Student", "Train-Model", "Take-Attandance", "Display", "Chat"]
fixed_width = len("Take-Attendance")
for name in model_names:
    model_btn = tk.Button(left_frame, text=name, font=("Arial", 14), bg=btn_color, fg="white",width=fixed_width, command=lambda name=name: display_model(name))
    model_btn.pack(pady=10)

# Create right frame to display selected model and name entry
right_frame = tk.Frame(root, bg=bg_color)
right_frame.pack(side="right", fill="both", expand=True)

# Run the main loop
root.mainloop()
