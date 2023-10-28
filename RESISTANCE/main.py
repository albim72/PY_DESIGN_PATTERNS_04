from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

print("___________ OldResistor _____________")
r0 = OldResistor(10.2E2)
print(r0)
print(r0._ohms)
r0.set_ohms(2.88E3)
print(r0.get_ohms())

print("___________ Resistor _____________")
r1 = Resistor(50E3)
print(r1.ohms)
r1.ohms = 1.3E3
print(f'układ elektryczny:\noporność: {r1.ohms} omów\n'
      f'napięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A\n')


print("___________ VoltageResistance _____________")
r2 = VoltageResistance(1.06E2)
print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 322
print(f'opór: {r2.ohms} omów')
print(f'napięcie prądu: {r2.voltage} V')
print(f'natężenie prądu: {r2.current} A')
