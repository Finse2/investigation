import random as ran


class Machine:
    def __init__(self, name, max_temperature=80, max_rpm=5000):
        # Store the machine's name and initial state.
        self.name = name
        self.temperature = 20.0
        self.rpm = 0
        self.running = False

        # Set the machine's operating limits.
        self.max_temperature = max_temperature
        self.max_rpm = max_rpm

    def start(self, rpm):
        # Prevent starting a machine that is already running.
        if self.running:
            return f'{self.name} is already running'

        # Reject speeds outside the allowed range.
        if rpm < 0:
            return f'{self.name} rpm cannot be initialized at a negative'

        if rpm > self.max_rpm:
            return (
                f'{self.name} rpm cannot be initialized '
                f'at a value greater than {self.max_rpm}'
            )

        # Apply the requested speed and mark the machine as running.
        self.rpm = rpm
        self.running = True

        return f'{self.name} has been initialized properly running at {self.rpm}'

    def stop(self):
        # Nothing needs to change if the machine is already off.
        if not self.running:
            return f'{self.name} is already off'

        # Reset the speed and switch off the machine.
        self.rpm = 0
        self.running = False
        return f'{self.name} has been terminated successfully'
    
    def update(self):
        # Cool toward ambient temperature when stopped or at zero RPM.
        if not self.running or self.rpm == 0:
            if self.temperature > 20.0:
                self.temperature = max(
                    20.0,
                    self.temperature - ran.uniform(0.5, 2.0)
                )

        else:
            # Simulate temperature changes while operating.
            self.temperature += (
                ran.randint(-5, 10) * (self.rpm / self.max_rpm)
            )

            # Keep the simulated temperature at or above ambient.
            self.temperature = max(20.0, self.temperature)

        # Shut down a running machine if it reaches the temperature limit.
        if self.running and self.temperature >= self.max_temperature:
            self.stop()
            return f'{self.name} has overheated at {self.temperature:.2f}°C'
    
    def get_status(self):
        # Return a snapshot of the machine's current state.
        return {
            "name": self.name,
            "temperature": round(self.temperature, 2),
            "rpm": self.rpm,
            "running": self.running
        }
