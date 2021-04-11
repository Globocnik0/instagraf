<!doctype html>
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
                <a class="nav-link" href="/en/">Upload file <span class="sr-only">(current)</span></a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/en/graph/">My graphs</a>
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
        <h1 style="color:rgb(59, 182, 110);">{{!base}}</h1><br>
        
        <h3 style="color:rgb(255, 38, 0);">{{!alert}} </h3>

        <h2>
        <form action="/en/upload/" method="post" enctype="multipart/form-data">
            
            <div class="col-sm-9">
                <label for="file">You can upload .txt, .csv or .xlsx file here. Make sure data is written in the first two columns, with no headers in the first row.</label> <br><br>
                <input type="file" name="data" class="form-control form-control-lg" aria-label="file example" required/> <br>
            </div>
            

            <div class="col-sm-2">
                <label for="title">Title</label>
                <input type="text" id="title" name="title" class="form-control"><br>

            </div>
            
                <div class="row">
                  <div class="col-sm-2">
                    <label for="x label">x label</label>
                    <input type="text" id="x_label" name="x_label" class="form-control"><br>
                  </div>
                  <div class="col-sm-2">
                    <label for="y label">y label</label>
                    <input type="text" id="y_label" name="y_label" class="form-control"><br>
                  </div>
                </div>


            <label for="fit">Choose a fit:</label>
            <select name="fit" id="fit">
              <optgroup label="polynomial fit">
                <option value="linear">Linear</option>
                <option value="quadratic">Quadratic</option>
                <option value="cubic">Cubic</option>
              </optgroup>

                <option value="exponential">Exponential</option>
                <option value="logarithmic">Logarithmic</option>
                <option value="None">Without fit</option>
            </select><br><br>

            <input type="submit" value='Submit' class="btn btn-success"/>
        </form>
        </h2>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" 
        integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous">
        </script>

    </body>
</html>