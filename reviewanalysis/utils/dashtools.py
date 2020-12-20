import dash
import plotly
from flask import request
import plotly.graph_objects as go
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash() 

def run_dash_server(go_fig, port_num=9000):
    app.layout = html.Div([
                        dcc.Location(id='url', refresh=False),
                        dcc.Link('Navigate to "/"', href='/'),
                        html.Br(),
                        dcc.Link('Close Dash Server', href='/shutdown'),

                        # content will be rendered in this element
                        html.Div(id='page-content'),
                        dcc.Graph(figure=go_fig)
                        ])

    app.run_server(debug=True,
                    host="127.0.0.1", 
                    port=port_num)

def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with Werkzeug server')
    func()

@app.callback(dash.dependencies.Output('page-content', 'children'),
            [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname=='/shutdown':
        shutdown()
    return html.Div([
        html.H3('You are on page {}'.format(pathname))
    ])