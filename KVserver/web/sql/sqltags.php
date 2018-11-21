





<?php


	$dbhost = '******';
	$dbuser = '******';
	$dbpwd = '******';
	$dbdb = '******';
	


	$con = mysqli_connect($dbhost, $dbuser, $dbpwd, $dbdb);

	if(!$con)
	{
		echo "Tietokantaan yhdistäminen ei onnistu" .mysqli_connect_error();
		die (' : ' .mysqli_connect_error());
	}
		

		$qu = "SELECT nimi, mac FROM ruuvit;";
		$query = mysqli_query($con, $qu);
		
		if(!$query)
		{
			echo "Tietokantakyseli ei onnistu" .mysqli_error($con);
			die (' : ' .mysqli_connect_error($con));
		}


				
			?>



<table class="data-table">
		<caption class="title">Skannattavat tagit</caption>
		<thead>
			<tr>
				<th> Nimi </th>
				<th> Mac </th>
			</tr>
		</thead>
			<tbody>
			<?php
							
					
					while($row = mysqli_fetch_assoc($query))
					echo '<tr>
							<td>'.$row['nimi'].'</td>
							<td>'.$row['mac'].'</td>
						</tr>';
					
			?>

			</tbody>
		</table>