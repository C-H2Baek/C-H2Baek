<%@ page contentType = "text/html; charset=utf-8" %>
<%@ page import = "dto.Product" %>
<%@ page import = "dao.ProductRepository" %>
<jsp:useBean id="productDAO" class="dao.ProductRepository" scope="session" />
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" />
<!-- <link rel="stylesheet" href="./resources/css/bootstrap.css" /> -->
<title>Product List</title>
</head>
<body>
	<jsp:include page="MENU.jsp" />
	<div class="jumbotron">
		<div class="container">
			<h1 class="display-3">Product Information</h1>
		</div>
	</div>
	<%
		String id = request.getParameter("id");
		ProductRepository dao = ProductRepository.getInstance();
		Product product = dao.getProductById(id);
	%>
	<div class="container">
		<div class="row">
			<div class="col-md-5">
<%-- 				<img src="./resources/images/<%=product.getFilename()%>" style="width: 100%"> --%>
				<img src="/Upload/<%=product.getFilename()%>" style="width: 100%">
			</div>
			<div class="col-md-6">
			<h3><%=product.getPname()%></h3>
			<p><%=product.getDescription()%>
			<p> <b>상품 코드 : </b><span class="badde badge-danger">
				<%=product.getProductId()%></span>
			<p> <b>제조사</b> : <%=product.getManufacturer()%> 
			<p> <b>분류</b> : <%=product.getCategory()%> 
			<p> <b>재고 수</b> : <%=product.getUnitsInStock()%>
			<h4><%=product.getUnitPrice()%>원</h4>
			<p> <a href="#" class="btn btn-info"> 상품 주문 &raquo;</a>
				<a href="./PRODUCTS.jsp" class="btn btn-secondary"> 상품
				목록 &raquo;</a> 
			</div>
		</div>
		<hr>
	</div>
	<jsp:include page="FOOTER.jsp" />
</body>
</html>
