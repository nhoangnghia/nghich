import tkinter as tk

def convert():
    try:
        number = int(entry_number.get())
        base_from = int(entry_base_from.get())
        base_to = int(entry_base_to.get())
        
        if base_from == 10:
            result = str(bin(number))[2:] if base_to == 2 else \
                     str(oct(number))[2:] if base_to == 8 else \
                     str(hex(number))[2:] if base_to == 16 else number
        else:
            result = int(str(number), base_from)
            result = bin(result)[2:] if base_to == 2 else \
                     oct(result)[2:] if base_to == 8 else \
                     hex(result)[2:] if base_to == 16 else result
        
        label_result.config(text=f"Kết quả: {result}")
    except ValueError:
        label_result.config(text="Vui lòng nhập số nguyên hợp lệ!")

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Chuyển đổi hệ cơ số")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_number = tk.Label(frame, text="Nhập số:")
label_number.grid(row=0, column=0)

entry_number = tk.Entry(frame)
entry_number.grid(row=0, column=1)

label_base_from = tk.Label(frame, text="Hệ cơ số đang có:")
label_base_from.grid(row=1, column=0)

entry_base_from = tk.Entry(frame)
entry_base_from.grid(row=1, column=1)

label_base_to = tk.Label(frame, text="Hệ cơ số muốn chuyển đổi:")
label_base_to.grid(row=2, column=0)

entry_base_to = tk.Entry(frame)
entry_base_to.grid(row=2, column=1)

button_convert = tk.Button(frame, text="Chuyển đổi", command=convert)
button_convert.grid(row=3, columnspan=2)

label_result = tk.Label(frame, text="")
label_result.grid(row=4, columnspan=2)

root.mainloop()
