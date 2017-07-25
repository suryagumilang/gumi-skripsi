<?php
include("connect.php");

$query = "SELECT * FROM history";
$result=mysqli_query($conn,$query);

while ($row=mysqli_fetch_assoc($result)) {
	echo"
			<tr>
				<td colspan='3'>".$row["nama_ka"]."</td>
				<td>".$row["no_ka"]."</td>
				<td>".$row["is_stasiun"]."</td>
				<td colspan='4'>".$row["nama_lokasi"]."</td>
				<td>".$row["real_ls"]."</td>
				<td>".$row["real_bt"]."</td>
				<td colspan='2'>".$row["kota_kab"]."</td>
				<td colspan='2'>".$row["provinsi"]."</td>
				<td colspan='2'>".$row["waktu"]."</td>
			</tr>
	";
}