class Device:
    manufacturer = "China"

    def __init__(self, model, color, brand, device_type):
        self.model = model
        self.color = color
        self.brand = brand
        self.device_type = device_type

    def electrical(self):
        print("Power high state")

    def __repr__(self) -> str:
        return f"{self.model} {self.color} {self.brand} {self.device_type}"

class Phone(Device):
    def __init__(self, model, color, brand, device_type, is_sim, is_callback):
        self.is_sim = is_sim
        self.is_callback = is_callback
        super().__init__(model, color, brand, device_type)

    def call(self):
        print("Phone call")

    def __repr__(self) -> str:
        return super().__repr__() + f" {self.is_sim} {self.is_callback}"

class Laptop(Device):  # Changed inheritance to Device
    def __init__(self, model, color, brand, device_type, config, speed_benchmark):
        self.config = config
        self.speed_benchmark = speed_benchmark
        super().__init__(model, color, brand, device_type)

    def coding(self):
        print("Coding is on")

    def __repr__(self) -> str:
        return super().__repr__() + f" {self.config} {self.speed_benchmark}"

class Tab(Laptop):  # Changed inheritance to Laptop
    def __init__(self, model, color, brand, device_type, s_size, charging_capacity):
        self.s_size = s_size
        self.charging_capacity = charging_capacity
        super().__init__(model, color, brand, device_type, config=None, speed_benchmark=None)  # Calling parent constructor

    def reg(self):
        print("Reg is on Tab")

    def __repr__(self) -> str:
        return super().__repr__() + f" {self.s_size} {self.charging_capacity}"

startechTab = Tab(model='H87', color='Red', brand='Samsung', device_type='Tab', s_size="7.9", charging_capacity="78000")

for att_name, att_value in vars(startechTab).items():
    print(att_name, att_value)
