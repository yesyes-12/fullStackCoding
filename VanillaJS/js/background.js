const images = [
  "https://t4.ftcdn.net/jpg/04/61/47/03/360_F_461470323_6TMQSkCCs9XQoTtyer8VCsFypxwRiDGU.jpg",
  "https://blog.kakaocdn.net/dn/cNZBMB/btsBitMVBRv/G5PYIJR8zQTRaMIok1YPw0/img.webp",
  "https://newsroom.posco.com/kr/wp-content/uploads/2024/08/PC_3840x2160.jpg",
];

const chosenImage = images[Math.floor(Math.random() * images.length)];
const bgImage = document.createElement("img");

bgImage.src = `${chosenImage}`;
document.body.appendChild(bgImage);
