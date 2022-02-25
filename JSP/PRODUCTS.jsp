<%@ page contentType = "text/html; charset=utf-8" %>
<%@ page import = "java.util.ArrayList" %>
<%@ page import = "dto.Product" %>
<%@ page import = "dao.ProductRepository" %>

<jsp:useBean id="productDAO" class="dao.ProductRepository" scope="session" />
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="./resources/css/bootstrap.min.css" />
<title>Product List</title>
</head>
<body>
	<jsp:include page="MENU.jsp" />
	
	<div class="jumbotron">
		<div class="container">
			<h1 class="display-3">Product List</h1>
		</div>
	</div>
	<%
		ProductRepository dao = ProductRepository.getInstance();
		ArrayList<Product> listOfProducts = dao.getAllProducts();
	%>
	<div class="container">
		<div class="row" align="center">
			<%
				for (int i = 0; i < listOfProducts.size(); i++) {
					Product product = listOfProducts.get(i);
			%>
			<div class="col-md-4">
<%-- 				<img src="./resources/images/<%=product.getFilename()%>" style="width: 100%"> --%>
				<img src="/Upload/<%=product.getFilename()%>" style="width: 100%">
				<h5 class="navbar-brand"><%=product.getManufacturer() %></h5>
				<h3 class="jumbotron"><%=product.getPname() %></h3>
				<p><%=product.getDescription() %>
				<p><%=product.getUnitPrice() %>
				<p> <a href="./PRODUCT.jsp?id=<%=product.getProductId() %>"
				class = "btn btn-secondary" role="button"> Detail Information &raquo;</a>
			</div>
			<%
				}
			%>
		</div>
		<hr>
	</div>
	<%@ include file = "FOOTER.jsp" %>
</body>
</html>
