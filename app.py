<!DOCTYPE html>
<html>
<head>
    <title>{{ training_topic.name }}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .container h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        .container img {
            width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .container p {
            font-size: 1.2rem;
            line-height: 1.6;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ training_topic.name }}</h1>
        <img src="{{ training_topic.image_url }}" alt="{{ training_topic.name }}">
        <p>{{ training_topic.description }}</p>
    </div>
</body>
</html>
