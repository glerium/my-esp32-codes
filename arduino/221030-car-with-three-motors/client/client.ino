int motor1=3, motor2=4, steer=0;
void stop();
void move();

void setup() {
  Serial.begin(115200,SERIAL_8N1,22,23);

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
  // Serial.begin(115200);
}

void loop() {
  if(Serial.available()){
    char in=Serial.read();
    if(in==1){
      move();
    }else if(in==2){
      stop();
    }
  }
  delay(50);
}

void move(){
  ledcWrite(motor1, 0);
  ledcWrite(motor2, 1023);
  pinMode(33, OUTPUT);
}
void stop(){
  ledcWrite(motor1, 0);
  ledcWrite(motor2, 0);
}