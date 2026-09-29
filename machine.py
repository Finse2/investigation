import random as ran


class Machine:
    def __init__(self, name, max_temperature = 80, max_rpm=5000):
        self.name = name

        self.temperature = 20.0
        self.rpm = 0
        self.running = False

        self.max_temperature = max_temperature
        self.max_rpm = max_rpm

    def start(self, rpm):
        if self.running:
            return f'{self.name} is already running'

        if rpm <= 0:
            return f'{self.name} rpm cannot be initialized at a negative or 0 value'

        if rpm > self.max_rpm:
            return f'{self.name} rpm cannot be initialized at a value greater than {self.max_rpm}'

        self.rpm = rpm
        self.running = True

        return f'{self.name} has been initialized properly running at {self.rpm}'

    def stop(self):
        if not self.running:
            return f'{self.name} is already off'

        self.rpm = 0
        self.running = False
        return f'{self.name} has been terminated successfully'

    def update(self):
        if not self.running:
            return f'{self.name} Machine cannot update when off'
     
        self.temperature += (ran.randint(-5,10) * (self.rpm / self.max_rpm))

        if self.temperature >= self.max_temperature:
            self.stop()
            return f'{self.name} has overheated at a value of {self.temperature}'

    def get_status(self):
        return {
            "name": self.name,
            "temperature":self.temperature,
            "rpm": self.rpm,
            "running": self.running
        }
            


machine = Machine("Machine-01")

print(machine.name)
print(machine.temperature)
print(machine.max_temperature)
print(machine.max_rpm)

print(machine.start(2000))
print(machine.running)
print(machine.rpm)

for i in range(100):
    result = machine.update()
    print(machine.get_status())