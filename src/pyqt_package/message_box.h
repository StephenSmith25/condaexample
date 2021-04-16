class MessageBox {
public:
    MessageBox(QString cppMsg) {
        QMessageBox::information("C++ title", cppMsg)
    }
};