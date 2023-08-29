import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    className='main-container',
    children=[
        html.Div(
            className='container',
            children=[
                html.H1("Container 1"),
                dcc.Input(id='input1', value='', type='text'),
                html.Div(id='output1')
            ]
        ),
        html.Div(
            className='container',
            children=[
                html.H1("Container 2"),
                dcc.Input(id='input2', value='', type='text'),
                html.Div(id='output2')
            ]
        )
    ]
)

@app.callback(
    Output('output', 'children'),
    [Input('input', 'value')]
)
def update_output(input_value):
    return f'You entered: {input_value}'

if __name__ == '__main__':
    app.run_server(debug=True)

# Generate HTML content
app_html_content = app.to_html()

print(app_html_content)

# Save the HTML content to a file
with open('index.html', 'w') as file:
    file.write(app_html_content)
