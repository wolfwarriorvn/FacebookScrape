
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt,QRegularExpression
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu
from PySide6.QtWidgets import QWidget
from PySide6.QtSql import QSqlTableModel
from views.ui.widget_custome.table_ui import Ui_widget_table

class AlignDelegateTB(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegateTB, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class CustomProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._filters = dict()

    @property
    def filters(self):
        return self._filters
    
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def setFilter(self, expresion, column):
        if expresion:
            self.filters[column] = expresion
        elif column in self.filters:
            del self.filters[column]
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        for column, expresion in self.filters.items():
            text = self.sourceModel().index(source_row, column, source_parent).data()
            regex = QRegularExpression(
                expresion, QRegularExpression.CaseInsensitiveOption
            )
            if not regex.match(text).hasMatch():
                return False
        return True
    
class TableCustome(QWidget):
    def __init__(self):
        super(TableCustome, self).__init__()
        self.ui = Ui_widget_table()
        self.ui.setupUi(self)

        # Align center text in cell of table
        delegate = AlignDelegateTB(self.ui.tableView)
        self.ui.tableView.setItemDelegate(delegate)
        self.proxy = CustomProxyModel()



