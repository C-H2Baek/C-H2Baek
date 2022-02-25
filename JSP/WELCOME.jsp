<%@ page contentType = "text/html; charset=utf-8" %>
<%@ page import = "java.util.Date" %>
<%@ page import = "java.text.SimpleDateFormat" %>


<html>
<head>
<link rel="stylesheet" href="./resources/css/bootstrap.min.css" />
<title>Welcome</title>
</head>
<body>
	<%@ include file = "MENU.jsp" %>
	<%! String greeting = "Welcome To ShoppingMall";
	String tagline = "Welcome to Web Market"; %>
	<div class = "jumbotron">
		<div class = "container">
			<h1 class = "display-3">
				<%= greeting %>
			</h1>
		</div>
	</div>
	<main role = "main">
	<div class = "container">
		<div class = "text-center">
			<h3>
				<%= tagline %>
			</h3>
			
		</div>
		<hr>
	</div>
	</main>
	<%@ include file = "FOOTER.jsp" %>
</body>
</html>
