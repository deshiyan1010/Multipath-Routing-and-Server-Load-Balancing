
import time
import json
import os
import requests
from topo import N_SERVERS
import time
import threading
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import random
#     # index = 0
#     # time.sleep(0.2)
#     # for s in server:
#     #     try:
#     #         response = requests.get('http://'+s+':5000/usage_stats')
#     #         data = response.json()
#     #         cpu_usage[index] = data['cpu']
#     #         memory_usage[index] = data['mem']
#     #         connections[index] = data['active_connection']
#     #     except Exception as e:
#     #         print(e)
#     #     index+=1


server = ['10.0.0.'+str(i) for i in range(1,N_SERVERS+1)]


cpu_usage = [10 for i in range(N_SERVERS)]
memory_usage = [0 for i in range(N_SERVERS)]
connections = [0 for i in range(N_SERVERS)]

tx_packet = [10 for i in range(N_SERVERS)]
tx_bytes = [0 for i in range(N_SERVERS)]
rx_packet = [0 for i in range(N_SERVERS)]
rx_bytes = [10 for i in range(N_SERVERS)]

response_time = [10 for i in range(N_SERVERS)]


app = dash.Dash()



app.layout = html.Div([
    html.Div([
        dcc.Graph(id='live-graph-1', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='live-graph-2', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='live-graph-3', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='live-graph-4', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'})
    ]),
    html.Div([
        dcc.Graph(id='live-graph-5', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='live-graph-6', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='live-graph-7', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='live-graph-8', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'})
    ]),
    html.Div([
        dcc.Graph(id='live-graph-9', figure={
            'data': [{'x': [], 'y': [], 'type': 'bar'}],
        }, style={'width': '25%', 'height': '50%', 'display': 'inline-block'}),
    ]),
    dcc.Interval(
        id='interval-component',
        interval=1*500,  # in milliseconds
        n_intervals=0
    )
])



prev = None
last_updated = 0
def preprocess():
    global cpu_usage,memory_usage,connections,tx_packet,tx_bytes,rx_packet,rx_bytes,prev,last_updated
    response = requests.get('http://10.0.0.47:5000/stats')
    data = response.json()
    updated = False
    for index,s in enumerate(server):
        
        cpu_usage[index] = data[s]['cpu']
        memory_usage[index] = data[s]['mem']
        connections[index] = data[s]['active_connection']
        response_time[index] = data[s]['response_time']

        if prev and time.time()-last_updated>=1:        
            tx_packet[index] = data[s]['data_packets_sent'] - prev[s]['data_packets_sent']
            tx_bytes[index] = data[s]['data_bytes_sent'] - prev[s]['data_bytes_sent']
            rx_packet[index] = data[s]['data_packets_received'] - prev[s]['data_packets_received']
            rx_bytes[index] = data[s]['data_bytes_received'] - prev[s]['data_bytes_received']
            updated = True
            # print(data[s]['data_packets_received'] ,prev[s]['data_packets_received'],data[s]['data_bytes_received'], prev[s]['data_bytes_received'])
    prev = data

    if updated:
        last_updated = time.time()


    print(time.time(),tx_bytes,rx_bytes,connections)





@app.callback(Output('live-graph-1', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_1(n):
    x = server
    y = cpu_usage
    # print("CPU Update")
    data = {'x': x, 'y': y, 'type': 'bar'}
    fig = {'data': [data],'layout': {'title': 'CPU Usage'}}
    return fig


@app.callback(Output('live-graph-2', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_2(n):
    x = server
    y = memory_usage
    # print("Memory Update")
    data = {'x': x, 'y': y, 'type': 'bar','marker': {'color': 'green'}}
    fig = {'data': [data],'layout': {'title': 'Memory Usage'}}
    return fig


@app.callback(Output('live-graph-3', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_3(n):
    x = server
    y = connections
    # print("Connections Update")
    data = {'x': x, 'y': y, 'type': 'bar','marker': {'color': 'purple'}}
    fig = {'data': [data],'layout': {'title': 'Active Requests'}}
    return fig


@app.callback(Output('live-graph-4', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_4(n):
    x = server
    y = response_time
    # print("Data Update")
    data = {'x': x, 'y': y, 'type': 'bar'}
    fig = {'data': [data],'layout': {'title': 'Response Time'}}
    return fig

@app.callback(Output('live-graph-5', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_5(n):
    x = server
    y = tx_packet
    # print("Connections Update")
    data = {'x': x, 'y': y, 'type': 'bar','marker': {'color': 'purple'}}
    fig = {'data': [data],'layout': {'title': 'Tx Packets (5sec)'}}
    return fig

@app.callback(Output('live-graph-6', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_6(n):
    x = server
    y = tx_bytes
    # print("Connections Update")
    data = {'x': x, 'y': y, 'type': 'bar','marker': {'color': 'purple'}}
    fig = {'data': [data],'layout': {'title': 'Tx Bytes (5sec)'}}
    return fig

@app.callback(Output('live-graph-7', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_7(n):
    x = server
    y = rx_packet
    # print("Connections Update")
    data = {'x': x, 'y': y, 'type': 'bar','marker': {'color': 'purple'}}
    fig = {'data': [data],'layout': {'title': 'Rx Packets (5sec)'}}
    return fig

@app.callback(Output('live-graph-8', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_8(n):
    x = server
    y = rx_bytes
    # print("Connections Update")
    data = {'x': x, 'y': y, 'type': 'bar','marker': {'color': 'purple'}}
    fig = {'data': [data],'layout': {'title': 'Rx Bytes (5sec)'}}
    return fig

@app.callback(Output('live-graph-9', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_9(n):
    preprocess()
    x = server
    y = [random.randint(1, 10) for _ in range(N_SERVERS)]
    # print("Data Update")
    data = {'x': x, 'y': y, 'type': 'bar'}
    fig = {'data': [data],'layout': {'title': 'Donno'}}
    return fig

if __name__ == '__main__':
    app.run_server(debug=True,host='10.0.0.47', port=8080)