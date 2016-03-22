import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
from op_method import operator
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
        tab4= QtGui.QWidget()
        tab_widget.addTab(tab1, "File")
        tab_widget.addTab(tab2, "Edit")
        tab_widget.addTab(tab3, "View")
        tab_widget.addTab(tab4, "Search")
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.tree_state = QtGui.QCheckBox()
        self.tree_state.setText("TreeView")
        self.tree_state.setFixedWidth(66)
        self.tree_state.setChecked(True)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.tree_state)
        tab3.setLayout(box)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.complete_file_search= QtGui.QCheckBox()
        self.complete_file_search.setText("Complete Filename Search")
        self.complete_file_search.setFixedWidth(150)
        self.complete_file_search.setChecked(True)
        box2 = QtGui.QHBoxLayout()
        box2.addWidget(self.complete_file_search)
        tab4.setLayout(box2)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.exact_file_search= QtGui.QCheckBox()
        self.exact_file_search.setText("Exact Filename Search")
        self.exact_file_search.setFixedWidth(130)
        self.exact_file_search.setChecked(False)

        box2.addWidget(self.exact_file_search)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.complete_folder_search= QtGui.QCheckBox()
        self.complete_folder_search.setText("Complete Foldername Search")
        self.complete_folder_search .setFixedWidth(165)
        self.complete_folder_search.setChecked(False)
        box2.addWidget(self.complete_folder_search)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.exact_folder_search= QtGui.QCheckBox()
        self.exact_folder_search.setText("Exact Foldername Search")
        self.exact_folder_search.setFixedWidth(150)
        self.exact_folder_search.setChecked(False)
        box2.addWidget(self.exact_folder_search)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        tab4.setLayout(box2)

        empty_lbl=QtGui.QLabel()
        empty_lbl2=QtGui.QLabel()
        empty_lbl3=QtGui.QLabel()
        box2.addWidget(empty_lbl3)
        ##############################################################
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
        #self.del_folder.setStyleSheet("border: 0px")              ######
        tab1_vbox.addWidget(self.new_window)
        tab1_vbox.addWidget(self.new_folder)
        #tab1_vbox.addWidget(self.del_folder)
        tab1_vbox.addWidget(self.control_panel)
        tab1_vbox.addWidget(self.cmd)
        tab1_vbox.addWidget(self.exit_btn)

        tab1_vbox.addWidget(empty_lbl)
        tab1.setLayout(tab1_vbox)
        #################################################################################
        tab2_vbox = QtGui.QHBoxLayout()
        self.copy_btn=QtGui.QPushButton("Copy")
        self.copy_btn.setIcon(QtGui.QIcon("copy.ico"))
        self.copy_btn.setFixedWidth(60)
        self.copy_btn.setToolTip("Copy")

        self.paste_btn=QtGui.QPushButton("Paste")
        self.paste_btn.setIcon(QtGui.QIcon("paste.ico"))
        self.paste_btn.setFixedWidth(60)
        self.paste_btn.setToolTip("Paste")

        self.cut_btn=QtGui.QPushButton("Cut")
        self.cut_btn.setIcon(QtGui.QIcon("cut.ico"))
        self.cut_btn.setFixedWidth(50)
        self.cut_btn.setToolTip("Cut")

        self.rename_btn=QtGui.QPushButton("Rename")
        self.rename_btn.setIcon(QtGui.QIcon("rename.ico"))
        self.rename_btn.setFixedWidth(70)
        self.rename_btn.setToolTip("Rename")


        self.remove_btn=QtGui.QPushButton("Remove")
        self.remove_btn.setIcon(QtGui.QIcon("del.ico"))
        self.remove_btn.setFixedWidth(75)
        self.remove_btn.setToolTip("Remove")


        tab2_vbox.addWidget(self.copy_btn)
        tab2_vbox.addWidget(self.cut_btn)
        tab2_vbox.addWidget(self.paste_btn)
        tab2_vbox.addWidget(self.rename_btn)
        tab2_vbox.addWidget(self.remove_btn)
        tab2_vbox.addWidget(empty_lbl2)
        tab2.setLayout(tab2_vbox)








        ###########################################################################################
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
        self.mypath=spath
        self.dirmodel = QtGui.QFileSystemModel(self)
        self.dirmodel.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        self.dirmodel.setRootPath(spath)
        self.treeview.setModel(self.dirmodel)


        self.listview = QtGui.QListView()
        self.filemodel = QtGui.QFileSystemModel(self)
        self.filemodel.setRootPath(spath)
        self.listview.setModel(self.filemodel)


        self.topright = QtGui.QFrame()

        self.topright.setFrameShape(QtGui.QFrame.StyledPanel)

        self.splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter1.addWidget(self.treeview)
        self.splitter1.setSizes([75, 200])
        self.splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.splitter1.addWidget(self.listview)
        self.splitter2.addWidget(self.splitter1)
        hbox.addLayout(vbox)
        hbox.addWidget(self.splitter2)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))


        self.splitter1.splitterMoved.connect(self.tick_splitter)
        self.treeview.clicked.connect(self.on_treeview_clicked)
        self.listview.doubleClicked.connect(self.on_listview_doubleclicked)
        self.addressbar.textChanged.connect(self.address_changed)
        self.tree_state.clicked.connect(self.check_treeview)
        self.listview.clicked.connect(self.on_listview_clicked)

        back.clicked.connect(self.back_clicked)
        next.clicked.connect(self.next_clicked)
        self.control_panel.clicked.connect(self.on_ctrl_pnl_clicked)
        self.cmd.clicked.connect(self.on_cmd_clicked)
        self.exit_btn.clicked.connect(self.exit_clicked)
        self.new_window.clicked.connect(self.new_win_clicked)
        self.new_folder.clicked.connect(self.new_folder_clicked)
        self.remove_btn.clicked.connect(self.remove_btn_clicked)
        self.copy_btn.clicked.connect(self.copy_btn_clicked)
        self.rename_btn.clicked.connect(self.rename_btn_clicked)
        self.cut_btn.clicked.connect(self.cut_btn_clicked)
        self.paste_btn.clicked.connect(self.paste_btn_clicked)
        self.statusbar = QtGui.QStatusBar()
        hbox.addWidget(self.statusbar)

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
        if len(spath)<4:
            self.statusbar.showMessage(spath[0])
        elif operator("check_file",spath):
            self.statusbar.showMessage(spath.split("/")[-1]+"\tsize:\t"+operator("file_size",spath)+"Byte")
        else:
            self.statusbar.showMessage(spath.split("/")[-1]+"\titems:\t"+operator("folder_size",spath))

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_listview_doubleclicked(self, index):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        spath = QtCore.QString(self.filemodel.fileInfo(index).absoluteFilePath())
        if operator("check_file",spath):
            operator("run",spath)
        else:
            self.listview.setRootIndex(self.filemodel.setRootPath(spath))
            self.addressbar.setText(spath)
            if self.backlst[len(self.backlst)-1] != spath:
                self.backlst.append(spath)

    def address_changed(self):
        spath = self.addressbar.text()
        if operator("check_path", spath) or spath == "":
            self.listview.setRootIndex(self.filemodel.setRootPath(spath))
            if self.backlst[len(self.backlst)-1] != spath:
                self.backlst.append(spath)
            if len(spath)<4:
                if spath == "":
                    self.statusbar.showMessage("")
                else:
                    self.statusbar.showMessage(spath[0])
            else :
                try :
                    if operator("check_file",spath):
                        self.statusbar.showMessage(spath.split("/")[-1]+"\tsize:\t"+operator("file_size",spath)+"Byte(s)")
                    else:
                        self.statusbar.showMessage(spath.split("/")[-1]+"\titems:\t"+operator("folder_size",spath))
                except :
                    print ""

    def tick_splitter(self):
        if self.treeview.width()>0  :
            self.tree_state.setChecked(True)

        else :
            self.tree_state.setChecked(False)


    def check_treeview(self):
        if self.tree_state.checkState():
            self.splitter1.setSizes([75, 200])
        else:
            self.splitter1.setSizes([0, 200])

    def back_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        self.nextlst.append(self.backlst.pop())
        if -1<len(self.backlst) < 1 :
            self.backlst.append("")

        elif len(self.backlst)>=1:
            spath = self.backlst[len(self.backlst)-1]
            self.listview.setRootIndex(self.filemodel.setRootPath(spath))
            self.addressbar.setText(spath)
            if len(spath)<4:
                if spath == "":
                    self.statusbar.showMessage("")
                else:
                    self.statusbar.showMessage(spath[0])
            elif operator("check_file",spath):
                self.statusbar.showMessage(spath.split("/")[-1]+"\tsize:\t"+operator("file_size",spath)+"Byte(s)")
            else:
                self.statusbar.showMessage(spath.split("/")[-1]+"\titems:\t"+operator("folder_size",spath))

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_listview_clicked(self, index):
        spath = QtCore.QString(self.filemodel.fileInfo(index).absoluteFilePath())
        if len(spath)<4:
            self.statusbar.showMessage(spath[0])
        elif operator("check_file",spath):
            self.statusbar.showMessage(spath.split("/")[-1]+"\tsize:\t"+operator("file_size",spath)+"Byte(s)")
        else:
            self.statusbar.showMessage(spath.split("/")[-1]+"\titems:\t"+operator("folder_size",spath))
        self.temp_path=spath
###################################
    def on_ctrl_pnl_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        operator("control_panel")
    def on_cmd_clicked(self,spath):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        operator("cmd",str(self.addressbar.text()))

    def next_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        if len(self.nextlst) > 0:
            spath = self.nextlst.pop()
            if len(spath)>0:
                if spath[len(spath)-2] == ":" and not self.backlst[len(self.backlst)-1] == "":
                    self.nextlst=[]
                else:
                    self.listview.setRootIndex(self.filemodel.setRootPath(spath))
                    self.addressbar.setText(spath)
                if len(spath)<4:
                    self.statusbar.showMessage(spath[0])
                elif operator("check_file",spath):
                    self.statusbar.showMessage(spath.split("/")[-1]+"\tsize:\t"+operator("file_size",spath)+"Byte(s)")
                else:
                    self.statusbar.showMessage(spath.split("/")[-1]+"\titems:\t"+operator("folder_size",spath))

    def exit_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        QtGui.QApplication.quit()

    def new_win_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        operator("run", "menu.py")

    def new_folder_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter Folder Name:')

        if ok:
            if self.addressbar.text()[-1] != "\\":
                operator("new_fd",str(self.addressbar.text())+"\\"+str(text))
            else:
                operator("new_fd",str(self.addressbar.text())+str(text))


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def remove_btn_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        try:
            if operator("check_file",str(self.temp_path)):
                #operator("change_dir",str(self.temp_path))
                operator("remove_file",str(self.temp_path))

                print str(self.temp_path)
            elif operator("check_dir",str(self.temp_path)):
                operator("remove_folder",str(self.temp_path))
        except:
            print "Coudn't open !"
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def copy_btn_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        self.tempcopy=self.temp_path
        self.order="copy"


    def cut_btn_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        self.tempcut=self.temp_path
        self.order="cut"

    def paste_btn_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()

        try :
            if self.order=="copy":
                if operator("check_file",str(self.tempcopy)):
                     operator("copy_file",str(self.tempcopy),str(self.addressbar.text()))
                elif operator("check_dir",str(self.tempcopy)):
                     operator("copy_folder",str(self.tempcopy),str(self.addressbar.text()+"/"+str(self.tempcopy).split("/")[-1]))

            elif self.order=="cut":
                operator("move",str(self.tempcut),str(self.addressbar.text()))
            print self.order , self.addressbar.text() , self.tempcopy
        except:
            print "COUDNT"

#####################33
    def rename_btn_clicked(self):
        self.click_sound=QtGui.QSound("_click_.wav")
        self.click_sound.play()
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter the New Name:')
        tempdir=self.addressbar.text()
        if ok:
            try :
                if operator("check_dir",str(self.temp_path)):
                    operator("rename",str(self.temp_path),str(tempdir)+"/"+text)
                    print str(self.temp_path),str(tempdir),text
                elif operator("check_file",str(self.temp_path)):
                    operator("rename",str(self.temp_path),str(tempdir)+'/'+text+str(operator("file_format",str(self.temp_path))))
                    print str(self.temp_path),str(tempdir)+'/'+text+str(operator("file_format",str(self.temp_path)))
            except:
                print "Coudnt"

def main():
    app = QtGui.QApplication(sys.argv)

    win = Filemanager()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
