import math
import ctre 
import wpilib

import robotpy_ext.common_drivers

PORT = 1


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #DRIVETRAIN
        print("It's Alive")
        self.stick = wpilib.XboxController(0)
        self.motor1 = ctre.WPI_TalonSRX(PORT)

    def robotPeriodic(self):
        return

    def teleopInit(self):
        print("TELEOP BEGINS")
        #self.motor2 = ctre.WPI_TalonSRX(PORT)
       # self.drive = DifferentialDrive(self.motor1, self.motor2)
        self.encoder = wpilib.Encoder(0,1)
        # setup wheel diameter

    def teleopPeriodic(self):
        forward = self.stick.getRawAxis(5)
        self.motor1.set(forward)
        #print(self.encoder.get())


if __name__ == "__main__":
	wpilib.run(Robot)
    