# -*- coding: cp1252 -*-
from time import sleep
import serial
import os
import gi
from gi.repository import GObject as gobject
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class window():
	def __init__(self):
		self.build = Gtk.Builder()
		self.build.add_from_file("ard.glade")
		self.build.connect_signals(self)
		self.win = self.build.get_object("window1")
		self.win.connect("key-press-event", self.a, None)
		self.win.show()
	def a(self,widget,event,jk):
		ser = serial.Serial('/dev/ttyACM0', 9600*2) # Establish the connection on a
		print "hi"
		while True:
			 
			arr =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			for l in range(0, 14):
				i=  ser.readline().split(',') # Read the newest output from the Arduin
				
				if i[0] == "S":
					op = ser.readline()
					arr[int(i[1].split("\\")[0])] = int(op.split("\\")[0])
					sleep(.05) # Delay for one tenth of a second
			
			for i in range(0,14):
				if arr[i] == 1:
					im = self.build.get_object("image"+str(i+1))
					im.set_from_file("s1.jpeg")
					
				else:
					im = self.build.get_object("image"+str(i+1))
					im.set_from_file("s2.jpeg")
					
			self.win.show()
			while Gtk.events_pending():
				Gtk.main_iteration_do(True)
			
if __name__ == "__main__":
	main = window()
	Gtk.main()






