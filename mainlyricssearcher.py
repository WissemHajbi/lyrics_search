import sys
from PyQt6.QtWidgets import QApplication, QGraphicsOpacityEffect,QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic 
from lyricssearcher import lyricssearch

class filesearcherUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('lyricssearcher.ui',self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Lyrics Searcher")
        self.setFixedHeight(663)
        self.setFixedWidth(585)
        self.setStyleSheet("background-color: #121212;")
        self.styling()
        self.searchButton.clicked.connect(self.search)
    def search(self):
        self.clearError()
        input=lyricssearch(self.songname.text(),self.singer.text())
        if len(input) == 2: 
            self.title.setText(input['title'])
            self.lyrics.setText(input['lyrics'])
        else:
            self.errors.setStyleSheet( 'color:#ff0000;' )
            self.errors.setText(input['error'])
    def styling(self):
        self.searchButton.setStyleSheet('background-color:#03DAC5;border : 2px solid green;border-color :#FFFFFF;color:white')
        self.songname.setStyleSheet('background-color:#BB86FC;padding-left:10px;')
        self.singer.setStyleSheet('background-color:#BB86FC;padding-left:10px;')
        self.title.setStyleSheet('background-color:#FF7597;')
        self.lyrics.setStyleSheet('background-color:#FF7597;')
        self.labelsongname.setStyleSheet('color:#FFFFFF')
        self.labelsingername.setStyleSheet('color:#FFFFFF')
        # setting opacity effect
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.70)
        self.labelsongname.setGraphicsEffect(opacity_effect)
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.70)
        self.labelsingername.setGraphicsEffect(opacity_effect)
    def clearError(self):
        self.errors.setText('')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    filesearcherUI= filesearcherUI()
    filesearcherUI.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing window')
        