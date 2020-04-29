<?php
include 'conn.php';
$Patent_ID=$_POST['Patent_ID'];
$Application_Office_ID=$_POST['Application_Office_ID'];
$Examiner_ID=$_POST['Examiner_ID'];
$Fees_Paid=$_POST['Fees_Paid'];
$Renewal_Status=$_POST['Renewal_Status'];
$conn->query("INSERT into Renewal_Applications(Patent_ID,Application_Office_ID,Examiner_ID,Fees_Paid,Renewal_Status) values('".$Patent_ID."','".$Application_Office_ID."','".$Examiner_ID."','".$Fees_Paid."','".$Renewal_Status."')");

?>