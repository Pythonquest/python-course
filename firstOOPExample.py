def enter_float(prompt):
    float_val = 0.0
    while 1 == 1:
        try:
            float_val = float(input("Version?: "))
            return float_val
        except Exception as e:
            print("Please type a float value.")

class Program():
    def __init__(self, *args, **kwargs):
        self.lang = input("What language?: ")
        self.version = enter_float("Version?: ")
        self.skill = input("What skill level?: ")

    def upgrade(self):
        new_version = enter_float("Version?: ")
        print("We have updated the version for", self.lang, "to", new_version)
        self.version = new_version


p1 = Program()
p1.upgrade()
print(p1.lang, p1.version, p1.skill)
