import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Michael Murillo'),
    html.H1(children='Matt Anikiej'),
    html.H1(children='David Butts'),
    html.H1(children='Luciano Silverstri'),
    html.H1(children='Liam Stanton'),
    html.H1(children='Math_Mayne'),
    html.H1(children='Jaclyn Frishcosy'),
    html.H1(children='Gautham Dharuman'),
])

