<?php 
	$db_host = 'localhost';
	$db_user = 'root'; // User Server
	$db_pass = ''; // Password Server
	$db_name = 'db_sistempemantauanv4'; // Nama Database

	$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
	if (!$conn) {
		die ('Gagal terhubung MySQL: ' . mysqli_connect_error());	
	}
?>