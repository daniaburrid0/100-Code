from tkinter import *

def main():
    
    
    # Create the main window
    root = Tk()
    root.title("Miles to Kilometers")

    # Create the main frame
    mainframe = Frame(root, height=400, width=400)
    mainframe.pack_propagate(0)
    mainframe.pack(padx=10, pady=10)

    # Fn to convert miles to kilometers
    fn_convert = lambda: kilo_display.config(text=str(float(miles_entry.get()) * 1.60934))
    
    # Create the widgets
    miles_label = Label(mainframe, text="Miles:")
    miles_entry = Entry(mainframe, width=10)
    convert_button = Button(mainframe, text="Convert", command=fn_convert)
    kilo_label = Label(mainframe, text="Kilometers:")
    kilo_display = Label(mainframe, text="0.0")

    # Lay out the widgets
    miles_label.grid(row=0, column=0, sticky=W)
    miles_entry.grid(row=0, column=1, sticky=E)
    convert_button.grid(row=1, column=0, columnspan=2)
    kilo_label.grid(row=2, column=0, sticky=W)
    kilo_display.grid(row=2, column=1, sticky=E)

    # Start the event loop
    root.mainloop()

if __name__ == '__main__':
    main()