<?php
// test.php
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>GoDaddy Test File - Meowdy Partner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
            background-color: #ffffff; /* white background */
        }
        .meowdy {
            font-size: 3em;
            font-weight: bold;
            color: black;
            background-color: saddlebrown;
            padding: 0.3em 0.5em;
            border-radius: 8px;
            display: inline-block;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 1.4em;
            color: #333;
            margin-top: 5px;
            margin-bottom: 20px;
        }
        .image-container {
            text-align: center !important; /* Force center */
            margin-bottom: 40px;
        }
        .cowboy-cat {
            display: inline-block !important; /* Avoid phpinfo overriding */
            max-width: 400px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .phpinfo-container {
            text-align: left;
            margin-top: 40px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>

    <h1 class="meowdy">Meowdy partner</h1>
    <div class="subtitle">this is a GoDaddy test file</div>

    <!-- Cowboy cat image -->
    <div class="image-container">
        <img class="cowboy-cat" src="https://media.istockphoto.com/id/896916940/photo/cat-cowboy-on-a-horse.jpg?s=612x612&w=0&k=20&c=vWP2EmHTDwgLnTXYyoBEmr3AD9R3dQcmiUbK-HNIbak=" alt="Cowboy Cat on a Horse">
    </div>

    <div class="phpinfo-container">
        <?php phpinfo(); ?>
    </div>

</body>
</html>
