def contextMenuEvent(self, pos):
    self.menu = QMenu(self)
    renameAction = QtGui.QAction('Rename', self)
    renameAction.triggered.connect(lambda: self.renameSlot(pos))
    self.menu.addAction(renameAction)
    # add other required actions
    self.menu.popup(pos)

def renameSlot(self, pos):
    print("renaming slot called")
    # get the selected row and column
    row = self.tableView.rowAt(pos.y())
    col = self.tableView.columnAt(pos.x())
    # get the selected cell
    # cell = self.tableView.item(row, col)
    # get the text inside selected cell (if any)
    cellText = cell.text()
    # get the widget inside selected cell (if any)
    widget = self.tableView.cellWidget(row, col)