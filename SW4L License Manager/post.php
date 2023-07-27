<?php
include_once('config.php');
if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $macAddress = isset($_POST['macAddress']) ? mysqli_real_escape_string($conn, $_POST['macAddress']) : "";
    $licenseFeature = isset($_POST['licenseFeature']) ? mysqli_real_escape_string($conn, $_POST['licenseFeature']) : "";
    $sql = "SELECT valid_until, status FROM LICENSE.LICENSES WHERE mac_address = '{$macAddress}' AND license_feature = '{$licenseFeature}'";
	$data_query = mysqli_query($conn, $sql) or die (mysqli_error($conn));

    if (mysqli_num_rows($data_query) != 0) {
		$result = array();

        while ($r = mysqli_fetch_array($data_query)) {
			extract($r);
			$result[] = array("valid_until" => $r["valid_until"], "status" => $r["status"]);
        }
        $json = array("status" => 1, "info" => $result);
    }

    else {
    $json = array("status" => 0, "error" => "Data not found.");
    }
}

else {
    $json = array("status" => 0, "error" => "Request method not accepted!");
}

@mysqli_close($conn);

header('Content-type: application/json');
echo json_encode($json);