<?php
include 'conn.php';
$sql=$conn->query('SELECT * FROM Renewal_Applications ORDER BY Examiner_ID');
$res=array();
while($row=$sql->FETCH_ASSOC()){
    $res[]=$row;
}
echo json_encode($res);
?>