import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Analog Clock")

        # create the canvas widget
        self.canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.canvas.pack()

        # draw the clock face and hands
        self.draw_clock_face()
        self.draw_hands()

        # update the clock every second
        self.update_clock()

    def draw_clock_face(self):
        # draw the clock face
        self.canvas.create_oval(50, 50, 250, 250, width=5)

        # draw the hour markers
        for i in range(12):
            x1 = 150 + 100 * math.sin(math.radians(i * 30))
            y1 = 150 - 100 * math.cos(math.radians(i * 30))
            x2 = 150 + 90 * math.sin(math.radians(i * 30))
            y2 = 150 - 90 * math.cos(math.radians(i * 30))
            self.canvas.create_line(x1, y1, x2, y2, width=3)

            # add the hour numbers
            x3 = 150 + 120 * math.sin(math.radians(i * 30))
            y3 = 150 - 120 * math.cos(math.radians(i * 30))
            self.canvas.create_text(x3, y3, text=str(i+1), font=("Arial", 12))

    def draw_hands(self):
        # draw the hour hand
        self.hour_hand = self.canvas.create_line(150, 150, 150, 100, width=5)

        # draw the minute hand
        self.minute_hand = self.canvas.create_line(150, 150, 150, 80, width=3)

        # draw the second hand
        self.second_hand = self.canvas.create_line(150, 150, 150, 70, width=2, fill="red")

    def update_clock(self):
        # get the current time
        current_time = time.localtime()

        # calculate the angles of the hands
        hour_angle = (current_time.tm_hour % 12) * 30 + current_time.tm_min / 2
        minute_angle = current_time.tm_min * 6
        second_angle = current_time.tm_sec * 6

        # rotate the hands on the canvas
        self.canvas.coords(self.hour_hand, 150, 150, 150 + 60 * math.sin(math.radians(hour_angle)), 150 - 60 * math.cos(math.radians(hour_angle)))
        self.canvas.coords(self.minute_hand, 150, 150, 150 + 80 * math.sin(math.radians(minute_angle)), 150 - 80 * math.cos(math.radians(minute_angle)))
        self.canvas.coords(self.second_hand, 150, 150, 150 + 90 * math.sin(math.radians(second_angle)), 150 - 90 * math.cos(math.radians(second_angle)))

        # update the clock every second
        self.master.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalogClock(root)
    root.mainloop()