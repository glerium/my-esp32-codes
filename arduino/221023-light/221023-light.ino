// 2022.10.23 LED灯循环亮灭
int ledPin = 32;
int ledPin2 = 33;
int delayTime = 1000;
void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin,OUTPUT);
  pinMode(ledPin2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin,HIGH);
  digitalWrite(ledPin2,HIGH);
  delay(delayTime);
  digitalWrite(ledPin,LOW);
  digitalWrite(ledPin2,LOW);
  delay(delayTime);
}
