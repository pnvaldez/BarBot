//BarBot Arduino Code

//Assign digital pins to pumps/stirring motor
#define PUMP_1 2
#define PUMP_2 3
#define PUMP_3 4
#define PUMP_4 5
#define STIRMOTOR 6


float flow_rate; //ml per second, found experimentally. This is passed on from the barbot.py 
float ml_per_oz = 29.57; //conversion factor

int curr_pump = 0;
float servings = 0.0;
float mix_time = 5.0;

void setup() {
  Serial.begin(9600);

  //Setup the pump pins
  pinMode(PUMP_1, OUTPUT);
  digitalWrite(PUMP_1, HIGH);
  pinMode(PUMP_2, OUTPUT);
  digitalWrite(PUMP_2, HIGH);
  pinMode(PUMP_3, OUTPUT);
  digitalWrite(PUMP_3, HIGH);
  pinMode(PUMP_4, OUTPUT);
  digitalWrite(PUMP_4, HIGH);
  pinMode(STIRMOTOR, OUTPUT);
  digitalWrite(STIRMOTOR, HIGH);

  get_flow_rate();
  Serial.println("Waiting for Drinks...");
}

void loop() {
  if (Serial.available()) {
    Serial.println("Getting Command");
    String command = Serial.readString();
    parse_command(command);
    run_pump();
    Serial.println("Done");
  }
}

void get_flow_rate() {
  while (Serial.available() < 1) {
  }
  
  Serial.println("Getting the Flowrate...");

  String flow_rate_str = Serial.readString();
  flow_rate = flow_rate_str.toFloat();
  
  Serial.println("Got the flow rate");
  Serial.println(flow_rate);
}

void parse_command(String curr_command) {
  int command_int = curr_command.toInt();
  int servings_temp = command_int % 100;
  servings = float(servings_temp) / 10;

  curr_pump = (command_int - servings_temp) / 100;

  Serial.println("Pump Pin");
  Serial.println(curr_pump);

  Serial.println("Servings");
  Serial.println(servings);
   
}

void run_pump() {
  float time_run = (servings * ml_per_oz) / flow_rate;
  Serial.println("Time (s)"); 
  Serial.println(time_run);
  if (curr_pump != 6) {
    digitalWrite(curr_pump, LOW);
    delay(time_run * 1000);
    digitalWrite(curr_pump, HIGH);
  }
  else {
    digitalWrite(curr_pump, LOW);
    delay(mix_time *1000);
    digitalWrite(curr_pump, HIGH);
  }
}
