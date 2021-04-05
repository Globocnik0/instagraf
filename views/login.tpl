<html>
    <head>
        <title>Instagraf</title>
        
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
        
        <link rel="shortcut icon" href="{{ get_url('database', filename = 'logo.ico') }}" type="image/x-icon">

    </head>
    <body>



        <h1 class="text-center">You need to login first.</h1>

        <h2 class="text-center"> If you don't have an account yet, you can register for free!</h2>

        <h3 class="text-center" style="color:rgb(255, 38, 0);">{{!alert}} </h3>

        <center>
        <div class="back">


            <div class="div-center">
          
          
              <div class="content">

        <form action="/en/login/" method="post">  
            <div class="form-group">
                <label for="username">Username : </label>   
                <input type="text" class="form-control-lg" placeholder="Enter Username" name="username" id="username" required> 
            </div>
            
            <br>

            <div class="form-group">
                <label for="password">Password : </label>   
                <input type="password" class="form-control-lg" placeholder="Enter Password" name="password" id="password" required> 
            </div>

                <input class="form-check-input" type="checkbox" name="first_login" id="first_login"> I don't have an account/register me!
                <br><br>

            <div class="align-center">
                <button type="submit" class="btn btn-success">Log in</button>  
            </div> 
            

        </form>  
        </div>
        </div>
        </div>
    </center>


    </body>
</html>