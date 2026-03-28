# UI Utilities and Custom Widgets

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from config import ScreenConfig, Colors, Fonts

class ResponsiveFrame(tk.Frame):
    """Frame that scales with window size"""
    
    def __init__(self, parent, bg=Colors.SECTION_BG, **kwargs):
        super().__init__(parent, bg=bg, **kwargs)
        self.parent = parent
        self.after(100, self._configure_grid)
    
    def _configure_grid(self):
        """Configure grid weights for responsiveness"""
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

class ResponsiveLabel(tk.Label):
    """Label that adjusts font size based on screen"""
    
    def __init__(self, parent, text="", font_size=11, font_style="normal", **kwargs):
        font_name = kwargs.pop('font_name', 'Segoe UI')
        
        font_weight = "bold" if font_style == "bold" else "normal"
        font_obj = tkFont.Font(family=font_name, size=font_size, weight=font_weight)
        
        super().__init__(parent, text=text, font=font_obj, **kwargs)

class ResponsiveEntry(tk.Entry):
    """Entry field with responsive styling"""
    
    def __init__(self, parent, font_size=11, **kwargs):
        font_obj = tkFont.Font(family='Segoe UI', size=font_size)
        super().__init__(parent, font=font_obj, **kwargs)
        self.config(
            relief=tk.FLAT,
            bd=2,
            insertwidth=2,
            selectforeground='white',
            selectbackground=Colors.PRIMARY_BLUE
        )

class ResponsiveButton(tk.Button):
    """Button with hover effects and responsive styling"""
    
    def __init__(self, parent, text="", font_size=11, on_click=None, **kwargs):
        font_obj = tkFont.Font(family='Segoe UI', size=font_size, weight='bold')
        
        bg_color = kwargs.pop('bg_color', Colors.BUTTON_BG)
        
        super().__init__(
            parent,
            text=text,
            font=font_obj,
            bg=bg_color,
            fg='white',
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            **kwargs
        )
        
        self.default_bg = bg_color
        self.hover_bg = Colors.BUTTON_HOVER
        
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        
        if on_click:
            self.config(command=on_click)
    
    def _on_enter(self, event):
        self.config(bg=self.hover_bg)
    
    def _on_leave(self, event):
        self.config(bg=self.default_bg)

class StyledCombobox(ttk.Combobox):
    """Styled combobox with consistent look"""
    
    def __init__(self, parent, font_size=11, **kwargs):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox', font=('Segoe UI', font_size))
        
        super().__init__(parent, font=('Segoe UI', font_size), **kwargs)
        self.config(state='readonly')

class SectionFrame(tk.LabelFrame):
    """Section frame with styled header"""
    
    def __init__(self, parent, text="", **kwargs):
        super().__init__(
            parent,
            text=text,
            font=Fonts.HEADING,
            bg=Colors.SECTION_BG,
            fg=Colors.LABEL_TEXT,
            relief=tk.RIDGE,
            borderwidth=2,
            padx=15,
            pady=15,
            **kwargs
        )

class InputField:
    """Wrapper for creating labeled input fields"""
    
    def __init__(self, parent, label_text, row, column, width=30, 
                 font_size=10, is_password=False, is_combobox=False, 
                 combobox_values=None):
        
        # Label
        label = ResponsiveLabel(
            parent,
            text=label_text,
            font_size=font_size,
            font_style="bold",
            bg=Colors.SECTION_BG,
            fg=Colors.LABEL_TEXT
        )
        label.grid(row=row, column=column, padx=10, pady=8, sticky='w')
        
        # Input field
        if is_combobox:
            self.field = StyledCombobox(
                parent,
                font_size=font_size,
                values=combobox_values or [],
                width=width - 2
            )
        else:
            self.field = ResponsiveEntry(
                parent,
                font_size=font_size,
                width=width,
                show="*" if is_password else ""
            )
        
        self.field.grid(row=row, column=column + 1, padx=10, pady=8, sticky='w')
    
    def get(self):
        return self.field.get()
    
    def set(self, value):
        if isinstance(self.field, StyledCombobox):
            self.field.set(value)
        else:
            self.field.delete(0, tk.END)
            self.field.insert(0, value)
    
    def clear(self):
        self.field.delete(0, tk.END)

class ScreenAdaptiveWindow:
    """Mixin class for screen-adaptive windows"""
    
    @staticmethod
    def get_window_geometry(root, default_width=1350, default_height=700):
        """Get responsive window geometry"""
        screen_config = ScreenConfig.get_screen_dimensions(root)
        
        # Scale window to 90% of screen for modern appearance
        width = int(screen_config['width'] * 0.9)
        height = int(screen_config['height'] * 0.9)
        
        # Ensure minimum size
        width = max(width, default_width)
        height = max(height, default_height)
        
        # Center window
        x = (screen_config['width'] - width) // 2
        y = (screen_config['height'] - height) // 2
        
        return width, height, x, y
    
    @staticmethod
    def center_window(root, width, height):
        """Center window on screen"""
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        return f"{width}x{height}+{x}+{y}"

class PageIndicator(tk.Frame):
    """Page indicator for multi-page forms"""
    
    def __init__(self, parent, pages, **kwargs):
        super().__init__(parent, bg=Colors.SECTION_BG, **kwargs)
        self.pages = pages
        self.current_page = 0
        
        # Page numbers
        for i, page_name in enumerate(pages):
            page_frame = tk.Frame(self, bg=Colors.ACCENT_GRAY, width=40, height=40)
            page_frame.pack(side=tk.LEFT, padx=5, pady=10)
            
            page_label = tk.Label(
                page_frame,
                text=str(i + 1),
                font=Fonts.HEADING,
                bg=Colors.ACCENT_GRAY if i != self.current_page else Colors.PRIMARY_BLUE,
                fg='black' if i != self.current_page else 'white',
                width=5,
                height=2
            )
            page_label.pack()
            
            if i < len(pages) - 1:
                tk.Label(self, text="→", font=Fonts.HEADING, 
                        bg=Colors.SECTION_BG).pack(side=tk.LEFT, padx=2)
