<html>
    <head>
        <title>Instagraf</title>
        
        <link rel="shortcut icon" href="{{ get_url('database', filename = 'logo.ico') }}" type="image/x-icon">

    </head>
    <body>
        <h1>You need to login first.</h1>

        <h2>
            If you don't have an account yet, you can register for free!
        </h2>

        <form action="/en/login/" method="post">  
 
                <label>Username : </label>   
                <input type="text" placeholder="Enter Username" name="username" required>  
                <label>Password : </label>   
                <input type="password" placeholder="Enter Password" name="password" required>  
                <input type="checkbox" name="first_login" id="first_login"> I don't have an account/register me!
                <button type="submit">Login</button>   

        </form>  

    </body>
</html>