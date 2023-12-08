//
//
//
#include <Wire.h>

const int LedPin = LED_BUILTIN;

int x;

void setup() {
  pinMode(LedPin, OUTPUT);
  pinMode(A0, INPUT);
  digitalWrite(LedPin, LOW);
  
  Wire.begin(0x08);
  Wire.onReceive(Detection);

  Serial.begin(9600);
  Wire.onRequest(requestEvent);

  // put your setup code here, to run once:

}

  void Detection(int count_on){
  while(Wire.available()){
    char a = Wire.read();
    digitalWrite(LedPin, a);
    }
  
  }

void loop() {
  Serial.println(x);
  delay(100);
  // put your main code here, to run repeatedly:

}


void requestEvent (int x) {


x = analogRead(A0);

Wire.write(highByte(x));
Wire.write(lowByte(x));

}


