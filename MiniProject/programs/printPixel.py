import tkinter as tk
import coordsData
import numpy as np

def draw_coordinates(canvas, coordinates, sx=1, sy=1):

    coordinates = coordinates*np.array([sx,sy])
    for (x, y) in coordinates:
        canvas.create_line(x-1, y, x, y, fill='black')

def main(coordinates):

    root = tk.Tk()
    root.title("Black Pixel Coordinates")

    canvas = tk.Canvas(root, width=500, height=500, bg='white')
    canvas.pack()
    draw_coordinates(canvas, coordinates,0.33,0.33)
    root.mainloop()

image_path = "C:\\Users\\piyus\\OneDrive\\Desktop\\MiniProject\\database\\alphabets_config\\alphabets.jpg" 

coordinates = coordsData.getData(image_path)

main(coordinates[25])
