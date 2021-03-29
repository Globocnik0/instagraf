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
        <div class="container">
        <h1>{{!base}}</h1><br><br>

        
        <h2>
        <form action="/en/upload/" method="post" enctype="multipart/form-data">
            
            <div>
            <input type="file" name="data" class="form-control form-control-lg"/> <br><br>
            </div>

            <div class="col-sm-2">
            <label for="tittle">Tittle</label>
            <input type="text" id="tittle" name="tittle" class="form-control"><br>
        
            <label for="x label">x label</label>
            <input type="text" id="x_label" name="x_label" class="form-control"><br>

            <label for="y label">y label</label>
            <input type="text" id="y_label" name="y_label" class="form-control"><br>
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
        integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>

    </body>
</html>