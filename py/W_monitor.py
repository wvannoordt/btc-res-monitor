import tkinter as tk

class W_monitor_binding:

    def __init__(self, underlying_window, root, spec, opener):
        self.window = underlying_window
        self.root_module = root
        self.init_data(spec, opener)
        self.init_config()

    def init_data(self, spec, opener):
        self.target_file = ""
        self.id = -1
        self.control_window_obj = None
        self.monitor_specification = spec
        self.open_button = opener

    def init_config(self):
        self.root_module.title(self.monitor_specification)
        self.root_module.protocol("WM_DELETE_WINDOW", self.on_close)
        self.open_button.configure(activebackground="#058700")
        self.open_button.configure(background="#058700")
        self.open_button.configure(highlightbackground="#058700")

    def on_close(self):
        self.target_file = "none"
        self.control_window_obj.opendict[self.monitor_specification] = False
        self.open_button.configure(activebackground="#898989")
        self.open_button.configure(background="#636363")
        self.open_button.configure(highlightbackground="#636363")
        self.root_module.destroy()
        self.control_window_obj.reduce_monitors()
