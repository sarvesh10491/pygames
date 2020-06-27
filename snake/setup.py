import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
    name = "Snake",
    options = {"build.exe":
                {"packages":["pygame"], 
                "included_files":["icon.png",
                                  "snakehead.jpg",
                                  "snakebody.jpg",
                                  "food1.jpg",
                                  "food2.jpg",
                                  "food3.jpg",
                                  "food4.jpg",
                                  "food5.jpg",
                                  "food6.jpg",
                                  "food7.jpg"]}},
    description = "Snake game",
    executables = executables
)

