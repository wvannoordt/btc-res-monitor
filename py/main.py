import sys
import control
import control_support
import W_control
import tkinter as tk

root = tk.Tk();
top = control.ControlWindow(root);
bindings = W_control.W_control_binding(top, root)
control_support.init(root, top)
root.mainloop()
