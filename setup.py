import cx_Freeze

executables = [cx_Freeze.Executable("monopoly.py")]

cx_Freeze.setup(
    name="Monopoly",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["monopoly.png","play.png","play2.png","icon.png","music.wav","micro.png"]}},
    executables = executables

    )
