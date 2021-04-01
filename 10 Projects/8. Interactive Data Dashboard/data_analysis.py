from pandas_datareader import data
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models.annotations import Title


def inc_dec(c, o):
    if c > o:
        return "Increase"
    elif c < o:
        return "Decrease"
    else:
        return "Equal"


start = datetime(2016, 3, 1)
end = datetime(2016, 3, 10)

df = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)
df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Close + df.Open) / 2
df["Height"] = abs(df.Close - df.Open)

p = figure(x_axis_type='datetime', width=1000, height=300)
t = Title()
t.text = "Candlestick Chart"
p.title = t

hours_12 = 12 * 60 * 60 * 1000  # 12 hrs into ms

# Method 1 : To prevent overwriting of data
'''
x_close_more = df.index[df.Close > df.Open]
x_close_less = df.index[df.Close < df.Open]
y_centre_point = (df.Close + df.Open) / 2
width = abs(df.Close - df.Open)

p.rect(x_close_more, y_centre_point, hours_12, width, fill_color='green', line_color='black')
p.rect(x_close_less, y_centre_point, hours_12, width, fill_color='red', line_color='black')'''

# Method 2 : Using an additional field
p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"], fill_color='green', line_color='black')
p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"], fill_color='red', line_color='black')
output_file("CS.html")
show(p)
