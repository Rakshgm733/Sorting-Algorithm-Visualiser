import tkinter as tk
from tkinter import ttk
import random
from algorithms import bubble_sort, merge_sort, quick_sort

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.config(bg="white")

        self.array = []
        self.speed = 0.1
        self.metrics = {"comparisons": 0, "swaps": 0}

        self.ui_frame = tk.Frame(self.root, width=600, height=200, bg="lightgray")
        self.ui_frame.grid(row=0, column=0, padx=10, pady=5)

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.grid(row=1, column=0, padx=10, pady=5)

        self.algorithms = {
            "Bubble Sort": bubble_sort,
            "Merge Sort": merge_sort,
            "Quick Sort": quick_sort,
        }

        self.selected_algorithm = tk.StringVar()
        self.speed_scale = tk.DoubleVar(value=0.1)

        self.create_ui()

    def create_ui(self):
        tk.Label(self.ui_frame, text="Algorithm", bg="lightgray").grid(row=0, column=0, padx=5, pady=5)
        algo_menu = ttk.Combobox(self.ui_frame, textvariable=self.selected_algorithm, values=list(self.algorithms.keys()))
        algo_menu.grid(row=0, column=1, padx=5, pady=5)
        algo_menu.current(0)

        tk.Label(self.ui_frame, text="Speed", bg="lightgray").grid(row=1, column=0, padx=5, pady=5)
        tk.Scale(self.ui_frame, from_=0.01, to=1.0, resolution=0.01, orient=tk.HORIZONTAL,
                 variable=self.speed_scale).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.ui_frame, text="Generate Array", command=self.generate_array).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(self.ui_frame, text="Start", command=self.start_sorting).grid(row=1, column=2, padx=5, pady=5)

        self.metrics_label = tk.Label(self.ui_frame, text="Comparisons: 0  Swaps: 0", bg="lightgray")
        self.metrics_label.grid(row=2, column=0, columnspan=3)

    def generate_array(self):
        self.array = [random.randint(10, 390) for _ in range(50)]
        self.metrics = {"comparisons": 0, "swaps": 0}
        self.draw_array()

    def draw_array(self, array=None, color_indices=[]):
        array = array or self.array
        self.canvas.delete("all")
        c_height = 400
        c_width = 600
        bar_width = c_width / len(array)
        for i, val in enumerate(array):
            x0 = i * bar_width
            y0 = c_height - val
            x1 = (i + 1) * bar_width
            y1 = c_height
            color = "red" if i in color_indices else "skyblue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.metrics_label.config(text=f"Comparisons: {self.metrics['comparisons']}  Swaps: {self.metrics['swaps']}")
        self.root.update_idletasks()

    def start_sorting(self):
        algo_name = self.selected_algorithm.get()
        algo = self.algorithms[algo_name]
        self.metrics = {"comparisons": 0, "swaps": 0}
        algo(self.array, self.draw_array, self.speed_scale.get(), self.metrics)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
