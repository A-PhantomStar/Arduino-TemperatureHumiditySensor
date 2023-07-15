// C++ code
//
float temp;

void setup()
{
  Serial.begin(9600); //Begin console
  //pinMode(2, OUTPUT); //blue led
  pinMode(3, OUTPUT); //Green
  pinMode(4, OUTPUT); //Red
  pinMode(2, INPUT); //sensor

}

void loop(){
  temp = digitalRead(2);
  //temp = temp * 0.48828125;
  Serial.print("The temp is: ");
  Serial.print(temp);
  Serial.println();
  delay(1000);
}