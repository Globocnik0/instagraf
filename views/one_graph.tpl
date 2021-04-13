<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">

        <title>Instagraf</title>

        <link rel="shortcut icon" href="{{ get_url('database', filename = 'logo.ico') }}" type="image/x-icon">

    </head>
    <body>

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="">Instagraf</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
    
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="/en/">Upload file</a>
                </li>
    
                <li class="nav-item">
                    <a class="nav-link" href="/en/graphs/">My graphs</a>
                </li>
                </ul>
    
                <ul class="nav navbar-nav navbar-right">
                <form class="form-inline my-2 my-lg-0" action="/en/" method="post">
                    <input type="submit" value='Log out' class="btn btn-success my-2 my-sm-0"/>
                </form>
                </ul>
    
            </div>
        </nav>  


        <div class="container">
        <h1 style="color:rgb(59, 182, 110);">Congratulations, your file has been uploaded and a graph was made from it. Click on it to download.</h1>




            %filename = graph['filename'].split('.', 1)[0]
            %path_to_image = '/graphs_made/' + str(username) + '/' + filename + '.png'
            <a class="credit" href={{path_to_image}} download={{filename}}>
                <img src={{path_to_image}} alt="Graph"/>   
            </a>
            %end
        </div>
    </body>
</html>