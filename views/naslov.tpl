<html>
    <head>
        <title>Instagraf</title>
        
        <link rel="shortcut icon" href="{{ get_url('database', filename = 'logo.ico') }}" type="image/x-icon">
        
    </head>
    <body>
        <h1>{{!base}}</h1>

        <h2>
        <form action="/en/upload/" method="post" enctype="multipart/form-data">
            <input type="file" name="data" /> <br><br>

            <label for="tittle">Tittle</label>
            <input type="text" id="tittle" name="tittle"><br><br>

            <label for="x label">x label</label>
            <input type="text" id="x_label" name="x_label"><br><br>

            <label for="y label">y label</label>
            <input type="text" id="y_label" name="y_label"><br><br>

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

            <input type="submit" value='Pošlji'/>
        </form>
        </h2>

    </body>
</html>