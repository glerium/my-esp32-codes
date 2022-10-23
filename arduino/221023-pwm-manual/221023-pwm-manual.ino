const int led = 33;
const int cnt = 100;
void setup() {
  pinMode(led, OUTPUT);
}

void loop() {
  for(int i=0;i<=cnt;i++){
    for(int j=0;j<10;j++){
      digitalWrite(led, LOW);
      delayMicroseconds(i);
      digitalWrite(led, HIGH);
      delayMicroseconds(cnt*2-i);
    }
  }
  for(int i=cnt;i>=0;i--){
    for(int j=0;j<10;j++){
      digitalWrite(led, LOW);
      delayMicroseconds(i);
      digitalWrite(led, HIGH);
      delayMicroseconds(cnt*2-i);
    }
  }
}
