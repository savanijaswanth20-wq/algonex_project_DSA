<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Python Revision Banner</title>

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap" rel="stylesheet">

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:#05070d;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    overflow:hidden;
    font-family:Orbitron,sans-serif;
}

.banner{
    width:1400px;
    height:800px;
    position:relative;
    background:
    radial-gradient(circle at center,#081a33 0%,#05070d 70%);
    overflow:hidden;
}

/* Circuit Lines */

.banner::before,
.banner::after{
    content:"";
    position:absolute;
    width:450px;
    height:450px;
    border:2px solid rgba(0,255,255,.15);
    filter:drop-shadow(0 0 15px cyan);
}

.banner::before{
    left:-220px;
    top:150px;
    transform:rotate(45deg);
}

.banner::after{
    right:-220px;
    top:150px;
    transform:rotate(-45deg);
}

/* Python */

.python{
    text-align:center;
    font-size:155px;
    font-weight:900;
    color:#29b6ff;

    text-shadow:
    0 0 5px #00d5ff,
    0 0 15px #00d5ff,
    0 0 35px #00d5ff,
    0 8px 0 #00395f;
}

/* Revision */

.revision{
    text-align:center;
    font-size:135px;
    margin-top:-20px;
    color:#ffd000;

    text-shadow:
    0 0 10px #ffcc00,
    0 0 30px #ffcc00,
    0 8px 0 #6f5000;
}

/* Python Logo */

.logo{
    font-size:120px;
    text-align:center;
    margin-top:30px;
}

/* Brackets */

.left,
.right{
    position:absolute;
    top:300px;
    font-size:170px;
    color:#00d5ff;

    text-shadow:0 0 20px cyan;
}

.left{
    left:50px;
}

.right{
    right:50px;
}

/* Bottom */

.bottom{
    position:absolute;
    bottom:70px;
    width:100%;
    text-align:center;
    color:white;
    letter-spacing:8px;
    font-size:26px;
}

.bottom span{
    color:#00d5ff;
}

/* Line */

.line{
    width:80%;
    height:4px;
    margin:auto;
    margin-top:30px;
    background:linear-gradient(90deg,transparent,#00d5ff,transparent);
    box-shadow:0 0 15px cyan;
}

/* Animation */

.python,
.revision,
.logo{
    animation:glow 2s infinite alternate;
}

@keyframes glow{

0%{
transform:scale(1);
}

100%{
transform:scale(1.03);
}
}
</style>

</head>

<body>

<div class="banner">

<div class="logo">🐍</div>

<div class="left">&lt;</div>
<div class="right">&gt;</div>

<div class="python">
PYTHON
</div>

<div class="revision">
REVISION
</div>

<div class="bottom">

<span>&lt;/&gt;</span>

LEARN • PRACTICE • MASTER • SUCCEED

<span>{ }</span>

<div class="line"></div>

</div>

</div>

</body>
</html>
