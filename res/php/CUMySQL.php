<?php
$conn = null;
function CUMySQL_connect()
{ //连接MySQL
	global $conn;
	if ($conn) {
		return true;
	}
	$servername = "127.0.0.1";
	$username = "root";
	$password = "root";
	$dbname = "tkwebs";

	// 创建连接
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
		$conn = null;
		ob_clean();
		return false;
	} else {
		return true;
	}
}
function CUMySQL_disconnect()
{ //断开MySQL连接
	global $conn;
	if ($conn) {
		mysqli_close($conn);
		$conn = null;
	}
}
function CUMySQL_execute()
{ //执行MySQL，参数1填写SQL语句，参数2.....n填写数据(SQL语句里用?n代替要写入的变量)
	//?n = 给内容带上 '' !n = 不给内容带上 ''
	global $conn;
	$arrayargs = func_num_args();
	$numargs = 0;
	$arg_list = func_get_args();
	$isarray = true;
	$sql  = $arg_list[0];
	$numargs += substr_count($sql, "?");
	$numargs += substr_count($sql, "!");
	if ($numargs < ($arrayargs - 1)) {
		$isarray = $arg_list[$arrayargs - 1];
	}
	for ($i = 1; $i < $arrayargs; $i++) {
		if (strpos($sql, "?") != false) {
			$sql = str_replace("?" . $i, "'" . mysqli_real_escape_string($conn, $arg_list[$i]) . "'", $sql);
		} else if (strpos($sql, "!") != false) {
			$sql = str_replace("!" . $i,  mysqli_real_escape_string($conn, $arg_list[$i]), $sql);
		}
	}
	$result = mysqli_query($conn, $sql);
	if (mysqli_affected_rows($conn) > 0) {
		if ($isarray == true) {
			$arraylist = array();
			for ($n = 0; $n < mysqli_num_rows($result); $n++) {
				$arraylist[$n] = mysqli_fetch_assoc($result);
			}
			
			return $arraylist;
		} else {
			return  $result;
		}
	} else {
        echo mysqli_error($conn);
		return false;
	}
}
