import tkinter as tk
from bs4 import BeautifulSoup
import requests
from tkinter import ttk

# Function to gather information from a given URL
def gather_information(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get HTTP headers
        headers = response.headers
        
        # Get HTML content
        html_content = soup.prettify()
        
        # Find all 'a' tags with 'href' attribute
        links = soup.find_all('a', href=True)
        
        # Extract the URLs
        urls = [link['href'] for link in links]
        
        return headers, html_content, urls
    except Exception as e:
        return f"An error occurred: {e}", '', []

# Function to handle the submit button click
def on_submit():
    url = entry.get()
    headers, html_content, urls = gather_information(url)
    
    # Clear the previous results
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    # Display HTTP headers
    headers_label = tk.Label(result_frame, text="HTTP Headers:", font=('bold', 14))
    headers_label.pack()
    headers_text = tk.Text(result_frame, height=5, width=80)
    headers_text.insert(tk.END, str(headers))
    headers_text.pack()
    
    # Display HTML content
    html_label = tk.Label(result_frame, text="HTML Content (truncated):", font=('bold', 14))
    html_label.pack()
    html_text = tk.Text(result_frame, height=5, width=80)
    html_text.insert(tk.END, html_content[:1000] + '...')  # Truncate for display purposes
    html_text.pack()
    
    # Display URLs in a table
    urls_label = tk.Label(result_frame, text="URLs Found:", font=('bold', 14))
    urls_label.pack()
    urls_table = ttk.Treeview(result_frame, columns=('URLs'), show='headings')
    urls_table.heading('URLs', text='URLs')
    urls_table.column('URLs', width=500, anchor='w')
    
    for url in urls:
        urls_table.insert('', tk.END, values=(url,))
    
    urls_table.pack()

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

# Create a frame to display results
result_frame = tk.Frame(root)
result_frame.pack(fill='both', expand=True)

# Run the application
root.mainloop()
