class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
      self.channels_list = []
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
      self.channel_no = self.channel_no
   def set_channels(self, channels_list):
      self.channels_list = channels_list
   def show_channels(self):
      print('Channel list:')
      number = 1
      for channel in self.channels_list:
        print(f"{number}. {channel}")
        number = number + 1 
   def show_status(self):
      if self.is_on == True :
         print(f"TV in on, channel {self.channel_no}")
      if self.is_on == False:
         print("TV is off")

   