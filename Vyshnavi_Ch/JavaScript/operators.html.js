<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        let side=10;
        console.log("area:",side * side);
        console.log("perimeter:",4 * side);

        let length = 10;
        let width = 20;

        console.log("area: ",length * width );
        console.log("perimeter:", 2 *(length + width));

        let radius = 20;
        const PI = 3.14;
        console.log("Area of a circle: ",PI * radius ** 2);
        console.log("perimeter of a circle",2 * PI * radius );

        // print volume of a sphere and surface area of a sphere

        let height = 10;
        let base= 15;  
        // print area and perimeter of equilateral triangle

        let n = Number(prompt("Enter a number"));
        console.log(n % 2 == 0, "The number is even");
        console.log(n % 2 == 1, "The number is odd");
        if (n % 2 == 0) {
            console.log("The number is even")
        } else {
            console.log("The number is odd")
            
        }

    </script> 
</body>
</html>