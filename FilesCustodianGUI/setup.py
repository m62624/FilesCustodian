from cx_Freeze import setup, Executable

setup(
    name="FilesCustodian",
    version="0.0.2",
    description="Backup utility",
    executables=[Executable("FilesCustodianGUI/main_window.py")],
)
