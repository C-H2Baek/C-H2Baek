const PI2 = Math.PI * 2;

const COLORS = [
  '#4b45ab',
  '#554fb8',
  '#605ac7',
  '#2a91a8',
  '#2e9ab2',
  '#32a5bf',
  '#81b144',
  '#85b944',
  '#8fc549',
  '#808000',
  '#e0af27',
  '#fec72e',
  '#bf342d',
  '#ca3931',
  '#d7423a',
]

export class Polygon{
  constructor(x, y, radius, sides){
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.sides = sides;
    this.rotate = 0;
  }

  animate(ctx, moveX){
    ctx.save();
    //사각형에 색을 넣을때는 주석
    // ctx.fillStyle = '#000';
    // ctx.beginPath();

    const angle = PI2 / this.sides;
    const angle2 = PI2 / 4;

    ctx.translate(this.x, this.y);

    //도형 or 점일때
    // this.rotate -= moveX * 0.008;
    //사각형에 색칠할때
    this.rotate -= moveX * .008;
    ctx.rotate(this.rotate);
    
    for(let i = 0; i < this.sides; i++){
      const x = this.radius * Math.cos(angle * i);
      const y = this.radius * Math.sin(angle * i);
      

      /////////////////////////////////////////////////////////사각형으로만드는 코드 시작
      ctx.save();
      //사각형에 배열에 담긴 색을 넣고싶을때추가
      ctx.fillStyle = COLORS[i];
      ctx.translate(x,y);
      ctx.rotate(((360 / this.sides) * i + 45 ) * Math.PI / 180);
      ctx.beginPath();
      for(let j = 0; j < 4; j++){
        const x2 = 80 * Math.cos(angle2 * j);
        const y2 = 80 * Math.sin(angle2 * j);
        (j == 0) ? ctx.moveTo(x2, y2) : ctx.lineTo(x2, y2);
      }
      ctx.fill();
      ctx.closePath();
      ctx.restore();
      /////////////////////////////////////////////////////////사각형으로만드는 코드 끝
      

      // (i == 0) ? ctx.moveTo(x,y) : ctx.lineTo(x,y); //도형으로 만드는 for문

      // ctx.beginPath();  //도형 채우는게 아니라 점만 있도록
      // ctx.arc(x, y, 30, 0, PI2, false); //도형 채우는게 아니라 점만 있도록
      // ctx.fill(); //도형 채우는게 아니라 점만 있도록

    }

    // ctx.fill(); //도형으로 만드는 for문
    // ctx.closePath();  //도형으로 만드는 for문
    ctx.restore();
  }
}