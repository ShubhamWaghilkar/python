class ElectronicDevice:
    Gpu = "1050ti"
    def Computer(self):
        self.processor = "Snapdragon 855"
        self.Camera = "sony imx586"
        self.display = "Oled"
        return f"the inbild processor is {self.processor} \n the camera module is {self.Camera} " \
               f"\n The display is {self.display}"
    def mob(self):
        self.mobile = "samsung"
        return f"The mobile is {self.mobile}"

class PocketGadgets(ElectronicDevice):
    def pad(self):
        self.padd = "apple"
        self.pads = "Samsung"
        return f"the Apple pad is {self.padd} and the android padd is {self.pads}"

class Phone(PocketGadgets):
    def feature(self):
        self.feat = "Nokia"
        self.feat2 = "Micromax"
        return f"The basic non-chinese phone is {self.feat}" \
               f"The chinese brand is {self.feat2}"

shubham = ElectronicDevice()
jack = PocketGadgets()
jon = Phone()

print(jon.mob())
print(shubham.Gpu)
print(jack.Gpu)


a = ["apple","samsung","honor"]

b = "and".join(a)
print(f"{b} Motorola ")


# class Dad:
#     basekball = 2
#
#     pass
# class Son(Dad):
#     score = 33
#     def isTeam(self):
#         return f"Your Score is {self.score}"
# class Grandson(Son):
#     birth = 1999
#
#     def birthday(self):
#         return f"Your Birth is {self.birth}"
# larry = Dad()
# sarry = Son()
# marry = Grandson()
#
# print(marry.score)
# print(sarry.basekball)