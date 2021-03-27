<html>
    <head>
        <title>Instagraf</title>
        
        <link rel="shortcut icon" href="..\database\logo.ico" type="image/x-icon">

    </head>
    <body>
        <h1>{{!base}}</h1>

        <h2>
        Here is your graph!
        </h2>
        
        <img src="{{ get_url('graphs_made', filename = 'naloga03_abs_beta.png') }}" alt="Graph"/>
        <img src="{{ get_url('graphs_made', filename = '{{!graph_filename}}') }}" alt="Graph"/>

    </body>
</html>