<%@ page contentType = "text/html; charset=utf-8" %>
<%@ page import = "java.util.Date" %>
<%@ page import = "java.text.SimpleDateFormat" %>
<footer class = "container">
		<p>&copy; WebMarket</p>
		<div class = "container">
		<div class = "jumbotron">
			<%
			
			Date today = new Date();
	     	SimpleDateFormat date = new SimpleDateFormat("yyyy/MM/dd");
	        SimpleDateFormat time = new SimpleDateFormat("hh:mm:ss a");
	        out.println("Current Date : " + today + "<br>" + "Date: " + date.format(today) + "<br>" +"Time: " + time.format(today));    
  			%>
		</div>
		<hr>
	</div>
</footer>