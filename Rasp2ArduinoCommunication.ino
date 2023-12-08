//
//
//
#include <Wire.h>

const int LedPin = LED_BUILTIN;

void setup() {
  pinMode(LedPin, OUTPUT);
  digitalWrite(LedPin, LOW);
  
  Wire.begin(0x08);
  Wire.onReceive(Detection);

  // put your setup code here, to run once:

}

  void Detection(int count_on){
  while(Wire.available()){
    char a = Wire.read();
    digitalWrite(LedPin, a);
    }
  
  }

void loop() {
  delay(100);
  // put your main code here, to run repeatedly:

}
