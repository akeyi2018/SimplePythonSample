# -*- coding: utf-8 -*-
from time import sleep
from gpiozero import OutputDevice as stepper
import datetime
import sys

class C28BYJ48:

    def __init__(self, IN1, IN2, IN3, IN4):
        self.IN1 = stepper(IN1)
        self.IN2 = stepper(IN2)
        self.IN3 = stepper(IN3)
        self.IN4 = stepper(IN4)
        #Setting GPIO
        self.stepPins = [self.IN1, self.IN2, self.IN3, self.IN4]
        self.sequenceNumber = 0
        self.stepCount = 8
        self.stop_time = datetime.time(17,30,00,000)
        self.start_time = datetime.time(9,00,00,000)
        self.lunch_time_s = datetime.time(12,00,00,000)
        self.lunch_time_e = datetime.time(13,00,00,000)

    def seq(self):
        return [[1,0,0,1], [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]

    def SetRoll(self, angle, wait):
        #入力値が0以下の場合
        if angle <= 0 : return 0,0
        #回転ステップ数の計算
        #カメラ台座ギア比2：1のため、角度入力値を二倍にします
        steps = int((angle * 2) * 4096 / 360)
        #回転インターバル時間の計算
        #入力値分単位を秒単位へ変換
        interval = float(wait * 60.0 / steps)
        return steps, interval

    #シーケンスのピンをセットする
    def SetPinVoltage(self, NSeq):
        self.sequenceNumber = NSeq
        for pin in range(0,4):
            xPin = self.stepPins[pin]
            seq = self.seq()
            if seq[self.sequenceNumber][pin]!=0:
                xPin.on()
            else:
                xPin.off()
    def Clear_Pin(self):
        for pin in range(0,4):
            xPin = self.stepPins[pin]
            xPin.off()

    def run(self, angle, wait, direction):
        # Set to 1 for clockwise
        # Set to -1 for anti-clockwise
        self.direction = direction
        #回転設定
        steps, interval = self.SetRoll(angle, wait)
        for i in range(0, steps):
            self.SetPinVoltage(self.sequenceNumber)
            self.sequenceNumber += self.direction
            if self.sequenceNumber >= self.stepCount:
                self.sequenceNumber = 0
            if self.sequenceNumber < 0:
                self.sequenceNumber = self.stepCount + self.direction
            sleep(interval)

if __name__ == '__main__':
    StepMotor = C28BYJ48(12,16,20,21)
    wait_time = 30
    # dt = datetime.datetime.now().time()

    # if StepMotor.lunch_time_e >= dt and dt >= StepMotor.lunch_time_s:
        # print('lunch time')

    # while True:
    #     dt = datetime.datetime.now().time()
    #     if StepMotor.lunch_time_e >= dt and dt >= StepMotor.lunch_time_s:
    #         print('lunch time')
    #         sleep(10)
    #     else:
    #         print('working time')
    #         sleep(10)

    while True:
        dt = datetime.datetime.now().time()
        if dt > StepMotor.stop_time:
            sys.exit()
        elif dt < StepMotor.start_time:
            sys.exit()
        elif StepMotor.lunch_time_e >= dt and dt >= StepMotor.lunch_time_s:
            sleep(30)
        else: 
            #時計周り 180度回転/撮影時間1分
            StepMotor.run(180, 0.1, 1)
            StepMotor.Clear_Pin()
            sleep(wait_time)
            #反時計周り 180度回転/撮影時間1分
            StepMotor.run(180, 0.1, -1)
            StepMotor.Clear_Pin()
            sleep(wait_time)
