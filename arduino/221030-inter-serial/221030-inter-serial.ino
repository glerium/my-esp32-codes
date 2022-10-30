void setup() {
  pinMode(33, OUTPUT);
  pinMode(32, OUTPUT);
  pinMode(35, INPUT);
  pinMode(34, INPUT);
  digitalWrite(33, 1);
  digitalWrite(32, 1);
  Serial.begin(115200,SERIAL_8N1,19,21);
  // Serial.begin(115200);
}

void loop() {
  bool got=false;
  if(Serial.available()){
    char in=Serial.read();
    if(in=='1'){
      digitalWrite(33, 0);
      digitalWrite(32, 1);
      got=true;
      // delay(100);
    }else if(in=='2'){
      digitalWrite(33, 1);
      digitalWrite(32, 0);
      got=true;
      // delay(100);
    }
  }
  if(!got){
    digitalWrite(33, 1);
    digitalWrite(32, 1);
  }
  int key1=digitalRead(35),
      key2=digitalRead(34);
  if(!key1) Serial.write('1');
  if(!key2) Serial.write('2');
  // delay(100);
  delay(10);
}
