<html>
    <head>
        <title>Instagraf</title>
        
        <link rel="shortcut icon" href="..\database\logo.ico" type="image/x-icon">
        <link rel="shortcut icon" href="{{ get_url('database', filename = 'logo.ico') }}" type="image/x-icon">
        <!-- <img src="{{ get_url('database', filename = 'logo.ico') }}" alt="Graph"/>       -->

    </head>
    <body>
        <h1>{{!base}}</h1>

        <h2>
        Here is your graph!
        </h2>
        
    % ime = graph_filename

        <img src="{{ get_url('graphs_made', filename = 'naloga04_abs_gama.png') }}" alt="Graph"/>
        <img src="{{ get_url('graphs_made', filename = ime ) }}" alt="Graph"/>
        <img src="..\graphs_made\{{!graph_filename}}" alt="Graph"/>

    </body>
</html>