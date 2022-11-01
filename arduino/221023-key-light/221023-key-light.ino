// 2022.10.23 按键小台灯
int led1=33, led2=32;
int key1=35, key2=34;
void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(key1, INPUT);
  pinMode(key2, INPUT);
  digitalWrite(led1, HIGH);
  digitalWrite(led2, HIGH);
}

void loop() {
  if(!digitalRead(key1)){
    while(!digitalRead(key1));
    digitalWrite(led1, 1-digitalRead(led1));
  }
  if(!digitalRead(key2)){
    while(!digitalRead(key2));
    digitalWrite(led2, 1-digitalRead(led2));
  }
}
