<!DOCTYPE html>
<html>
<head>
	<meta content="width=device-width, initial-scale=1" name="viewport">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet">
	<title>Instagraf</title>
	<link href="{{ get_url('database', filename = 'logo.ico') }}" rel="shortcut icon" type="image/x-icon">
</head>
<body>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
		<a class="navbar-brand" href="">Instagraf</a> <button aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#navbarSupportedContent" data-toggle="collapse" type="button"><span class="navbar-toggler-icon"></span></button>
		<div class="collapse navbar-collapse" id="navbarSupportedContent">
			<ul class="navbar-nav mr-auto">
				<li class="nav-item active">
					<a class="nav-link" href="/en/">Upload file</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="/en/graphs/">My graphs</a>
				</li>
			</ul>
			<div class="nav navbar-nav navbar-right" style="margin-left: 2em">
				<form action="/en/" class="form-inline my-2 my-lg-0" method="post">
					<input class="btn btn-success my-2 my-sm-0" type="submit" value='Log out'>
				</form>
			</div>
		</div>
	</nav>
	<div class="container">
		{{!base}}
	</div>
</body>
</html>