//控制蜂鸣器发声
#define lo(x) ((x)+16)    //宏定义：长音
#define sh(x) ((x)+32)    //宏定义：短音
const int TONE=25;
int channel=0;
const int tones[]={0,262,294,330,349,392,440,494,523,784,880,988,1046,1175};	//每个音符对应的频率
int song[]={1,2,3,1,1,2,3,1,3,4,lo(5),3,4,lo(5),
           sh(5),sh(6),sh(5),sh(4),3,1,sh(5),sh(6),sh(5),sh(4),3,1};

void sing(int tone){	//播放音符，持续时间默认300ms，短音150ms，长音600ms
  const int base=300;
  int tim;
  if(tone>=1 && tone<=13) tim=base;
  else if(tone>=16 && tone<=32) tim=base*2;
  else tim=base/2;
  ledcWriteTone(channel, tones[tone%16]);
  delay(tim);
}

void setup() {
  // Serial.begin(115200);
  ledcAttachPin(25, channel);
  ledcWriteTone(channel, 300);
  delay(1000);
  size_t len=sizeof(song)/sizeof(int);
  for(int i=0;i<len;i++)
    sing(song[i]);
  sing(0);
}

void loop() {

}
