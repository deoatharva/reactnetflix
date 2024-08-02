import tkinter as tk
from tkinter import messagebox

GOAL = 4  # The exact amount of water to have in a bucket to win.
steps = 0  # Keep track of how many steps the player made to solve this.
waterInBucket = {'8': 0, '5': 0, '3': 0}  # The amount of water in each bucket.

def update_display():
    # Update the display of buckets in the GUI
    canvas.delete("all")  # Clear previous display

    x_offset = 50
    y_offset = 30
    spacing = 50
    bucket_size = {'8': 8, '5': 5, '3': 3}

    for key, value in waterInBucket.items():
        canvas.create_text(x_offset, y_offset - 20, text=key + "L", anchor=tk.W)
        for i in range(bucket_size[key]):
            if value > i:
                canvas.create_rectangle(x_offset - 15, y_offset + (bucket_size[key] - i - 1) * 30,
                                        x_offset + 15, y_offset + (bucket_size[key] - i) * 30, fill="blue")
            else:
                canvas.create_rectangle(x_offset - 15, y_offset + (bucket_size[key] - i - 1) * 30,
                                        x_offset + 15, y_offset + (bucket_size[key] - i) * 30, fill="white")
        x_offset += spacing

    canvas.pack()

def fill_bucket(bucket):
    waterInBucket[bucket] = int(bucket)
    update_display()

def empty_bucket(bucket):
    waterInBucket[bucket] = 0
    update_display()

def pour(src_bucket, dst_bucket):
    src_size = int(src_bucket)
    dst_size = int(dst_bucket)

    space_in_dst = dst_size - waterInBucket[dst_bucket]
    water_to_pour = min(space_in_dst, waterInBucket[src_bucket])

    waterInBucket[src_bucket] -= water_to_pour
    waterInBucket[dst_bucket] += water_to_pour

    update_display()

def pour_selected(selected_bucket):
    global steps
    src_bucket = top.get()
    
    if src_bucket != selected_bucket:  # Ensure different source and destination buckets
        pour(src_bucket, selected_bucket)
        steps += 1
        check_win()

def check_win():
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            messagebox.showinfo("Congratulations!", f"You solved it in {steps} steps!")
            root.destroy()
            break

def make_move(action, top_var):
    global steps
    bucket = top_var.get()  # Get the actual string value from StringVar
    if action == 'F':
        fill_bucket(bucket)
    elif action == 'E':
        empty_bucket(bucket)
    elif action == 'P':
        show_pour_dropdown()

    steps += 1
    check_win()

def show_pour_dropdown():
    # Create a Toplevel window to show the Pour options
    pour_window = tk.Toplevel(root)
    pour_window.title("Select Pour Destination")

    # Dropdown to select where to pour
    selected_bucket_var = tk.StringVar(pour_window, '8')  # Default value

    def pour_action(selected_bucket):
        pour_selected(selected_bucket)
        pour_window.destroy()  # Close the dropdown window

    pour_dropdown = tk.OptionMenu(pour_window, selected_bucket_var, '8', '5', '3', command=pour_action)
    pour_dropdown.pack(padx=20, pady=20)

    pour_window.grab_set()  # Make the pour window modal
    root.wait_window(pour_window)  # Wait for pour window to close before continuing

root = tk.Tk()
root.title("Water Bucket Puzzle")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

# Buttons for actions
fill_button = tk.Button(root, text="Fill", command=lambda: make_move('F', top))
fill_button.pack(side=tk.LEFT, padx=10)

empty_button = tk.Button(root, text="Empty", command=lambda: make_move('E', top))
empty_button.pack(side=tk.LEFT, padx=10)

pour_button = tk.Button(root, text="Pour", command=lambda: make_move('P', top))
pour_button.pack(side=tk.LEFT, padx=10)

# Dropdown menu to select the source bucket for pouring
top = tk.StringVar(root)
top.set('8')  # Default value

dropdown = tk.OptionMenu(root, top, '8', '5', '3')
dropdown.pack(side=tk.LEFT, padx=10)

update_display()

root.mainloop()
