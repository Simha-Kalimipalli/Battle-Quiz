import os

program_name = "Bataquiz"
main_file = "Trivia0611.py"
libraries_used = ["pygame", "sys", "os", "pandas", "random", "pygbutton", "numpy"]
files_needed = ["images", "sounds", "data"]
program_description = "This is a quiz game called Bataquiz"
program_version = "0.0.2"

python_path = r"C:\Users\Sree\AppData\Local\Programs\Python\Python36"




code = f"""\
import cx_Freeze

cx_Freeze.setup(
    name="{program_name}",
    version = "{program_version}",
    description = "{program_description}",
    options={{"build_exe": {{"packages": {libraries_used},
                           "include_files": {files_needed}}}}},
    executables=[cx_Freeze.Executable("{main_file}")]

)
"""

with open("setup.py", 'w') as setup_file:
    setup_file.write(code)


os.environ['TCL_LIBRARY'] = rf'{python_path}\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = rf'{python_path}\tcl\tk8.6'
libraries_used.append("cx_Freeze")
for i in libraries_used:
    os.system(rf"{python_path}\Scripts\pip.exe install {i}")

os.system(rf"{python_path}\python.exe setup.py build")
os.system(rf"{python_path}\python.exe setup.py bdist_msi")  # for creating msi installer
#os.system(rf"{python_path}\python.exe setup.py bdist_dmg")  # only on mac create an installer

os.remove("setup.py")