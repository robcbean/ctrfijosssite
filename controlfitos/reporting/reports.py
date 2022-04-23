import matplotlib.pyplot as plt

class OutputReports:
    def __init__(self,_colour = "blue"):
        self.colour = _colour

    def barReport(self,_x,_x_label,_y,_y_label,_title,_outputfile=""):
        plt.barh(_x,_y)

    def reportYearTotalEvolution(self,_years,_total_weight,_outputfile =""):
        self.barReport(_years,"Años",_total_weight,"Kilos","Kilos totales por año",_outputfile)




