
<!DOCTYPE html>
<html>
	<head>
		<script src="jquery331min.js"></script>
		<script>
			
			var intervalVar = "None";
			
			function log(){
				$("#sqlquery").load("sql/sqllog.php");	
			}
			
			function views(x){
				if(x==1)
				{
					$("#buttons").load("sql/viewalllog.php");
				}
				if(x==2)
				{
					$("#buttons").load("sql/viewonly6.php");
				}
				if(x==0)
				{
					$("#buttons").empty();
				}
			}
			
			
			function logall(){
				$("#sqlquery").load("sql/sqllogall.php");
			}
			
			
			function Taglog(){
				$("#sqlquery").load("sql/sqltags.php");
				
			}
			
			
			
			function call(d){
				
				if (intervalVar != "None")
				{
					clearInterval(intervalVar);
					d = setInterval(d, 100);
					intervalVar = d;
				}
				else
				{
					d = setInterval(d, 500);
					intervalVar = d;
				}
				
				
			}
			

	
				


			//$(document).ready(function(){
					//$("#buttons").empty();
			//});
		</script>
		<Title> Kulunvalvonta </title>
		<style type="text/css">
			body
			{
				font-size: 15px;
				color: #343d44;
				font-family: "seogoe-ui", "open_sans", tahoma, arial;
				padding: 0;
				margin: 0;
			}
			table
			{
				margin: auto;
				font-family: "Lucida Sans Unicode", "Lucida Grande", "Segoe Ui";
				font-size: 12px;
			}
			h1
			{
				margin 25px; auto 0;
				text-align: center;
				text-transform: upprercase;
				font-size: 25px;
			}
			h2
			{
				text-align: center;
				float: center;
			}
			h3
			{
				text-align: center;
				float: center;
				margin: 5px;
				
				
			}
			table td
			{
				transition: all .5s;
			}
			.data-table
			{
				border-collapse: collapse;
				font-size: 14px;
				min-width: 537px;
			}
			.data-table th,
			.data-table td
			{
				border: 1px solid #eledff;
				padding: 7px 17px;
			}
			.data-table caption
			{
				margin 7px;
			}
			.data-table thead th
			{
				background-color: #508abb;
				color:#FFFFFF;
				border-color: #6ea1cc !important;
				text-transform: uppercase;
			}
			.data-table tbody td
			{
				color: #353535;
			}
			.data-table tbody td:first-child,
			.data-table tbody td:nth-child(4),
			.data-table tbody td:last-child
			{
				text-align: center;
			}
			.data-table tbody tr:nth-child(odd) td
			{
				background-color: #f4fbff;
			}
			.data-table tbody tr:hover td
			{
				background-color: #ffffa2;
				border-color: #ffff0f;
			}
			.data-table tfoot th
			{
				background-color: #e5f5ff;
				text-align: right;
			}
			.data-table tfoot th:first-child
			{
				text-align: left;
			}
			.data-table tbody td: empty
			{
				background-color: #ffcccc;
			}
			
			.mainb
			{
				padding: 12px 28px;
				border-radius: 18px;
				border: 1px gray solid;
			}
			.mainb:hover
			{
				background-color: #e5e5e5;
			}
			.button
			{
				border-radius: 8px;
				background-color: lightgreen;
			}
			.button:hover
			{
				background-color: springgreen;
			}
		</style>
	</head>
	
	
	<body>
		<h1> Kulunvalvonta </h1>
		<h2>
		<button class="mainb" onclick="call(log), views(1)">Tapahtumaloki</button>
		<button class="mainb" onclick="call(Taglog), views(0)">Skannattavat tagit</button>
		</h2>
		<h3>
		<div id="buttons"> </div>
		</h3>
		
		<div id="sqlquery">
		<script> call(log); views(1); </script>
		</div>
	</body>
</html>

