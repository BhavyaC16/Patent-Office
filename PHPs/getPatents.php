<?php
include 'conn.php';
$sql=$conn->query('SELECT * FROM Patents ORDER BY Patentee_ID');
$res=array();
while($row=$sql->FETCH_ASSOC()){
    $res[]=$row;
}
echo json_encode($res);
?>