
class Stylesheet():
  @staticmethod
  def value():
    return """
    * {
      color: rgb(255, 245, 255);
    }

    QLabel {
      font-weight: bold;
    }

    QLabel QToolTip {
      color: rgb(0, 0, 0);
      font-size: 14px;
      opacity: 224;
    }
    """