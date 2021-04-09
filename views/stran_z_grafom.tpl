<html>
    <head>
        <title>Instagraf</title>
        

        <link rel="shortcut icon" href="{{ get_url('database', filename = 'logo.ico') }}" type="image/x-icon">
        <!-- <img src="{{ get_url('database', filename = 'logo.ico') }}" alt="Graph"/>       -->

    </head>
    <body>
        <h1>{{!base}}</h1>

        <h2>
        Here are your graphs!
        </h2>

    %
    %   
    %for graph in graphs:
    %path = str(username) + '/' + graph['filename'].split('.', 1)[0] + '.png'
    %relative_path = '/graphs_made/' + path
    <img src={{relative_path}} alt="Graph"/>   
    %end

    </body>
</html>