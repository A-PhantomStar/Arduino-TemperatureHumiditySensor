#include <DHT.h> //Libreria necesaria para el sensor
#define pinDHT 2 //Declaracion del pin para el sensor

DHT dht(pinDHT, DHT11);// Inicializamos sensor

//Declaramos las variables
double temperatura;
double humedad;

void setup() {
  Serial.begin(9600);//Inicializamos el puerto serial
  dht.begin();

}

void loop() {
  // Obtenemos la lectura de temperatura y humedad
  temperatura = dht.readTemperature();
  humedad = dht.readHumidity();

  // Imprimimos los valores obtenidos
  Serial.print(temperatura); Serial.print("x");Serial.println(humedad);

  delay(1000); //Actualizamos datos cada 1 segundo
  
}