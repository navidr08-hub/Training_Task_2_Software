# Training_Task_2_Software

This is a python script that uses pygame to take user input from the keyboard, and sends directions based on user input: forward, backward, left, right. 
Using the TCP commuication, the directions are sent in the form of PWM data for each single motor (4-motors), to the client (rover) from the host machine.

### input.py
- Acts as the host and interprets the user keyboard input and converts it to PWM data.
- Sends PWM data to client (output.py)

### output.py
- Acts as the reciever (rover) and simply prints the PWM data recieved from the host.
- Used socket python module for TCP communications on a server to send and recieve data.

### DEMO
https://user-images.githubusercontent.com/72671675/138581785-7efbdd1d-8459-477e-b89b-15df8eb100cc.mp4

#### Screenshot of output
![image](https://user-images.githubusercontent.com/72671675/138581305-ec65b36a-c53c-4d74-84d7-0d8939e60ce1.png)
