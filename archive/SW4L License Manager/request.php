<?php
$_GET = array();

foreach($argv as $key => $pair) {
    if ($key == 0) {
        continue;
    }

    list($key, $value) = explode(":", $pair);
    $_GET[$key] = $value;
}

$servername = "localhost";
$username = "";
$password = "";
$database = "LICENSE";

$query_1 = "SELECT key_ FROM LICENSE.LICENSES WHERE mac = ${mac} AND email = ${email}";
$query_2 = "SELECT until FROM LICENSE.LICENSES WHERE mac = ${mac} AND email = ${email}";
$query_3 = "SELECT mac FROM LICENSE.LICENSES WHERE key_ = ${key_} AND email = ${email}";
$query_4_1 = "SET SQL_SAFE_UPDATES = 0;";
$query_4_2 = "UPDATE LICENSE.LICENSES SET mac = REPLACE(mac, %s, %s);";
$query_4_3 = "SET SQL_SAFE_UPDATES = 1;";
$query_5 = "SELECT * FROM LICENSE.LICENSES WHERE email = ${email}";

$mysqli = new mysqli($servername, $username, $password, $database);

if ($mysqli -> connect_errno) {
    echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
    exit();
}

if ($result = $mysqli -> query($query_1)) {
    while($row = mysqli_fetch_array($result)) {
        print_r($row);
    }
    $result -> free_result();
}

?>