import os
import dash
import plotly
import pandas as pd
from subprocess import call
from reviewanalysis.utils.csvtools import generate_csv
from flask import request
import plotly.graph_objects as go
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

app = dash.Dash() 
dir_name = os.getcwd()
file_path = ""
topic_reviews = pd.DataFrame()
num_topics = 0

def run_dash_server(go_fig, port_num=9000, topic_df=pd.DataFrame(), topics=None):
    app.layout = html.Div([
                        dcc.Location(id='url', refresh=False),
                        dcc.Link('Navigate to "/"', href='/'),
                        html.Br(),
                        dcc.Link('Close Dash Server', href='/shutdown'),
                
                        # content will be rendered in this element
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dcc.Input(id='save_dir', value=str(os.getcwd()), type='text'),
                        html.Button(id='submit-button-1', type='submit', children='Submit'),
                        html.Div(id='output-div-1'),
                        html.Br(),
                        dcc.Input(id='csv_name', value='topic.csv', type='text'),
                        html.Button(id='submit-button-2', type='submit', children='Submit'),
                        html.Div(id='output-div-2'),
                        html.Br(),
                        html.Div(id='page-content'),
                        #dcc.Link('Generate Topic CSV', href='/generate'),
                        html.Button(id='generate-csv', type='submit', children='Generate CSV'),
                        html.Div(id='output-div-3'),
                        dcc.Graph(figure=go_fig)
                        ])

    global topic_reviews
    global num_topics
    topic_reviews = topic_df
    num_topics = topics

    #print(topic_reviews)
    app.run_server(debug=True,
                    host="127.0.0.1", 
                    port=port_num)

def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with Werkzeug server')
    func()

def generate():
    if not os.path.exists(dir_name):
        print("Path does not exist! : {}".format(dir_name))
        shutdown()

    generate_csv(topic_reviews, file_path, num_topics)

@app.callback(Output('output-div-1', 'children'),
              [Input('submit-button-1', 'n_clicks'),
               State('save_dir', 'value')])
def update_output(clicks, input_value):
    if clicks is not None:
        global dir_name
        dir_name = input_value
        if not os.path.exists(dir_name):
            print("Path does not exist!")
            shutdown() 
        print(dir_name)

@app.callback(Output('output-div-2', 'children'),
              [Input('submit-button-2', 'n_clicks'),
               State('csv_name', 'value')])
def update_second_output(clicks, input_value):
    if clicks is not None:
        global file_path
        file_path = os.path.join(dir_name, input_value)
        print(file_path)

@app.callback(Output('output-div-3', 'children'),
              [Input('generate-csv', 'n_clicks')])
def generate_link_csv(clicks):
    if clicks is not None:
        generate()

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname=='/shutdown':
        shutdown()
    if pathname=='/generate':
        generate()
    return html.Div([
        html.H3('You are on page {}'.format(pathname))
    ])