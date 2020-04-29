<?php
include 'conn.php';
$Title=$_POST['Title'];
$Subject=$_POST['Subject'];
$Patent_Examiner_ID=$_POST['Patent_Examiner_ID'];
$Inventor=$_POST['Inventor'];
$Expense_in_US=$_POST['Expense_in_US'];
$Patent_Attorney_ID=$_POST['Patent_Attorney_ID'];
$Opposition_Filled_Status=$_POST['Opposition_Filled_Status'];
$Filling_Language=$_POST['Filling_Language'];
$Renewal_Status=$_POST['Renewal_Status'];
$conn->query("INSERT into Pending(Title,Subject,Patent_Examiner_ID,Inventor,Expense_in_US,Patent_Attorney_ID,Opposition_Filled_Status,Filling_Language) values('".$Title."','".$Subject."','".$Patent_Examiner_ID."','".$Inventor."','".$Expense_in_US."','".$Patent_Attorney_ID."','".$Opposition_Filled_Status."','".$Filling_Language."')");

?>