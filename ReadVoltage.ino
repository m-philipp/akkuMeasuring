
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}


void loop() {
  // read the analog input Pins:
  int sensorValue0 = analogRead(A0);
  delay(10);
  int sensorValue1 = analogRead(A1);
  delay(10);
  int sensorValue2 = analogRead(A2);
  delay(10);
  int sensorValue3 = analogRead(A3);
  delay(10);
  int sensorValue4 = analogRead(A4);
  delay(10);
  int sensorValue5 = analogRead(A5);
  delay(10);
  
  
  // print out the values read:
  Serial.print(sensorValue0);
  Serial.print(" ");
  Serial.print(sensorValue1);  
  Serial.print(" ");
  Serial.print(sensorValue2);
  Serial.print(" ");
  Serial.print(sensorValue3);
  Serial.print(" ");
  Serial.print(sensorValue4);
  Serial.print(" ");
  Serial.println(sensorValue5);
  delay(3000);       
}
