import tkinter as tk

def get_dpi():
    root = tk.Tk()
    
    # Get DPI Awareness (Windows only, may require Python 3.10+)
    try:
        dpiawareness = root.tk.call('tk', 'scaling', '-displayof', '.', '-dpiawareness')
        if dpiawareness == 'none':
            root.tk.call('tk', 'scaling', '-displayof', '.', '-dpiawareness', 'system')
    except tk.TclError:
        pass
    
    # Get actual DPI
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Get screen dimensions in inches
    screen_width_inch = root.winfo_screenmmwidth() / 25.4  # mm to inches
    screen_height_inch = root.winfo_screenmmheight() / 25.4  # mm to inches
    
    # Calculate DPI
    dpi_x = screen_width / screen_width_inch
    dpi_y = screen_height / screen_height_inch
    
    root.destroy()
    
    return dpi_x, dpi_y

if __name__ == "__main__":
    dpi_x, dpi_y = get_dpi()
    print(f"DPI (X): {dpi_x}")
    print(f"DPI (Y): {dpi_y}")
