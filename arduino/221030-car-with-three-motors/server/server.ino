int motor1=3, motor2=4, steer=0;
void stop();
void move();

void setup() {
  Serial1.begin(115200,SERIAL_8N1,22,23);
  Serial2.begin(115200,SERIAL_8N1,19,21);

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

  pinMode(35, INPUT); //key1
}

void loop() {
  while(digitalRead(35));
  move();
  delay(300);
  stop();
}

void move(){
  ledcWrite(motor1, 0);
  ledcWrite(motor2, 1023);
  Serial1.write(1);
  Serial2.write(1);
}
void stop(){
  ledcWrite(motor1, 0);
  ledcWrite(motor2, 0);
  Serial1.write(2);
  Serial2.write(2);
}