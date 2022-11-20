
class Stylesheet():
  @staticmethod
  def value():
    return """
    QWidget#mainView QGroupBox {
      border: 0;
    }

    QWidget#mainView QMenu { 
      color: rgb(0, 0, 0);
    }

    QWidget#mainView QLabel {
      color: rgb(255, 245, 255);
      font-weight: bold;
    }

    QWidget#mainView QLabel#applicationName {
      font-size: 18px;
    }

    QWidget#mainView QLabel QToolTip {
      color: rgb(0, 0, 0);
      font-size: 14px;
      opacity: 224;
    }
    """