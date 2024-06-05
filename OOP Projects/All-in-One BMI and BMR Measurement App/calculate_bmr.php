<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $height = floatval($_POST['height']);
    $weight = floatval($_POST['weight']);
    $age = intval($_POST['age']);
    $gender = htmlspecialchars($_POST['gender']);

    if ($gender == 'male') {
        $bmr = 88.362 + (13.397 * $weight) + (4.799 * $height) - (5.677 * $age);
    } else {
        $bmr = 447.593 + (9.247 * $weight) + (3.098 * $height) - (4.330 * $age);
    }

    echo "<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>BMR Results</title>
        <link rel='stylesheet' href='styles.css'>
    </head>
    <body>
        <div class='result'>
            <h3>Your BMR is: " . number_format($bmr, 2) . " calories/day</h3>
            
            <a href='index.html'>Go Back</a>
        </div>
    </body>
    </html>";
}
?>
