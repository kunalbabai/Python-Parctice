tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # specify more numerals if you wish
}

def roman_deci(map):
    try:
        import colorama
        from colorama import Fore,Style
        colorama.init(autoreset=True)
        roman = input('Enter the Roman character -').upper()
        result = map[roman[-1]]
        for i in range(len(roman)-2,-1,-1):
            if map[roman[i]] < map[roman[i+1]]:
                result -= map[roman[i]]
            elif map[roman[i]] == map[roman[i+1]] or map[roman[i]] > map[roman[i+1]]:
                result += map[roman[i]]
        print(Fore.GREEN+Style.BRIGHT+str(result))
    except Exception as Ex:
        return Ex

(roman_deci(map=tallies))