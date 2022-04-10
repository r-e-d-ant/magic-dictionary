
from tkinter import *
from tkinter import messagebox
from PyDictionary import PyDictionary

# init
root = Tk()

# general settings
root.title("Magic - Dictionary")
root.iconbitmap("book-2.ico")
root.geometry("570x500")

# --====================-- functions --=====================--

def lookup():
	# inform that the search box is empty if it this on lookup
	if (len(my_entry.get()) <= 0):
		messagebox.showwarning('Warning', 'The search box is empty')

	# otherwise if not empty
	else:
		# Clear the Text box
		my_text.delete(1.0, END)

		# Look up word
		dictionary = PyDictionary()
		definition = dictionary.meaning(my_entry.get())

		try:
			for key, value in definition.items():
				# Put the key header in textbox
				my_text.insert(END, key + "\n\n")

				for values in value:
					my_text.insert(END, f"- { values }\n\n")
		# if the word not available in dictionary
		except AttributeError:
			messagebox.showerror("Error", f" { my_entry.get() } - Word not found")


# =============================================================

# label frame
my_labelFrame = LabelFrame(root, text="Enter a Word")
my_labelFrame.pack(pady=20)

# word entry box
my_entry = Entry(my_labelFrame, font=('Helvetica', 18))
my_entry.grid(row=0, column=0, padx=10, pady=10)

# search button
my_button = Button(my_labelFrame, text="Lookup", fg='white', bg='green', command=lookup)
my_button.grid(row=0, column=1, padx=10)

# Text box to show the searched word meanings
my_text = Text(root, height=20, width=65, wrap=WORD, relief=GROOVE, borderwidth=2)
my_text.pack(pady=10)


root.mainloop()