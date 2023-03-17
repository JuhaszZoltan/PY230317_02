class Hallgato:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.nem:bool = v[1] == 'm'
        self.befizetes:int = int(v[2])
        self.eredmenyek:dict[str, int] = {
            'hálózat': int(v[3]),
            'mobil': int(v[4]),
            'frontend': int(v[5]),
            'backend': int(v[6]),
        }
        self.atlag:float = sum(self.eredmenyek.values()) / 4
        for val in self.eredmenyek.values():
            if val < 51:
                self.van_bukas:bool = True
                break
        else: self.van_bukas:bool = False