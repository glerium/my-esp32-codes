//2022.10.23 单片机与电脑利用电脑串口通信控制LED亮灭
void setup() {
  Serial.begin(9600);
  pinMode(33, OUTPUT);
  digitalWrite(33, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    int a=Serial.read();
    if(a=='1'){
      digitalWrite(33, LOW);
      Serial.write('1');
      delay(300);
    }
    else if(a=='0'){
      digitalWrite(33, HIGH);
      Serial.write('0');
      delay(300);
    }
  }
}
