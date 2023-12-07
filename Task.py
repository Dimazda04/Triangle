import tkinter as tk

def clear():
    lbl_ans.configure(text="")
    lbl_err.configure(text="")
    e_1.delete(0, "end")
    e_2.delete(0, "end")
    e_3.delete(0, "end")
def but():
    lbl_err.configure(text="")
    lbl_ans.configure(text="")
    try:
        a = int(e_1.get())
        b = int(e_2.get())
        c = int(e_3.get())
    except ValueError:
        lbl_err.configure(text="Неверные данные")
    else:
        if a > 0 and b > 0 and c > 0:
            if a == b == c:
                if a != 0:
                    lbl_ans.configure(text="Треугольник равносторонний")
            elif a == b and a != c:
                if a + b > c:
                    lbl_ans.configure(text="Треугольник равнобедренный")
                else:
                    lbl_err.configure(text="Треугольник не существует")
            elif a == c and a != b:
                if a + c > b:
                    lbl_ans.configure(text="Треугольник равнобедренный")
                else:
                    lbl_err.configure(text="Треугольник не существует")
            elif c == b and c != a:
                if c + b > a:
                    lbl_ans.configure(text="Треугольник равнобедренный")
                else:
                    lbl_err.configure(text="Треугольник не существует")
            elif a + b > c and a + c > b and b + c > a:
                lbl_ans.configure(text="Треугольник разносторонний")
            else:
                lbl_err.configure(text="Треугольник не существует")
        else:
            lbl_err.configure(text="Неверные данные")


root = tk.Tk()
root.title("Треугольник")
root.geometry("475x300")

lbl_1 = tk.Label(root, text="Первое число", padx=60, pady=10)
lbl_1.grid(column=0, row=0)
lbl_2 = tk.Label(root, text="Второе число", padx=60, pady=10)
lbl_2.grid(column=0, row=1)
lbl_3 = tk.Label(root, text="Третье число", padx=60, pady=10)
lbl_3.grid(column=0, row=2)
lbl_ans = tk.Label(root)
lbl_ans.grid(column=1, row=4)
lbl_err = tk.Label(root)
lbl_err.grid(column=1, row=5)

e_1 = tk.Entry(root)
e_1.grid(column=1, row=0)
e_2 = tk.Entry(root)
e_2.grid(column=1, row=1)
e_3 = tk.Entry(root)
e_3.grid(column=1, row=2)

btn = tk.Button(root, text="Рассчитать", command=but, padx=60, pady=10)
btn_clr = tk.Button(root, text="Очистить", command=clear, padx=60, pady=10)
btn.grid(column=0, row=4)
btn_clr.grid(column=0, row=5)

root.mainloop()

