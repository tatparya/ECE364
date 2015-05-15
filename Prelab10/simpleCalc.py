# Import classes
import sys
import locale

from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

#   Calculator Class
class simpleCalculator(QMainWindow, Ui_MainWindow):

    #   Constructor
    def __init__(self, parent=None):
        super(simpleCalculator, self).__init__(parent)
        self.setupUi(self)

        #   Set up buttons click listeners

        #   Numbers
        self.pb0.clicked.connect(lambda : self.appendStr('0'))
        self.pb1.clicked.connect(lambda : self.appendStr('1'))
        self.pb2.clicked.connect(lambda : self.appendStr('2'))
        self.pb3.clicked.connect(lambda : self.appendStr('3'))
        self.pb4.clicked.connect(lambda : self.appendStr('4'))
        self.pb5.clicked.connect(lambda : self.appendStr('5'))
        self.pb6.clicked.connect(lambda : self.appendStr('6'))
        self.pb7.clicked.connect(lambda : self.appendStr('7'))
        self.pb8.clicked.connect(lambda : self.appendStr('8'))
        self.pb9.clicked.connect(lambda : self.appendStr('9'))
        self.pbDecimal.clicked.connect(lambda : self.appendStr('.'))
        self.pbCancel.clicked.connect(lambda : self.appendStr('C'))

        #   Operator
        self.pbAdd.clicked.connect(lambda : self.operate('+'))
        self.pbSub.clicked.connect(lambda : self.operate('-'))
        self.pbMul.clicked.connect(lambda : self.operate('*'))
        self.pbDiv.clicked.connect(lambda : self.operate('/'))

        self.pbEqual.clicked.connect(lambda : self.operate('='))

        #   Other
        self.decimalBox.valueChanged.connect(lambda : self.changeDecimal())
        self.cbThousands.stateChanged.connect(lambda : self.changeThou())

        #   Two variables to store values
        self.x = 0
        self.y = 0
        self.result = 0
        self.decimal = 0

        #   To store display string
        self.expression = ""
        self.operator = '+'
        self.numstrokes = 0
        self.keystrokes = 0
        self.thousands = 0
        self.changeThou()

        #   Set locale to US
        locale.setlocale( locale.LC_ALL, 'en_US' )

    def changeThou(self):
        #   Get value
        if self.cbThousands.isChecked():
            self.thousands = 1
        else:
            self.thousands = 0

    def changeDecimal(self):
        #   Get value
        print("DECIAL VALUE CHANGED!!")
        self.decimal = self.decimalBox.value()

    #   To append number to display
    def appendStr(self, num):
        if self.numstrokes == 0:
            #   Refresh display
            self.expression = ""
            self.mainDisplay.setText(self.expression)
        self.numstrokes += 1
        #   Get expression
        if num == 'C':
            if len(self.expression) > 1:
                self.expression = self.expression[:-1]
                self.mainDisplay.setText(self.expression)
            else:
                self.expression = "0."
                self.numstrokes = 0
                self.keystrokes = 0
                self.x = 0
                self.y = 0
                #self.printDebug()
        else:
            self.expression += num
        #   Set to display
        self.mainDisplay.setText(self.expression)
        self.printExpr()

    def operate(self, operator):

        #   Get Operator
        if operator == '=':
            self.getResult()
            self.y = self.x
        else:
            #   check number of keystrokes
            self.keystrokes += 1

            if self.keystrokes > 1:
                #   Operate, set result to x and proceed
                self.getResult()
                self.keystrokes = 1
            else:
                #   Get x from display
                if( self.mainDisplay.displayText() != "" ):
                    try:
                        self.x = float(self.mainDisplay.displayText())
                    except ValueError:
                        self.expression = "Error"
                        self.numstrokes = 0
                        self.mainDisplay.setText(self.expression)
                        return
                else:
                    self.x = 0

            #   Get operator
            if operator == '+':
                self.operator = '+'
            elif operator == '-':
                self.printDebug()
                if self.numstrokes == 0 and self.keystrokes >= 1:
                    self.negate()
                    return
                else:
                    self.operator = '-'
            elif operator == '*':
                self.operator = '*'
            elif operator == '/':
                self.operator = '/'

            self.numstrokes = 0
            self.printDebug( "After new operator")

        self.printDebug( "After operation ")

    def getResult(self):
        result = 0
        error = ""
        #   Get y
        try:
            self.y = float(self.expression)
        except ValueError:
            self.expression = "Error"
            self.mainDisplay.setText(self.expression)
        #   Get Operator
        if self.operator == '+':
            #   Add
            result = self.x + self.y
        elif self.operator == '-':
            #   Subtract
            result = self.x - self.y
        elif self.operator == '*':
            #   Multiply
            result = self.x * self.y
        else:
            #   Divide
            #   Check for division by 0
            if not self.y == 0:
                result = self.x / self.y
            else:
                error = "Error"

        if not error:
            #   Set display to result
            self.x = result
            #   Get decimal Value
            if self.thousands:
                expression = '{:,}'.format(int(self.x))
            else:
                expression = "%.*f" % ( self.decimal, self.x )
            self.mainDisplay.setText(expression)
        else:
            self.mainDisplay.setText(error)

        self.keystrokes = 0
        self.numstrokes = 0

    def negate(self):
        self.appendStr('-')
        pass


    def printDebug(self, string="Debug" ):
        #print( string )
        #print( "Self x = {0}".format( self.x ) )
        #print( "Self y = {0}".format( self.y ) )
        #print( "Operator = " + self.operator )
        #print( "numStrokes = {0}".format( self.numstrokes ) )
        #print( "keyStrokes = {0}".format( self.keystrokes ) )
        #print( "decimal = {0}".format( self.decimal ) )
        pass

    def printExpr(self):
        #print( "Expression: " + self.expression )
        pass

    def printNumStrokes(self):
        #print( "numStrokes = {0}".format( self.numstrokes ) )
        pass

#   Main
def main():
    app = QApplication(sys.argv)
    calculator = simpleCalculator()

    calculator.show()
    app.exec_()
    pass

if __name__ == "__main__":
    main()
