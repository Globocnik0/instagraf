<!DOCTYPE html>
<html>
<head>
	<title>Instagraf</title>
	<meta content="width=device-width, initial-scale=1" name="viewport">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet">
	<link href="{{ get_url('database', filename = 'logo.ico') }}" rel="shortcut icon" type="image/x-icon">
</head>
<body>
	<h1 class="text-center">You need to login first.</h1>
	<h2 class="text-center">If you don't have an account yet, you can register for free!</h2>
	<h3 class="text-center" style="color:rgb(255, 38, 0);">{{!alert}}</h3>
	<center>
		<div class="back">
			<div class="div-center">
				<div class="content">
					<form action="/en/login/" method="post">
						<div class="form-group">
							<label for="username">Username :</label> <input class="form-control-lg" id="username" name="username" placeholder="Enter Username" required="" type="text">
						</div><br>
						<div class="form-group">
							<label for="password">Password :</label> <input class="form-control-lg" id="password" name="password" placeholder="Enter Password" required="" type="password">
						</div><input class="form-check-input" id="first_login" name="first_login" type="checkbox"> I don't have an account/register me!<br>
						<br>
						<div class="align-center">
							<button class="btn btn-success" type="submit">Log in</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</center>
</body>
</html>