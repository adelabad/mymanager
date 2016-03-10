import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
from op_method import *
import threading


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self, name=name)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)
'''
t = MyThread(main)
self.threads.append(t)
self.threads[-1].start()
'''
#oon jayi ke ghrare window jadid baz beshe in se khat ro bezarid

class Filemanager(QtGui.QWidget):

    def __init__(self):
        super(Filemanager, self).__init__()
        self.initui()

    def initui(self):

        hbox = QtGui.QVBoxLayout()
        self.backlst = [""]
        self.nextlst = []
        tab_widget = QtGui.QTabWidget()     # add tab
        tab1 = QtGui.QWidget()
        tab2 = QtGui.QWidget()
        tab3 = QtGui.QWidget()
        tab_widget.addTab(tab1, "File")
        tab_widget.addTab(tab2, "Edit")
        tab_widget.addTab(tab3, "View")
        self.check_close = QtGui.QCheckBox()
        self.check_close.setText("TreeView")
        self.check_close.setFixedWidth(66)
        self.check_close.setChecked(True)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.check_close)
        tab3.setLayout(box)

        empty_lbl=QtGui.QLabel()
        #empty_lbl.setFixedWidth(500)


        tab1_vbox = QtGui.QHBoxLayout()
        self.new_window=QtGui.QPushButton("New Window")
        self.new_window.setIcon(QtGui.QIcon("new_window.ico"))
        self.new_window.setFixedWidth(100)
        self.new_window.setToolTip("New Window")

        self.exit_btn=QtGui.QPushButton("Exit")
        self.exit_btn.setIcon(QtGui.QIcon("exit.ico"))
        self.exit_btn.setFixedWidth(50)
        self.exit_btn.setToolTip("Exit")

        self.cmd=QtGui.QPushButton("Command Prompt")
        self.cmd.setIcon(QtGui.QIcon("command.ico"))
        self.cmd.setFixedWidth(120)
        self.cmd.setToolTip("Command Prompt")

        self.control_panel=QtGui.QPushButton("Control Panel")
        self.control_panel.setIcon(QtGui.QIcon("Control_Panel.ico"))
        self.control_panel.setFixedWidth(100)
        self.control_panel.setToolTip("Control Panel")

        self.new_folder = QtGui.QPushButton("New Folder")      #######
        self.new_folder.setIcon(QtGui.QIcon("folder-add.ico"))
        self.new_folder.setFixedWidth(100)
        self.new_folder.setToolTip("New Folder")
        #self.new_folder.setStyleSheet("border: 0px")          #########
        self.del_folder = QtGui.QPushButton("Delete Folder")     #########
        self.del_folder.setIcon(QtGui.QIcon("folder-delete.ico"))
        self.del_folder.setFixedWidth(100)
        self.del_folder.setToolTip("Delete Folder")
        #self.del_folder.setStyleSheet("border: 0px")              ######
        tab1_vbox.addWidget(self.new_window)
        tab1_vbox.addWidget(self.new_folder)
        tab1_vbox.addWidget(self.del_folder)
        tab1_vbox.addWidget(self.control_panel)
        tab1_vbox.addWidget(self.cmd)
        tab1_vbox.addWidget(self.exit_btn)

        tab1_vbox.addWidget(empty_lbl)
        tab1.setLayout(tab1_vbox)
        tab_widget.setFixedHeight(70)
        #tab_widget.setFixedWidth(250)
        hbox.addWidget(tab_widget)
        vbox = QtGui.QHBoxLayout()
        back = QtGui.QPushButton()
        back.setFixedWidth(30)
        back.setStyleSheet("border: 0px")#########
        back.setIcon(QtGui.QIcon("Pre.ico"))
        next = QtGui.QPushButton()
        next.setIcon(QtGui.QIcon("Next.ico"))
        next.setFixedWidth(30)
        next.setStyleSheet("border: 0px")#############
        self.addressbar = QtGui.QLineEdit()
        self.searchbar= QtGui.QLineEdit()######

        self.combo = QtGui.QComboBox(self)#####
        self.combo.addItem("System Search")####
        self.combo.addItem("Web Search")#######

        vbox.addWidget(back)
        vbox.addWidget(next)
        vbox.addWidget(self.addressbar)
        vbox.addWidget(self.searchbar)########
        vbox.addWidget(self.combo)######
        self.searchbar.setFixedWidth(150)########



        self.treeview = QtGui.QTreeView()
        spath = QtCore.QString("")
        self.dirmodel = QtGui.QFileSystemModel(self)
        self.dirmodel.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        self.dirmodel.setRootPath(spath)
        self.treeview.setModel(self.dirmodel)


        self.listview = QtGui.QListView()
        self.filemodel = QtGui.QFileSystemModel(self)
        self.filemodel.setRootPath(spath)
        self.listview.setModel(self.filemodel)


        topright = QtGui.QFrame()
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        self.splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter1.addWidget(self.treeview)
        self.splitter1.setSizes([75, 200])
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.splitter1.addWidget(self.listview)
        splitter2.addWidget(self.splitter1)
        hbox.addLayout(vbox)
        hbox.addWidget(splitter2)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

        self.treeview.clicked.connect(self.on_treeview_clicked)
        self.listview.doubleClicked.connect(self.on_listview_clicked)
        self.addressbar.textChanged.connect(self.address_changed)
        self.check_close.clicked.connect(self.check_treeview)

        back.clicked.connect(self.back_clicked)
        next.clicked.connect(self.next_clicked)

        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle('FileManager')
        self.setLayout(hbox)
        self.show()

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeview_clicked(self, index):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        spath = QtCore.QString(self.dirmodel.fileInfo(index).absoluteFilePath())
        self.listview.setRootIndex(self.filemodel.setRootPath(spath))
        self.addressbar.setText(spath)
        if self.backlst[len(self.backlst)-1] != spath:
            self.backlst.append(spath)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_listview_clicked(self, index):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        spath = QtCore.QString(self.filemodel.fileInfo(index).absoluteFilePath())
        if os.path.isfile(spath):
            os.startfile(spath)
        else:
            self.listview.setRootIndex(self.filemodel.setRootPath(spath))
            self.addressbar.setText(spath)
            if self.backlst[len(self.backlst)-1] != spath:
                self.backlst.append(spath)

    def address_changed(self):
        spath = self.addressbar.text()
        self.listview.setRootIndex(self.filemodel.setRootPath(spath))
        if self.backlst[len(self.backlst)-1] != spath:
            self.backlst.append(spath)


    def check_treeview(self):
        if self.check_close.checkState():
            self.splitter1.setSizes([75, 200])
        else:
            self.splitter1.setSizes([0, 200])

    def back_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        self.nextlst.append(self.backlst.pop())
        if len(self.backlst) < 1 :
            self.backlst.append("")
        else:
            spath = self.backlst[len(self.backlst)-1]
            self.listview.setRootIndex(self.filemodel.setRootPath(spath))
            self.addressbar.setText(spath)



    def next_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        if len(self.nextlst) > 0:
            spath = self.nextlst.pop()
            if spath[len(spath)-2] == ":" and not self.backlst[len(self.backlst)-1] == "" and len(spath)>0:
                self.nextlst=[]
            else:
                self.listview.setRootIndex(self.filemodel.setRootPath(spath))
                self.addressbar.setText(spath)

def main():
    app = QtGui.QApplication(sys.argv)
    win = Filemanager()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
