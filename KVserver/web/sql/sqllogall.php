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


		$qu = "SELECT ruuvi, direction FROM direction";
		$query = mysqli_query($con, $qu);
		
		if(!$query)
		{
			echo "Tietokantakyseli ei onnistu" .mysqli_error($con);
			die (' : ' .mysqli_connect_error($con));
		}


				
			?>

<table class="data-table">
		<caption class="title">Koko tapahtumaloki</caption>
		<thead>
			<tr>
				<th> Nimi </th>
				<th> suunta </th>
			</tr>
		</thead>
			<tbody>
			<?php
							
					
					while($row = mysqli_fetch_assoc($query))
					echo '<tr>
							<td>'.$row['ruuvi'].'</td>
							<td>'.$row['direction'].'</td>
						</tr>';
				
			?>
			</tbody>
		</table>