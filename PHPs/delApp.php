<?php
include 'conn.php';

$Renewal_Application_ID=$_POST['Renewal_Application_ID'];


$conn->query("delete from Renewal_Applications where Renewal_Application_ID='".$Renewal_Application_ID."'");
echo("DELETED");



?>