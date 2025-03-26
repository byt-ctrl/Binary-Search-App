# WRITTEN BY OM [byt-ctrl]
# BINARY SEARCH APPLICATION

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

# The Most efficient way [Binary Search Algorithm]


# BINARY SEARCH ALGORITHM LOGIC
def binary_search(array,target) :

    
    
    """
    Performs binary search on a sorted array to find the target element.
    Returns the index of the target if found , else -1 ....

    """
    left,right=0 , len(array)-1
    while left <= right :
        mid=(left+right) // 2
        if array[mid] == target :
            return mid                                 # Returing Index of target
        
        elif array[mid] > target :
            right=mid-1                                # Target will be starting half side

        else :
            left=mid+1                                 # Target will be ending half side
    return -1           # If target not found return '-1' (That exit the fuctions and code blocks) (reduces clutter situations)




# Binary search for closest element
def closest_number_binary_search(array,target) :

    """
    It finds the closest element in the array
    returns the closest number that user inputted from array

    """

# BINARY SEARCH ALGORITHM LOGIC

    left,right = 0 , len(array) - 1
    closest = array[0]  # At first setting the first element as closest

    while left<=right:
        mid=(left+right) // 2
        if array[mid]==target :
            return array[mid]  # Getting that match
        
        if abs(array[mid] - target) < abs(closest - target) :     # Using abs (for returning absolute value)
            closest = array[mid]                                  # Update closest if a closer element is found
        if array[mid] > target :
            right = mid - 1                                        # Search starting half
        else :
            left = mid + 1                                        # Search ending half
    return closest                                                # Return the closest element




# Sorting The Inputted array by user

def sorting_the_array(array,order="Ascending") :

    """

    It sorts the array either in Ascending or Descending .

    """

    if order=="Ascending" :
        array.sort()  # Sort in Ascending order

    elif order=="Descending" :
        array.sort(reverse=True)  # Sort in Descending order

    return array




# Find the Kth smallest or largest element
def find_kth_element(array,k,order="smallest") :

    """
    This Block finds the smallest and largest Kth number 
    """

    if k<=0 or k>len(array) :
        return None  # if the index is invalid
    if order=="smallest" :
        return array[k-1]  # It returns Kth smallest element
    elif order=="largest" :
        return array[-k]  # It returns Kth largest element



# MAIN APPLICATION FOR BINARY SEARCH
class BinarySearchApp :
    def __init__(self,root) :

        """
        Initializes the Tkinter GUI application.
        """
        self.root=root
        self.root.title("Binary Search")
        self.root.geometry("900x900")  # For setting proper window size
        self.root.configure(bg="aliceblue")
        
        self.array=[]  # Empty List to store inputted array

        # Title 
        self.title_label=tk.Label(self.root,text="Binary Search Application", font=("Times",20,"bold"),bg="aliceblue",fg="midnightblue")  #GUI
        self.title_label.pack(pady=22)

        # array input
        self.array_label=tk.Label(self.root,text="Enter numbers (Separated By Spaces) :",font=("Times",14),bg="aliceblue",fg="midnightblue") #GUI
        self.array_label.pack()
        
        self.array_entry=tk.Entry(self.root,font=("Times",15),width=50,bg="white",fg="midnightblue") #GUI
        self.array_entry.pack(pady=11)

        # Sorting Order Option Dropdown Menu
        self.sort_order_label=tk.Label(self.root, text="Select Sort Order :",font=("Times",13),bg="aliceblue",fg="midnightblue")
        self.sort_order_label.pack()

        self.sort_order_types=tk.StringVar(value="Ascending")
        self.sort_order_menu=ttk.Combobox(self.root,textvariable=self.sort_order_types,values=["Ascending","Descending"],state="readonly",width=16) # GUI
        self.sort_order_menu.pack(pady=11) # GUI

        # Sorting Button
        self.sort_button=tk.Button(self.root,text="Sort Array",font=("Times",13),bg="forestgreen",fg="white",command=self.sort_input_array) #GUI
        self.sort_button.pack(pady=11)

        # Canvas Frame
        self.frame=tk.Frame(self.root)
        self.frame.pack(pady=11,fill=tk.X,padx=22) #GUI

        # Canvas and Scroll bar for array
        self.canvas=tk.Canvas(self.frame,bg="aliceblue",height=202)
        self.scrollbar=tk.Scrollbar(self.frame,orient="horizontal",command=self.canvas.xview) #GUI
        self.canvas.config(xscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="bottom",fill="x")
        self.canvas.pack(side="left",fill="both",expand=True)

        self.canvas.create_text(11,11,anchor="nw",text="Sorted Array : None",font=("Times",13))

        # Targeted Input
        self.target_label=tk.Label(self.root, text="Enter target to search :", font=("Times",13), bg="aliceblue",fg="midnightblue")
        self.target_label.pack()
        
        self.target_entry=tk.Entry(self.root, font=("Times",14),width=50,bg="white",fg="midnightblue")
        self.target_entry.pack(pady=10)

        # Horizontal frame for buttons
        self.button_frame=tk.Frame(self.root,bg="aliceblue")
        self.button_frame.pack(pady=10)

        # Search Element Button
        self.search_button=tk.Button(self.button_frame,text="Search Element",font=("Times",13),bg="royalblue",fg="white",command=self.search_element) # GUI
        self.search_button.grid(row=0, column=0, padx=10)

        # Closest Element Button
        self.closest_button=tk.Button(self.button_frame,text="Find Closest",font=("Times",13),bg="darkorange",fg="white",command=self.find_closest_element) #GUI
        self.closest_button.grid(row=0,column=1,padx=11)

        # Kth Smallest Element Button
        self.kth_smallest_button=tk.Button(self.button_frame,text="Kth Smallest Element",font=("Times",13),bg="purple",fg="white",command=self.find_kth_smallest) #GUI
        self.kth_smallest_button.grid(row=0,column=2,padx=11)

        # Kth Largest Element Button
        self.kth_largest_button=tk.Button(self.button_frame,text="Kth Largest Element",font=("Times",13),bg="orangered",fg="white",command=self.find_kth_largest)#GUI
        self.kth_largest_button.grid(row=0,column=3,padx=11)

        # Check Sorted Button
        self.check_sorted_button=tk.Button(self.button_frame,text="Check if Sorted",font=("Times",13),bg="yellow",fg="black",command=self.check_sorted)#GUI
        self.check_sorted_button.grid(row=0, column=4,padx=11)

        # Result Display Title
        self.result_title_label=tk.Label(self.root,text="Operation Result:",font=("Times",14,"bold"),bg="aliceblue",fg="midnightblue") #GUI
        self.result_title_label.pack(pady=11)

        # Result Display
        self.result_label=tk.Label(self.root,text=" Result will appear here ", font=("Times",14),bg="aliceblue",fg="midnightblue")
        self.result_label.pack(pady=11)

        # Clear Button
        self.clear_button=tk.Button(self.root,text="Clear",font=("Times",15),bg="firebrick",fg="white",command=self.clear_all)
        self.clear_button.pack(pady=9)






    def check_sorted(self) :

        """
        determines if the array is arranged in descending or ascending position.
        changes the result label according to the order of the array.

        """
        
        if self.array==sorted(self.array) :
            self.result_label.config(text="The Array is Sorted in Ascending order.")
        elif self.array==sorted(self.array,reverse=True) :
            self.result_label.config(text="The Array is Sorted in Descending order.")
        else:
            self.result_label.config(text="The Array is Not Sorted.")




    def sort_input_array(self) :

        """
        uses the user's input and chosen order to sort the array.
        shows the array that has been sorted and the sorting time.

        """
        try:
            input_data=self.array_entry.get()
            self.array=list(map(int,input_data.split())) # Create an integer list from the input.
            
            if len(self.array)>1000:
                messagebox.showwarning("Warning!!", "The array is very large , sorting may take time.")
            
            start_time=time.time()  # Set a sorting timer.
            self.array=sorting_the_array(self.array,self.sort_order_types.get())  # Sort the array
            end_time=time.time()  # Timer for the end


            # Use square brackets and commas to properly format the sorted array.
            sorted_text=f"[{', '.join(map(str,self.array[:20]))}]"  # Only display the top twenty items.

            # Empty the canvas's old contents and show the newly sorted array.
            self.canvas.delete("all")
            self.canvas.create_text(10,10,anchor="nw",text="Sorted Array :",font=("Times",15,"bold"))
            self.canvas.create_text(10,40,anchor="nw",text=sorted_text,font=("Times",13))

            # Show the sorting time
            self.result_label.config(text=f"Array sorted in {end_time - start_time:.6f} seconds.")

            # Modify the scroll area of the canvas
            self.canvas.config(scrollregion=self.canvas.bbox("all"))
        except ValueError :
            messagebox.showerror("Input Error","Please enter valid numbers separated by spaces.")




    def search_element(self) :

        """
        looks through the sorted array for the desired element.
        shows the outcome or, if it cannot be found, an error message.

        """
        if not self.array :
            messagebox.showerror("Error", "Array is empty . Please enter and sort an array first.")
            return
        try:
            target=int(self.target_entry.get())  # Get the element you want to search for.
            start_time=time.time()
            result=binary_search(self.array,target)         # Execute a binary search
            end_time=time.time()

            if result!=-1 :
                self.result_label.config(text=f"Element {target} found at index {result}.")
            else:
                self.result_label.config(text=f"Element {target} not found.")
            print(f"Search took {end_time-start_time:.6f} seconds.")  # Log search time
        except ValueError :
            messagebox.showerror("Input Error" , "Please enter a valid integer for the target.")




    def find_closest_element(self) :

        """
        locates and shows the element in the sorted array that is closest to the target.
        """

        try :
            target=int(self.target_entry.get())  # Get target
            closest=closest_number_binary_search(self.array,target)  # Find closest element
            self.result_label.config(text=f"The closest element to {target} is {closest} .")

        except ValueError  :
            messagebox.showerror("Input Error" , "Please enter a valid integer for the target.")




    def find_kth_smallest(self) :

        """
        locates and shows the array's Kth smallest element.
        """
        try:
            k=int(self.target_entry.get())  # Get k value

            if k<=0 or k>len(self.array) :
                messagebox.showerror("Input Error" , "Please enter a valid value for k.")
                return
            result=find_kth_element(self.array,k,"smallest")  # Locate the Kth smallest component
            if result is not None:
                self.result_label.config(text=f"The {k}th smallest element is {result}.")
            else:
                self.result_label.config(text="Invalid value for k.")
        except ValueError :
            messagebox.showerror("Input Error" , "Please enter a valid integer for k.")




    def find_kth_largest(self) :

        """
        locates and shows the array's Kth greatest element.
        """
        try:
            k=int(self.target_entry.get())  # Get k value
            if k<=0 or k>len(self.array) :
                messagebox.showerror("Input Error" , "Please enter a valid value for k.")
                return
            result=find_kth_element(self.array,k,"largest")  # Locate the Kth biggest element.

            if result is not None :
                self.result_label.config(text=f"The {k}th largest element is {result} .")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for k .")




    def clear_all(self) :

        """
        disables buttons, resets the array, and clears all input fields until a valid input is entered.
        """
        self.array=[]  # Reset array
        self.array_entry.delete(0,tk.END)  # Make input fields clear
        self.target_entry.delete(0,tk.END)
        self.result_label.config(text="Result will appear here")  # Reset the result label
        self.canvas.delete("all")  # Clear canvas content
        self.canvas.create_text(10,10,anchor="nw",text="Sorted Array: None",font=("Times",14))  # Reset canvas

        # Turn off buttons until the array is filled in.
        self.search_button.config(state="disabled")
        self.closest_button.config(state="disabled")
        self.kth_smallest_button.config(state="disabled")
        self.kth_largest_button.config(state="disabled")

# The application's main program
if __name__=="__main__" :

   # Launch the program after initializing the Tkinter root window.
    root=tk.Tk()
    app=BinarySearchApp(root)
    root.mainloop()

# END
