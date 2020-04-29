<?php

include 'conn.php';
$Validation_States=$_POST['Validation_States'];
$Patent_ID=$_POST['Patent_ID'];
$query="UPDATE Patents SET Validation_States = '".$Validation_States."' WHERE Patent_ID = '".$Patent_ID."'";
$statement=$conn->prepare($query);
$statement->execute();
echo json_encode("Updated");

?>