import matplotlib.pyplot as plt
import numpy as np


class OutputReports:
    def __init__(self,_colour = "blue"):
        self.colour = _colour
    def exportFile(self,_outputfile):
        if _outputfile != ""
            plt.savefig(_outputfile)
        else:
            plt.show()

    def barReport(self,_x,_x_label,_y,_y_label,_title):
        plt.bar(_x,_y,color=self.colour)
        plt.xlabel(_x_label)
        plt.ylabel(_y_label)
        plt.title(_title)

    def normalizeYears(self,_years):
        ret = np.array(_years)-2000
        return ret

    def reportYearTotalEvolution(self,_years,_total_weight,_outputfile =""):
        years = self.normalizeYears(_years)
        self.barReport(years,"Años",_total_weight,"Kilos","Kilos totales por año")
        plt.xticks(ticks=years)
        self.exportFile(_outputfile)

    def reportYearVariedadEvolution(self,_years,_weight,_variedad,_outputfile=""):
        title = f'Kilos de {_variedad} por año'
        years = self.normalizeYears(_years)
        self.barReport(years,"Años",_weight, "Kilos",title)
        plt.xticks(ticks=years)
        self.exportFile(_outputfile)






