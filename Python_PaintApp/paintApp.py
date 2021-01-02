from tkinter import *
import tkinter.font

# Class Definition

class PaintApp:

	# Class Variables
	drawing_tool = "pencil"
	left_but = "up"
	x_pos, y_pos = None, None
	x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

	@staticmethod
	def changeToPencil(self):
		if self.drawing_tool == "pencil":
			return
		self.drawing_tool = "pencil"
	def changeToLine(self):
		if self.drawing_tool == "line":
			return
		self.drawing_tool = "line"
	def changeToArc(self):
		if self.drawing_tool == "arc":
			return
		self.drawing_tool = "arc"
	def changeToOval(self):
		if self.drawing_tool == "oval":
			return
		self.drawing_tool = "oval"
	def changeToRectangle(self):
		if self.drawing_tool == "rectangle":
			return
		self.drawing_tool = "rectangle"
	def changeToText(self):
		if self.drawing_tool == "text":
			return
		self.drawing_tool = "text"

	# Catch Mouse Down
	def left_but_down(self, event=None):
		self.left_but = "down"

		self.x1_line_pt = event.x
		self.y1_line_pt = event.y

	# Catch Mouse Up
	def left_but_up(self, event=None):
		self.left_but = "up"

		self.x_pos = None
		self.y_pos = None

		self.x2_line_pt = event.x
		self.y2_line_pt = event.y

		if self.drawing_tool == "line":
			self.line_draw(event)

	# Catch Mouse Move
	def motion(self, event=None):
		if self.drawing_tool == "pencil":
			self.pencil_draw(event)
		elif self.drawing_tool == "arc":
			self.arc_draw(event)
		elif self.drawing_tool == "oval":
			self.oval_draw(event)
		elif self.drawing_tool == "rectangle":
			self.rectangle_draw(event)
		elif self.drawing_tool == "text":
			self.text_draw(event)
			
	# Draw with Pencil
	def pencil_draw(self, event=None):
		if self.left_but == "down":
			if self.x_pos is not None and self.y_pos is not None:
				event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE)
			self.x_pos = event.x
			self.y_pos = event.y

	# Draw Line
	def line_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
			event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill="green")

	# Draw Arc
	def arc_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
			coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
			event.widget.create_arc(coords, start=0, extent=150, style=ARC)


	# Draw 	Oval
	def oval_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
			coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
			event.widget.create_oval(coords, fill="midnight blue", outline="yellow", width=2)

	# Draw Rectagle
	def rectangle_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
			coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
			event.widget.create_rectangle(coords, fill="midnight blue", outline="yellow", width=2)

	# Draw Text
	def text_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt):
			text_font = tkinter.font.Font(family="Helvetica", size=20, weight='bold', slant='italic')
			coords = self.x1_line_pt, self.y1_line_pt
			event.widget.create_text(coords, fill="green", font=text_font, text="WOW")

	# Initialize
	def __init__(self, root):

		menubar = Menu(root)

		toolbar = Menu(root, tearoff=0)		
		toolbar.add_command(label="Pencil", command=self.changeToPencil)
		toolbar.add_command(label="Line", command=self.changeToLine)
		toolbar.add_command(label="Arc", command=self.changeToArc)
		toolbar.add_command(label="Oval", command=self.changeToOval)
		toolbar.add_command(label="Rectangle", command=self.changeToRectangle)
		toolbar.add_command(label="Text", command=self.changeToText)

		menubar.add_cascade(label="Drawing Options", menu=toolbar)

		root.config(menu=menubar)

		drawing_area = Canvas(root)
		drawing_area.pack()

		drawing_area.bind("<Motion>", self.motion)
		drawing_area.bind("<ButtonPress-1>", self.left_but_down)
		drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

root = Tk()
root.title("Paint App")

paint_app = PaintApp(root)

root.mainloop()