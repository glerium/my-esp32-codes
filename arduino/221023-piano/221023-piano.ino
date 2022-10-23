int channel = 0;
const int TONE = 25;
const int KEYS[]={5,12,14,18,19,21,22};
const int key_count=7;
const int tones[]={262,294,330,349,392,440,494};

void setup(){
  ledcAttachPin(TONE, channel);
  pinMode(33, OUTPUT);
  digitalWrite(33, HIGH);
  for(int i=0;i<key_count;i++) pinMode(KEYS[i], INPUT_PULLUP);
}

void loop() {
  for(int i=0;i<key_count;i++){
    if(digitalRead(KEYS[i])==LOW){
      ledcWriteTone(channel, tones[i]);
      digitalWrite(33, LOW);
      delay(300);
      digitalWrite(33, HIGH);
      ledcWriteTone(channel, 0);
    }
  }
}
