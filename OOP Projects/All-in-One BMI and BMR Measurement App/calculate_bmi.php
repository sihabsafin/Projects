<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $id = htmlspecialchars($_POST['id']);
    $weight = floatval($_POST['weight']);
    $height = floatval($_POST['height']);
    $gender = htmlspecialchars($_POST['gender']);

   
    $heightInMeters = $height / 100;

    $bmi = $weight / ($heightInMeters * $heightInMeters);

    if ($bmi < 18.5) {
        $status = 'Underweight';
    } elseif ($bmi < 24.9) {
        $status = 'Normal weight';
    } elseif ($bmi < 29.9) {
        $status = 'Overweight';
    } else {
        $status = 'Obesity';
    }

    echo "<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>BMI Results</title>
        <link rel='stylesheet' href='styles.css'>
    </head>
    <body>
        <div class='result'>
            <h3>Results:</h3>
            <p>Name: $name</p>
            <p>ID: $id</p>
            <p>Gender: $gender</p>
            <p>BMI: " . number_format($bmi, 2) . "</p>
            <p>Status: $status</p>
            <a href='index.html'>Go Back</a>
        </div>
    </body>
    </html>";
}
?>
