class dad:
    basketball = 1
class son(dad):
    dance = 6

    def isdance(self):
        return f"yes i dance {self.dance} no of time"
class grandson(son):
    def isdance(self):
        dance=6
        return f"jackson yeah!/" \
               f"yes i dance very awesomely {self.dance} no of time"
darry=dad()
larry=son()
harrry=grandson()
print(harrry.dance)


# write a programm
# electronic device
# pocket gadget
# phone
