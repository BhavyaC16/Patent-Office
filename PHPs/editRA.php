<?php

include 'conn.php';
$Renewal_Status=$_POST['Renewal_Status'];
$Renewal_Application_ID=$_POST['Renewal_Application_ID'];
$query="UPDATE Renewal_Applications SET Renewal_Status = '".$Renewal_Status."' WHERE Renewal_Application_ID = '".$Renewal_Application_ID."'";
$statement=$conn->prepare($query);
$statement->execute();
echo json_encode("Update");

?>