import tkinter as tk
from bs4 import BeautifulSoup
import requests

# Function to gather information from a given URL
def gather_information(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Find all 'a' tags with 'href' attribute
        links = soup.find_all('a', href=True)
        
        # Extract the URLs and return them
        return '\\n'.join([link['href'] for link in links])
    except Exception as e:
        return f"An error occurred: {e}"

# Function to handle the submit button click
def on_submit():
    url = entry.get()
    results = gather_information(url)
    result_container.delete('1.0', tk.END)  # Clear the previous results
    result_container.insert(tk.END, results)

# Set up the main application window
root = tk.Tk()
root.title("Information Gathering Bot")

# Create the input field
entry_label = tk.Label(root, text="Enter URL:")
entry_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Create the submit button
submit_button = tk.Button(root, text="Gather Information", command=on_submit)
submit_button.pack()

# Create the container to display results
result_container = tk.Text(root, height=15, width=80)
result_container.pack()

# Run the application
root.mainloop()
