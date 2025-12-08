class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
      self.channel_no = self.channel_no
   def set_channel(self, new_channel_no):
      self.new_channel_no = new_channel_no
      self.channel_no = new_channel_no
   
   def show_status(self):
      if self.is_on == True :
         print(f"TV in on, channel {self.channel_no}")
      if self.is_on == False:
         print("TV is off")

   