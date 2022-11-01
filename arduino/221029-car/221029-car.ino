//小车行进比赛代码
const int T_LEFT=7, T_FORWARD=21, T_RIGHT=33;
// const int T_LEFT=50, T_FORWARD=300, T_RIGHT=550;
int motor1=3, motor2=4, steer=0;
void turn_ms(int pos, int ms);
void turn(int pos);
void stop();
void move(bool forward=true, int speed=300);

void setup() {
  pinMode(26, OUTPUT);
  ledcAttachPin(26, motor1);
  ledcSetup(motor1, 50, 10);
  pinMode(27, OUTPUT);
  ledcAttachPin(27, motor2);
  ledcSetup(motor2, 50, 10);
  pinMode(15, OUTPUT);
  ledcAttachPin(15, steer);
  ledcSetup(steer, 50, 8);
  ledcWrite(steer, 20);
  pinMode(35, INPUT);
  turn(T_FORWARD);
  // turn(T_RIGHT);
}

void loop() {
  while(digitalRead(35));  
  move(true); delay(1200);
  turn_ms(33,700);
  turn(25); delay(400);
  // turn(T_FORWARD);
  turn(30); delay(1000);
  // turn_ms(33,450);
  turn(T_FORWARD); delay(800);
  turn_ms(T_RIGHT,700); delay(800);
  turn_ms(T_FORWARD,600);
  delay(1000);
  // delay(2500);
  // delay(500);
  // turn_ms(28,700,800);
  // delay(1500);
  // turn_ms(27,700,700);
  // delay(1000);
  // turn_ms(27,700,700);
  // delay(800);
  stop();
  // turn(T_LEFT);
  // delay(2000);
  // turn(T_RIGHT);
  // delay(2000);
}

void turn_ms(int pos, int ms){   //逐渐转向，ms1, ms2为时间
  int from = ledcRead(steer);
  if(pos>from){
    int delta = ms / (pos-from);
    int i;
    for(i=from+1; i<=pos; i++){
      ledcWrite(steer, i);
      delay(delta);
    }
  }else{
    int delta = ms / (from-pos);
    int i;
    for(i=from+1; i>=pos; i--){
      ledcWrite(steer, i);
      delay(delta);
    }
  }
}
void turn(int pos){
  ledcWrite(steer, pos);
}
void stop(){
  ledcWrite(motor1, 0);
  ledcWrite(motor2, 0);
}
void move(bool forward, int speed){
  if(!forward){
    ledcWrite(motor1, 0);
    ledcWrite(motor2, speed);
  }else{
    ledcWrite(motor1, speed);
    ledcWrite(motor2, 0);
  }
}
