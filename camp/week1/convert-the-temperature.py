class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        lis = []
        lis.append(float(("%.6f" % (celsius + 273.15))))
        lis.append(float(("%.6f" % ((celsius * 1.8) + 32.00))))
        return lis