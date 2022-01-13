import {Polygon} from './1_Rotate_Polygon.js'

class App{
  constructor(){
    this.canvas = document.createElement('canvas');
    document.body.appendChild(this.canvas);
    this.ctx = this.canvas.getContext('2d');

    this.pixelRatio = window.devicePixelRatio > 1 ? 2 : 1;

    window.addEventListener('resize', this.resize.bind(this), false);
    this.resize();

    this.isDown = false;
    this.moveX = 0;
    this.offsetX = 0;
    document.addEventListener('pointerdown', this.onDown.bind(this), false);
    document.addEventListener('pointermove', this.onMove.bind(this), false);
    document.addEventListener('pointerup', this.onUp.bind(this), false);

    window.requestAnimationFrame(this.animate.bind(this));
  }

  resize(){
    this.stageWidth = document.body.clientWidth;
    this.stageHeight = document.body.clientHeight;

    this.canvas.width = this.stageWidth * this.pixelRatio;
    this.canvas.height= this.stageHeight * this.pixelRatio;
    this.ctx.scale(this.pixelRatio, this.pixelRatio);

    //도형의 사이즈 조절
    this.Polygon = new Polygon(
      this.stageWidth / 2,
      // this.stageHeight / 2,  //도형 또는 점일때
      this.stageHeight / + (this.stageHeight / 4),  //사각형 & 화면 반만 채울때
      this.stageHeight / 1.5,
      15 //<<도형의 꼭지점 개수 설정 ex.3이면 삼각형
    )
  }

  animate(){
    window.requestAnimationFrame(this.animate.bind(this));

    this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);
    
    this.moveX *= 0.92;
    this.Polygon.animate(this.ctx, this.moveX);
  }

  onDown(e){
    this.isDown = true;
    this.moveX = 0 ;
    this.offsetX = e.clientX;
  }

  onMove(e){
    if(this.isDown){
      this.moveX = e.clientX - this.offsetX;
      this.offsetX = e.clientX;
    }
  }

  onUp(e){  
    this.isDown = false;
  }
}

window.onload = () => {
  new App();
}