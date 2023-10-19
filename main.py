import os
import tkinter as tk
from tkinter import filedialog, Menu
import pydicom
from PIL import Image

def convert_to_dicom(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            jpeg_image = Image.open(os.path.join(input_folder, filename))
            
            # Crear un nuevo objeto Dataset DICOM
            ds = pydicom.Dataset()

            # Establecer 'is_little_endian' y 'is_implicit_VR' de acuerdo a tus necesidades
            ds.is_little_endian = True  # O False según corresponda
            ds.is_implicit_VR = True    # O False según corresponda

            # Agregar metadatos DICOM según tus necesidades
            ds.PatientName = "Nombre del paciente"
            ds.PatientID = "ID del paciente"
            # Agregar más metadatos DICOM según sea necesario

            # Convertir la imagen JPEG en píxeles y guardarla en el archivo DICOM
            ds.PixelData = jpeg_image.tobytes()

            # Guardar el archivo DICOM
            output_filename = os.path.join(output_folder, filename.replace('.jpg', '.dcm'))
            ds.save_as(output_filename)

def select_input_folder():
    folder = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, folder)

def select_output_folder():
    folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder)

def convert_images():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    convert_to_dicom(input_folder, output_folder)
    result_label.config(text="Conversión completada.")

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("Acerca de")

    about_label = tk.Label(about_window, text="Conversión de JPEG a DICOM")
    about_label.config(font=("Helvetica", 16))
    about_label.pack(padx=20, pady=10)

    creator_label = tk.Label(about_window, text="Creado por Hernan Curuchet")
    creator_label.pack(pady=5)

    version_label = tk.Label(about_window, text="Versión 1.0")
    version_label.pack(pady=5)

    description_label = tk.Label(about_window, text="Esta aplicación convierte imágenes JPEG a archivos DICOM.")
    description_label.pack(pady=5)

    credits_label = tk.Label(about_window, text="Créditos y agradecimientos:")
    credits_label.config(font=("Helvetica", 12))
    credits_label.pack(pady=10)

    credits_text = tk.Text(about_window, height=5, width=40)
    credits_text.insert(tk.END, "Agradecemos a la comunidad de Python.")
    credits_text.config(state=tk.DISABLED)
    credits_text.pack()

    # Puedes agregar más información, como historial de cambios, políticas de privacidad, etc.

    close_button = tk.Button(about_window, text="Cerrar", command=about_window.destroy)
    close_button.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Conversión de JPEG a DICOM")
root.geometry("800x600")

# Crear el menú superior
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Etiquetas y entradas para seleccionar carpetas de entrada y salida
input_label = tk.Label(root, text="Carpeta de entrada (JPEG):")
input_label.pack()
input_folder_entry = tk.Entry(root)
input_folder_entry.pack()
input_button = tk.Button(root, text="Seleccionar carpeta de entrada", command=select_input_folder)
input_button.pack()

output_label = tk.Label(root, text="Carpeta de salida (DICOM):")
output_label.pack()
output_folder_entry = tk.Entry(root)
output_folder_entry.pack()
output_button = tk.Button(root, text="Seleccionar carpeta de salida", command=select_output_folder)
output_button.pack()

# Menú "Acerca de"
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Acerca de", menu=about_menu)
about_menu.add_command(label="Información del creador", command=show_about)

root.mainloop()