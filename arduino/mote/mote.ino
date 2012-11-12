   /*
   *  Copyright (C) 2007 Libelium Comunicaciones Distribuidas S.L.
   *  http://www.libelium.com
   *
   *  This program is free software: you can redistribute it and/or modify
   *  it under the terms of the GNU General Public License as published by
   *  the Free Software Foundation, either version 2 of the License, or
   *  (at your option) any later version.
   *
   *  This program is distributed in the hope that it will be useful,
   *  but WITHOUT ANY WARRANTY; without even the implied warranty of
   *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   *  GNU General Public License for more details.
   *
   *  You should have received a copy of the GNU General Public License
   *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
   *
   *  SquidBee code
   *  Version 0.1
   *  Author: Marcos Yarza
   */



   // variables declaration
   //sensors
   int sens0 = 0;    // Light sensor
   int sens1 = 1;    // Humidity sensor
   int sens2 = 2;    // Temperature sensor

   //aux var
   int val0 = 0;
   int val1 = 0;
   int val2 = 0;

   int count = 0;

   void setup(){  
   Serial.begin(19200);    // starts the serial port
   }

   // function to send data

   void sendData(int id,int num, int data0,int data1,int data2){
   
   Serial.print("@");
   Serial.print(id);
   Serial.print("|");
   
   Serial.print(num);
   
   Serial.print("|data0-");
   Serial.print(data0);
   
   Serial.print("|data1-");
   Serial.print(data1);
   
   Serial.print("|data2-");
   Serial.print(data2);
      
   Serial.println("#\r");      // end of message
   }

   void loop(){ 
   while (count <= 10000){
      val0 = analogRead(sens0);
      val1 = analogRead(sens1);
      val2 = analogRead(sens2);
      //val2 = (analogRead(sens2) * 5 / 1024) / 0.01;
      
      sendData(1,count, val0,val1,val2);

      delay(5000);
      count++;
      }
   
   count = 0;

   }
