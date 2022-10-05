
class Stylesheet():
  @staticmethod
  def value():
    return """
    QMainWindow#mainView {
      color: rgb(255, 245, 255);
      border: 0;
    }

    QMainWindow#mainView QMenu { 
      color: rgb(0, 0, 0);
    }

    QMainWindow#mainView QLabel {
      font-weight: bold;
    }

    QMainWindow#mainView QLabel#applicationName {
      font-size: 18px;
    }

    QMainWindow#mainView QLabel QToolTip {
      color: rgb(0, 0, 0);
      font-size: 14px;
      opacity: 224;
    }
    """