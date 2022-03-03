from cx_Freeze import setup, Executable
base = None
# Replace "main.py" with the name of script
executables = [Executable("wordle.py", base=base)]
# Fill in the list with the packages used by your program
packages = ["random","sys","ansicon"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
# Adapt the values of the variables "name", "version" and "description"
setup(
    name="wordle.ribou",
    options=options,
    version="1.0",
    description='Wordle game by Ribou',
    executables=executables
)