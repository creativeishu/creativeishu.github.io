<?php

$title = $_POST["title"];
$input = $_POST["input"];


$cmd = "python summary_centroid.py ".'"'.$title.'"'." ".'"'.$input.'"';

$result = shell_exec($cmd);
$result_json = array("result" => $result);
echo json_encode($result_json);
?>