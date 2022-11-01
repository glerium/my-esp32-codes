//呼吸灯，使用PWM模块
int LED[]={12,14,18};
void setup() {
  for(int i=0;i<3;i++){
    pinMode(LED[i], OUTPUT);
    ledcSetup(LED[i], 100000, 10);
  }
}

void loop() {
  for(int i=0;i<1024;i++)
    for(int j=0;j<3;j++)
      ledcWrite(LED[j], i);
    delay(1);
}
