import tkinter as tk
import monitor
import W_monitor

class W_control_binding:

    def __init__(self, underlying_window, root):
        self.window = underlying_window
        self.root_module = root
        self.init_data()
        self.init_config()

    def init_data(self):
        self.monitors = []
        self.target_file_residual = "./stats/residual_norm.dat"
        self.target_file_wss = "./outputBndySolution/boundaryData.dat"
        self.target_file_wss_wm = "./outputBndySolution/wall_model_data.dat"
        self.opendict = None

    def init_config(self):
        self.opendict = {"Residual": False, "WSS": False, "WSS-wm": False}
        self.window.residuals_button.configure(command=lambda monitor_specification = "Residual",editor = self.window.residuals_edit_button,target_file = self.target_file_residual, opener = self.window.residuals_button: self.create_motitor(monitor_specification, editor, target_file, opener))
        self.window.wall_shear_button.configure(command=lambda monitor_specification = "WSS", editor = self.window.wall_shear_edit_button, target_file = self.target_file_wss, opener = self.window.residuals_button: self.create_motitor(monitor_specification, editor, target_file, opener))
        self.window.wall_shear_wm_button.configure(command=lambda monitor_specification = "WSS-wm", editor = self.window.wall_shear_wm_edit_button, target_file = self.target_file_wss_wm, opener = self.window.residuals_button: self.create_motitor(monitor_specification, editor, target_file, opener))

    def create_motitor(self, monitor_specification_i, editor, target_file_i, opener):
        if not self.opendict[monitor_specification_i]:
            new_root = tk.Toplevel(self.root_module)
            new_monitor = monitor.MainWindow(new_root)
            bindings = W_monitor.W_monitor_binding(new_monitor, new_root, monitor_specification_i, opener)
            bindings.target_file = target_file_i
            bindings.id = hash(bindings)
            bindings.control_window_obj = self
            self.monitors.append(bindings)
            editor.configure(command=lambda id = bindings.id, spec = monitor_specification_i: self.config_monitor_properties(id, spec))
            self.opendict[monitor_specification_i] = True

    def config_monitor_properties(self, id, spec):
        if self.opendict[spec]:
            print("needs implementation")

    def reduce_monitors(self):
        for monitor in self.monitors:
            if monitor.target_file == "none":
                self.monitors.remove(monitor)
