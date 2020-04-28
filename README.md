# Movingstar
SwissSkills Homework 2020

Dieses Projekt dient als Hausaufgabe für die Vorselektion.
Mein persönliches Ziel ist es, die Schweizermesterschaft mit FOSS (Free Open Source Software) zu bestreiten.

## Toolchain
- [KiCad](https://github.com/KiCad) -> ECAD: Schema & Layout
- Python -> Berechnungen: Stern z.B.

## Hardware

### Lichtsensor & ADC
I(10klx) = 1mA
I(100lx) = 23uA
VCC = 5V
=> R=5k
U(10klx) = I*R = 1mA * 5k = 5V
U(100lx) = I*R = 23uA * 5k = 115mV


### I2C Levelshifter
U104 (Bewegung Sensor) wird mit 2.5V - 3V versorgt. Das I2C Signal bei 2.5V Versorgung genügt dem Microcontroller (U102) nicht für ein logisches 1 (0.7 * VCC = 0.7 * 5V = 3.5V)
So muss das Signal geshiftet werden.
Dies geschieht nach [NXP AN10441](https://www.nxp.com/docs/en/application-note/AN10441.pdf) über die beiden Mosfets Q102 & Q103.

### Programmieren
Als Programmierschnittstelle wird die UPDI Schnittstelle von Atmel verwendet. Diese kommt mit einem Pin aus.

### Stromversorgung
Die Stromversorgung wurde über eine USB-C Buchse vorgesehen. Es stehen dann ca. 5V von einem Handelsüblichen Steckernetzteil zur Verfügung.
Imax ~= 30LED * 3Farben * ca. 20mA = 1.8A
Somit sollte die Quelle auf 2A ausgelegt werden um alle LEDs komplett anzusteuern.
Für die Versorgung von U104 Steht ein 3.3V (oder auch 2.5V) Spannungsregler U101 zur Verfügung.
Der Microcontroller U102 wird nicht mit 3.3V Versorgt, da sonst die Taktfrequenz gesenkt werden muss. Dies wurde zum Enwicklungszeitpunkt noch nicht gemacht, um alle Möglichkeiten der LED (WS2812B-2020) Ansteuerung offen zu halten.

### LED Ansteuerung

Als LED Ansteuerung wurden mehrere Möglichkeiten offen gelassen.
- SPI Interface MOSI an PA1 (R105 bestückt)
- I2C Interface SDA an PA1 (R105 bestückt)
- Waveform Generator Output WO3 an PA3 (R106 bestückt)

### Accelerometer U104

Der Beschleunigungssensor wird über I2C über den Levelshifter betrieben. Die Interruptpins können optional verwendet werden.
Die Interrupt Pins müssten auch über einen Levelshifter betrieben werden um eine Korrekte Funktion beim Microcontroller zu erzeugen.



