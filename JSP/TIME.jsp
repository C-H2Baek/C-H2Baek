<%@ page contentType = "text/html; charset=utf-8" %>
<%@ page import = "java.util.Date" %>
<%@ page import = "java.text.SimpleDateFormat" %>
<html>
<body>
	<div class = "container">
		<div class = "text-center">
			<%
			response.setIntHeader("Refresh", 1);
			Date today = new Date();
	     	SimpleDateFormat date = new SimpleDateFormat("yyyy/MM/dd");
	        SimpleDateFormat time = new SimpleDateFormat("hh:mm:ss a");
	        out.println("Current Date : " + today + "<br>" + "Date: " + date.format(today) + "<br>" + "Time: " + time.format(today));    
  			%>
		</div>
		<hr>
	</div>
</body>
</html>
