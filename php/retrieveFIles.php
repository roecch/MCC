<?php
$playersImgArray = array();

foreach (glob("../static/images/players/*") as $filename) {
    $playersImgArray[strtok(substr($filename, strrpos($filename, "/") + 1), '.')] = $filename;

}

$json = json_encode($playersImgArray);
$list = file_put_contents("../static/list_of_images.json", $json);

?>