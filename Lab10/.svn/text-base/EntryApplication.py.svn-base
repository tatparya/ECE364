import sys
import re
import string

from PySide.QtGui import *

from EntryForm import *



class EntryApplication(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)

        #   Conneting Buttons
        self.textList = [ self.txtFirstName, self.txtLastName, self.txtAddress, self.txtCity, self.txtState, self.txtZip, self.txtEmail ]

        self.btnClear.clicked.connect( lambda : self.clear() )
        self.btnSave.clicked.connect( lambda : self.save() )
        self.btnLoad.clicked.connect( lambda : self.load() )

        for txtEdit in self.textList:
            txtEdit.textChanged.connect( lambda: self.intialize() )

        self.enteringText = 0

    def intialize(self):

        if self.enteringText == 1:
            return

        #   Enable load
        self.btnLoad.setDisabled( True )

        #   Disable save
        self.btnSave.setEnabled( True )

        #   Reset Error
        self.resetError()

        self.enteringText = 1

    def clear(self):
        #   Clear all text from text fields
        for editText in self.textList:
            editText.setText( "" )

        #   Enable load
        self.btnLoad.setEnabled( True )

        #   Disable save
        self.btnSave.setDisabled( True )

        self.enteringText = 0

    def load(self):
        self.enteringText = 0
        self.loadData()

    def save(self):
        self.enteringText = 0

        #   Check if all fields are entered
        for lineEdit in self.textList:
            if lineEdit.text() == "":
                self.setError( "Error: One of the fields are empty!" )
                return

        #   Validate text fields
        #   State
        exists = 0
        inputState = self.txtState.text()
        for state in self.states:
            if inputState == state:
                exists = 1
        if exists == 0:
            self.setError( "Error: State is not valid" )
            return

        #   Zip
        inputZip = self.txtZip.text()
        match = re.findall( r"\d{5}", inputZip )
        if not match:
            self.setError( "Error: ZIP is not valid" )
            return

        #   Email
        inputEmail = self.txtEmail.text()
        emailMatch = re.findall( r"\w+@\w+\.\w+", inputEmail )
        if not emailMatch:
            self.setError( "Error: Email is not valid" )
            return

        #   Save to xml
        self.saveToXml()

    #   Function to reset error label
    def resetError(self):
        self.lblError.setText( "" )

    #   Function to set error label to message
    def setError(self, message):
        self.lblError.setText( message )

    #   Function to save to xml
    def saveToXml(self):

        #   Open output file
        outputFilename = "target.xml"
        outputFile = open( outputFilename, 'w' )

        #   Getting data from input form
        firstName = self.txtFirstName.text()
        lastName = self.txtLastName.text()
        address = self.txtAddress.text()
        city = self.txtCity.text()
        state = self.txtState.text()
        zip = self.txtZip.text()
        email = self.txtEmail.text()

        #   Creating xml
        firstLine = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        outputFile.write( firstLine )
        userBegin = "<user>\n"
        firstNameOut = "\t<FirstName>" + firstName + "</FirstName>\n"
        lastNameOut = "\t<LastName>" + lastName + "</LastName>\n"
        addresssOut = "\t<Address>" + address + "</Address>\n"
        cityOut = "\t<City>" + city + "</City>\n"
        stateOut = "\t<State>" + state + "</State>\n"
        zipOut = "\t<ZIP>" + zip + "</ZIP>\n"
        emailOut = "\t<Email>" + email + "</Email>\n"
        userEnd = "</user>"
        userOut = userBegin + firstNameOut + lastNameOut + addresssOut + cityOut + stateOut + zipOut + emailOut + userEnd
        outputFile.write( userOut )

    #   Gets the entire file as a string
    def getEntireFile(self, filename ):
        LongString = ""
        with open( filename, 'r' ) as inputFile:
            content = inputFile.readlines()
        LongString = LongString.join(content)
        #print( LongString )
        return LongString

    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """

        #   Get entire file
        allLines = self.getEntireFile( filePath )
        #print( allLines )

        #   FirstName
        match1 = re.findall( r"<FirstName>(\w*)</FirstName>", allLines )
        if match1:
            #print (match1)
            self.txtFirstName.setText( match1[0] )
        #   LastName
        match2 = re.findall( r"<LastName>(\w*)</LastName>", allLines )
        if match2:
            #print (match2)
            self.txtLastName.setText( match2[0] )
        #   Address
        match3 = re.findall( r"<Address>(\w*)</Address>", allLines )
        if match3:
            #print (match3)
            self.txtAddress.setText( match3[0] )
        #   City
        match4 = re.findall( r"<City>(\w*)</City>", allLines )
        if match4:
            #print (match4)
            self.txtCity.setText( match4[0] )
        #   State
        match5 = re.findall( r"<State>(\w*)</State>", allLines )
        if match5:
            #print (match5)
            self.txtState.setText( match5[0] )
        #   ZIP
        match6 = re.findall( r"<ZIP>(\w*)</ZIP>", allLines )
        if match6:
            #print (match6)
            self.txtZip.setText( match6[0] )
        #   Email
        match7 = re.findall( r"<Email>(.*)</Email>", allLines )
        if match7:
            #print (match7)
            self.txtEmail.setText( match7[0] )


        pass

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadFromXmlFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()
