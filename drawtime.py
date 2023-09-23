import gmplot
import pandas as pd

df = pd.read_csv("aircraft_signal.csv")
gmap = gmplot.GoogleMapPlotter(40.72472, 8.938611117, 6)
gmap.plot(df["latitude"], df["longitude"], "#FF0000", edge_width=2.5)
gmap.draw("plotted_data.html")











