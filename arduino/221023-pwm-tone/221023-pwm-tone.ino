int tone=25;
int channel=0;
void setup() {
  // Serial.begin(115200);
  ledcAttachPin(25, channel);
  ledcWriteTone(channel, 300);
}

void loop() {

}
