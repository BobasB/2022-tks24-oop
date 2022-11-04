class Rocket:
    def __init__(self, name, mass) -> None:
        assert isinstance(name, str), "Передане імя ракети має бути стрічкою!"
        assert mass >= 0, "Масса має бути більшою за нуль!"
        if mass == 0:
            raise ValueError("Сумнівно що маса є рівна 0???")
        
        self.name = name
        self.mass = mass

    @property
    def get_info(self):
        #modified_name = self.name.lower()
        return f"Ракета {self.name} та має масу {self.mass} кг"
    
    @property
    def get_info_en(self):
        return f"Ракета {self.name} та має масу {self.convert()} фунтів"
    
    def convert(self):
        return self.mass * 2.20462262


#r1 = Rocket("Falcon 9", 549054)
#
#print(r1.get_info)
#
#r2 = Rocket("Ares I", -25500)
#
#print(r2.get_info_en)

