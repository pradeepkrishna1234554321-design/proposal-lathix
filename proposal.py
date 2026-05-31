from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import threading
import socket

HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>For Lathika Sri ❤️</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    height: 100vh;
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
    background: radial-gradient(circle at top, #ff5fa2, #2b0033 45%, #050008);
    color: white;
    text-align: center;
}

.title {
    margin-top: 45px;
    font-size: 42px;
    color: #ffd6e8;
    text-shadow: 0 0 15px #ff1493, 0 0 35px #ff69b4;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px pink; }
    to { text-shadow: 0 0 35px #ff1493, 0 0 60px hotpink; }
}

.subtitle {
    margin-top: 10px;
    font-size: 20px;
    color: #ffe6f2;
}

#envelopeBox {
    position: absolute;
    top: 52%;
    left: 50%;
    transform: translate(-50%, -50%);
    cursor: pointer;
    animation: float 2s infinite ease-in-out;
}

@keyframes float {
    0%,100% { transform: translate(-50%, -50%); }
    50% { transform: translate(-50%, -58%); }
}

.envelope {
    width: 260px;
    height: 170px;
    background: linear-gradient(135deg, #ffb6d9, #ff4fa3);
    border-radius: 15px;
    position: relative;
    box-shadow: 0 0 40px #ff69b4;
}

.envelope:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    border-left: 130px solid transparent;
    border-right: 130px solid transparent;
    border-top: 95px solid #ffd1e8;
}

.envelope:after {
    content: "❤️";
    position: absolute;
    top: 65px;
    left: 105px;
    font-size: 45px;
}

.clickText {
    margin-top: 25px;
    font-size: 24px;
    color: gold;
    text-shadow: 0 0 15px gold;
}

#letterScreen {
    display: none;
    height: 100vh;
    justify-content: center;
    align-items: center;
}

.paper {
    width: 760px;
    max-width: 90%;
    min-height: 520px;
    background: #fff8ee;
    color: #3b1f2b;
    padding: 38px;
    border-radius: 18px;
    box-shadow: 0 0 45px pink;
    font-family: Georgia, serif;
    animation: slideUp 1.5s ease;
    position: relative;
    z-index: 5;
}

@keyframes slideUp {
    from { transform: translateY(250px) scale(0.7); opacity: 0; }
    to { transform: translateY(0) scale(1); opacity: 1; }
}

.paper h1 {
    color: #d4145a;
    margin-bottom: 20px;
    font-size: 34px;
}

#proposalText {
    font-size: 21px;
    line-height: 1.65;
    text-align: left;
}

#proposalText {
    font-size: 20px;
    line-height: 1.7;
    text-align: left;
    height: 320px;
    overflow-y: auto;
    scroll-behavior: smooth;
}

#proposalText p {
    margin-bottom: 12px;
    opacity: 0;
    animation: slideUp 1s forwards;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.heart {
    position: absolute;
    pointer-events: none;
    animation: fall linear forwards;
    z-index: 1;
}

@keyframes fall {
    from {
        transform: translateY(-60px) rotate(0deg);
        opacity: 1;
    }
    to {
        transform: translateY(110vh) rotate(360deg);
        opacity: 0;
    }
}

.star {
    position: absolute;
    background: white;
    border-radius: 50%;
    animation: twinkle 2s infinite alternate;
}

@keyframes twinkle {
    from { opacity: 0.2; }
    to { opacity: 1; }
}

.finalBox {
    margin-top: 25px;
    text-align: center;
}

.finalQuestion {
    font-size: 34px;
    color: #d4145a;
    font-weight: bold;
}

.btn {
    margin: 18px 12px;
    padding: 13px 32px;
    border: none;
    border-radius: 30px;
    font-size: 22px;
    cursor: pointer;
    color: white;
}

.yes {
    background: linear-gradient(45deg, #ff1493, #ff69b4);
    box-shadow: 0 0 20px #ff69b4;
}

.no {
    background: #555;
    position: relative;
}

#mobilePrompt {
    position: absolute;
    top: 18px;
    right: 18px;
    width: 250px;
    padding: 16px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 18px;
    backdrop-filter: blur(10px);
    color: #fff;
    box-shadow: 0 0 30px rgba(255, 105, 180, 0.25);
    text-align: center;
}

#mobilePrompt img {
    margin: 12px 0 8px;
    width: 100%;
    height: auto;
    border-radius: 18px;
    border: 2px solid rgba(255, 255, 255, 0.4);
}

.mobileLink {
    font-size: 13px;
    word-break: break-all;
    color: #ffe6f2;
    margin-top: 6px;
}

#happyScreen {
    display: none;
    height: 100vh;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    color: gold;
    text-shadow: 0 0 25px gold, 0 0 50px hotpink;
}

#happyScreen h1 {
    font-size: 52px;
}

#happyScreen h2 {
    margin-top: 25px;
    font-size: 32px;
    color: #ffd6e8;
}
</style>
</head>

<body>

<h1 class="title">A Letter From My Heart 💌</h1>
<p class="subtitle">For the most special person, Lathika Sri ❤️</p>

<div id="mobilePrompt">
    <div>Scan to open on mobile</div>
    <img src="https://api.qrserver.com/v1/create-qr-code/?size=240x240&data={MOBILE_LINK}" alt="Mobile QR Code">
    <div class="mobileLink">{MOBILE_LINK}</div>
</div>

<div id="envelopeBox" onclick="openLetter()">
    <div class="envelope"></div>
    <div class="clickText">Click the love letter</div>
</div>

<div id="letterScreen">
    <div class="paper">
        <h1>Dear Lathika Sri ❤️</h1>
        <div id="proposalText"></div>
        <div id="finalBox" class="finalBox"></div>
    </div>
</div>

<div id="happyScreen">
    <h1>She Said YES! ❤️💍</h1>
    <h2>I will choose you in every lifetime, Lathika Sri ❤️</h2>
</div>

<audio id="music" loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>

<script>
const lines = [
"Before I met you, every day felt ordinary...",
"But your smile turned simple moments into unforgettable memories.",
"Your kindness, your laughter, and your beautiful heart became my favorite part of every day.",
"When life feels difficult, just thinking about you makes everything lighter.",
"I don't promise a perfect life...",
"But I promise honesty, respect, care, support, and loyalty through every moment.",
"When I imagine my future, I see your smile beside me.",
"You are more precious than any achievement, trophy, or dream I have ever chased.",
"Among billions of people, my heart chose only one person...",
"And that person is you, Lathika Sri ❤️",
"So today, with all the sincerity in my heart...",
"I want to ask you something very special..."
];

let index = 0;

function openLetter() {
    document.getElementById("envelopeBox").style.display = "none";
    document.getElementById("letterScreen").style.display = "flex";
    document.getElementById("music").play();
    showLine();
}

function showLine() {
    if (index < lines.length) {
        document.getElementById("proposalText").innerHTML += "<p>" + lines[index] + "</p>";
        index++;
        setTimeout(showLine, 1900);
    } else {
        showFinalQuestion();
    }
}

function showFinalQuestion() {
    document.getElementById("finalBox").innerHTML = `
        <div class="finalQuestion">Lathika Sri, will you be mine forever? 💍❤️</div>
        <button class="btn yes" onclick="sayYes()">Yes ❤️</button>
        <button class="btn no" onmouseover="moveNo(this)">No 😅</button>
    `;
}

function sayYes() {
    document.getElementById("letterScreen").style.display = "none";
    document.getElementById("happyScreen").style.display = "flex";
    setInterval(createHeart, 80);
}

function moveNo(btn) {
    btn.style.left = Math.random() * 180 - 90 + "px";
    btn.style.top = Math.random() * 120 - 60 + "px";
}

function createHeart() {
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = Math.random() > 0.5 ? "❤️" : "💖";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (18 + Math.random() * 35) + "px";
    heart.style.animationDuration = (3 + Math.random() * 4) + "s";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 7000);
}

function createStar() {
    let star = document.createElement("div");
    star.className = "star";
    star.style.left = Math.random() * 100 + "vw";
    star.style.top = Math.random() * 100 + "vh";
    let size = Math.random() * 3 + 1;
    star.style.width = size + "px";
    star.style.height = size + "px";
    document.body.appendChild(star);
}

for (let i = 0; i < 120; i++) createStar();
setInterval(createHeart, 250);
</script>

</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        page = HTML.replace("{MOBILE_LINK}", mobile_link)
        self.wfile.write(page.encode("utf-8"))

def open_browser():
    webbrowser.open("http://localhost:8000")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

ip = get_ip()
mobile_link = f"http://{ip}:8000"

server = HTTPServer(("0.0.0.0", 8000), Handler)
threading.Timer(1, open_browser).start()

print("❤️ Proposal is running...")
print(f"Mobile Link: {mobile_link}")

server.serve_forever()