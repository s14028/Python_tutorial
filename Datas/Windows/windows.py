import pandas
ds = pandas.read_excel("data.xlsx", sheetname="Arkusz1", header=None)
print(ds)

ds.to_html("data.html")
