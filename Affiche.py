
import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
from collections import OrderedDict
import dash_table
import GetTense
import ForAffiche
import readBook
import listOfLevelsOP
import unusedwordsinlevel

y = readBook.readBookFile(readBook.convertBook('5.PNG'))
x = listOfLevelsOP.GetLsisLevel(y)[0]



tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

itemsA1 = []
itemsA2 =[]
itemsB1=[]
itemsB2=[]
itemsC=[]
unusedWordsA1 =unusedwordsinlevel.unusedIteminLevel('A1')
unusedWordsA2 =unusedwordsinlevel.unusedIteminLevel('A2')
unusedWordsB1 =unusedwordsinlevel.unusedIteminLevel('B1')
unusedWordsB2 =unusedwordsinlevel.unusedIteminLevel('B2')
unusedWordsC =unusedwordsinlevel.unusedIteminLevel('C')
for i in unusedWordsA1 :
    itemsA1.append(dbc.DropdownMenuItem(i))
for i in unusedWordsA2 :
    itemsA2.append(dbc.DropdownMenuItem(i))
for i in unusedWordsB1 :
    itemsB1.append(dbc.DropdownMenuItem(i))
for i in unusedWordsB2 :
    itemsB2.append(dbc.DropdownMenuItem(i))
for i in unusedWordsC :
    itemsC.append(dbc.DropdownMenuItem(i))
#tenses
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.DataFrame(OrderedDict([
    ('Tense', ['Present', 'Past', 'Future', 'Conditional']),
    ('simple', [len(GetTense.SimplePresent), len(GetTense.simplePast), len(GetTense.future), 0]),
    ('Progressive', [len(GetTense.PastProgressive), len(GetTense.PastProgressive), len(GetTense.futureProgressive), len(GetTense.conditionalProgressive)]),
    ('Perfect', [len(GetTense.PresentProgressive), len(GetTense.PastPerfect), len(GetTense.futurePerfect), len(GetTense.conditionalPerfect)]),
    ('Perfect Progressive', [len(GetTense.presentPerfectProgressive), len(GetTense.PastPerfectProgressive), len(GetTense.futurePerfectProgressive), len(GetTense.conditionalPerfectProgressive)])
]))


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Stat Level", href="/", active="exact"),
                dbc.NavLink("Tenses", href="/page-1", active="exact"),
                dbc.NavLink("Used words in level", href="/page-2", active="exact"),
            ],
            brand="Statistics of The book",
            color="primary",
            dark=True,
        ),
        dbc.Container(id="page-content", className="pt-4"),

    ]
)

#words used in level
@app.callback(Output('output-tab', 'children'),
              [Input('tabs', 'value')])
def display_content(value):
    data = [
        {   'labels' : ['Unused Words ','Used Words'],
            'values': [ForAffiche.usedUnusedWOrdsInLevel('A1',x),ForAffiche.usedUnusedWOrdsInLevel('A2',x),ForAffiche.usedUnusedWOrdsInLevel('B1',x),ForAffiche.usedUnusedWOrdsInLevel('B2',x),ForAffiche.usedUnusedWOrdsInLevel('C',x)][int(value)-1],
            'type': 'pie',
        },
    ]


    A1=html.Div(
    [
        dbc.DropdownMenu(
             itemsA1, label="Unused Words", color="info", className="m-1"

         ),html.Div([
        dcc.Graph(

            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 50,
                        'r': 50,
                        'b': 50,
                        't': 50
                    },
                    'legend': {'x': 0, 'y': 1},
                    'title': 'Words used in level A1'
                }
            }
        ),
    ])
    ],
    style={"display": "flex", "flexWrap": "wrap"},
)
    A2 = html.Div(
        [
            dbc.DropdownMenu(
                itemsA2, label="Unused Words", color="info", className="m-1"
            ),html.Div([
        dcc.Graph(

            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 50,
                        'r': 50,
                        'b': 50,
                        't': 50
                    },
                    'legend': {'x': 0, 'y': 1},
                    'title': 'Words used in level A2'
                }
            }
        ),
    ])
        ],

        style={"display": "flex", "flexWrap": "wrap"},
    )
    B1 = html.Div(
        [
            dbc.DropdownMenu(
                itemsB1, label="Unused Words", color="info", className="m-1"
            ),html.Div([
        dcc.Graph(

            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 50,
                        'r': 50,
                        'b': 50,
                        't': 50
                    },
                    'legend': {'x': 0, 'y': 1},
                    'title': 'Words used in level B1'
                }
            }
        ),
    ])
        ],

        style={"display": "flex", "flexWrap": "wrap"},
    )
    B2 = html.Div(
        [
            dbc.DropdownMenu(
                itemsB2, label="Unused Words", color="info", className="m-1"
            ),html.Div([
        dcc.Graph(

            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 50,
                        'r': 50,
                        'b': 50,
                        't': 50
                    },
                    'legend': {'x': 0, 'y': 1},
                    'title': 'Words used in level B2'
                }
            }
        ),
    ])
        ],

        style={"display": "flex", "flexWrap": "wrap"},
    )
    C = html.Div(
        [
            dbc.DropdownMenu(
                itemsC, label="Unused Words", color="info", className="m-1"
            ),html.Div([
        dcc.Graph(

            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 50,
                        'r': 50,
                        'b': 50,
                        't': 50
                    },
                    'legend': {'x': 0, 'y': 1},
                    'title': 'Words used in level C'
                }
            }
        ),
    ])
        ],

        style={"display": "flex", "flexWrap": "wrap"},
    )
    if value == 1 :
        return (A1)
    elif value == 2 :
        return (A2)
    elif value == 3 :
        return (B1)
    elif value == 4 :
        return (B2)
    elif value == 5 :
        return (C)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['A1', "A2", "B1", 'B2', 'C'], 'y': listOfLevelsOP.GetLsisLevel(y)[1], 'type': 'bar', 'name': 'SF'},

            ],
            'layout': {
                'title': 'Used words by levels'
            }
        }
    ),
    elif pathname == "/page-1":
        return html.Div([
            dbc.Alert(
                [
                    html.H1("Used Times", className="alert-heading"),
                    html.Hr(),
                    html.H4(
                        "This table represent the four tenses with their types "
                            " used in the book. "

                    ),


                ]
            ),html.Hr(style={"width": "0%","color": "#FEC700"}),
            html.Hr(style={"width": "0%", "color": "#FEC700"}),
            html.Hr(style={"width": "0%", "color": "#FEC700"}),

    dash_table.DataTable(
        id='table-dropdown',
        data=df.to_dict('records'),
        columns=[
            {'id': 'Tense', 'name': 'Tense', 'presentation': 'dropdown'},
            {'id': 'simple', 'name': 'simple', 'presentation': 'dropdown'},
            {'id': 'Progressive', 'name': 'Progressive', 'presentation': 'dropdown'},
            {'id': 'Perfect', 'name': 'Perfect', 'presentation': 'dropdown'},
            {'id': 'Perfect Progressive', 'name': 'Perfect Progressive'},
        ],

        editable=False,


        dropdown={
            'Tense': {
                'options': [
                    {'label': i, 'value': i}
                    for i in df['Tense'].unique()
                ],
                'clearable':True,


            },
        }
    ),
])
    elif pathname == "/page-2":
        return ( html.Div([
            dcc.Tabs(id='tabs', value=1, children=[
                dcc.Tab(label='A1', value=1,style=tab_style,selected_style=tab_selected_style),
                dcc.Tab(label='A2', value=2,style=tab_style,selected_style=tab_selected_style),
                dcc.Tab(label='B1', value=3,style=tab_style,selected_style=tab_selected_style),
                dcc.Tab(label='B2', value=4,style=tab_style,selected_style=tab_selected_style),
                dcc.Tab(label='C', value=5,style=tab_style,selected_style=tab_selected_style),



            ]),

            html.Div(id='output-tab')
        ]))

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=5000)