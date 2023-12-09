from collections.abc import Iterable


class Pen:
    manufactuere = "Bangladesh"  # A class variable shared among all instances of the class
    head = True  # A class variable shared among all instances of the class

    def __init__(self, color, brand, design_pattern, ball_len) -> None:
        self.color = color
        self.brand = brand
        self.design_pattern = design_pattern
        self.ball_len = ball_len

    def version(self, version):
        print(version)
    def __dir__(self) -> Iterable[str]:
        return f"{self.color},{self.brand},{self.design_pattern},{self.ball_len}"



matador=Pen("green","matador",45.326,"6cm")
matador.version(555555555)
claro=Pen("blue","matador",45.326,"6cm")
claro.version(555555555)
altime=Pen("red","matador",45.326,"6cm")
altime.version(555555555)


        