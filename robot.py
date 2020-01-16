import wpilib
import ctre
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID



LEFT_HAND = GenericHID.Hand.kLeft
RIGHT_HAND = GenericHID.Hand.kRight

#Constants for the kicker`
PNCANID = 0
RFForward = 0
RFReverse = 1

##Motor Victor port 4
##Piston port 2z

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot initialization function"""
        # object that handles basic drive operations
    
       

        self.main_motor = wpilib.PWMVictorSPX(4)

        self.foot = RoboFoot(wpilib.DoubleSolenoid(PNCANID, RFForward, RFReverse))

        self.driver = wpilib.XboxController(0)

     

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass
    
    def teleopInit(self):
        """Executed at the start of teleop mode"""
        #self.myRobot.setSafetyEnabled(True)

    
    

    def teleopPeriodic(self):
        
        forward = self.driver.getY(LEFT_HAND)
        
        self.main_motor.set(forward)


        if self.driver.getAButtonPressed():
            self.foot.kick()
        
        if  self.driver.getAButtonReleased():
            self.foot.unkick()
        



# It's the Super RoboFoot class.
class RoboFoot:
    stateExtend = wpilib.DoubleSolenoid.Value.kForward
    stateRetract = wpilib.DoubleSolenoid.Value.kReverse
    def __init__(self, piston):
        self.piston = piston

    def kick(self):
        self.piston.set(RoboFoot.stateRetract)
    
    def unkick(self):
        self.piston.set(RoboFoot.stateExtend)

    
if __name__ == "__main__":
    wpilib.run(MyRobot)
