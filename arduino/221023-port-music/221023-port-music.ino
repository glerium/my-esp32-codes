int channel=0, cn_light=1;
const int tones[]={262,294,330,349,392,440,494};
void setup() {
  Serial.begin(9600);
  ledcAttachPin(25, channel);
  ledcAttachPin(33, cn_light);
  ledcSetup(cn_light, 112000, 10);
  ledcWrite(cn_light, 1023);
}

void loop() {
  if(Serial.available()){
    char ima = Serial.read();
    ledcWriteTone(channel, tones[ima-'1']);
    ledcWrite(cn_light, max(1023-150*(ima-'0'),0));
    Serial.write(ima);
    delay(400);
  }
}
