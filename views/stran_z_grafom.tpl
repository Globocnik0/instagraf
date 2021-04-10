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
    %filename = graph['filename'].split('.', 1)[0]
    %path_to_image = '/graphs_made/' + str(username) + '/' + filename + '.png'
    <a class="credit" href={{path_to_image}} download={{filename}}>
        <img src={{path_to_image}} alt="Graph"/>   
    </a>
    %end

    </body>
</html>