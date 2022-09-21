class roman:
    def int_roman(self,num:int) -> str:
        tallies = [['I', 1],['IV',4],['V',5],['IX',9],['X', 10],['XL',40],['L', 50],['XC',90],['C', 100],['CD',400],['D', 500],['CM',900],['M', 1000]]
        try:
            import colorama
            from colorama import Fore
            colorama.init(autoreset=True)
            result = ""
            for char, value in reversed(tallies):
                if num//value:
                    count = num//value
                    result +=  char*count
                    num = num%value
            return Fore.GREEN+result
        except Exception as Ex:
            return Ex
#--------------------implementation ------------------
a = roman()
print(a.int_roman(1994))