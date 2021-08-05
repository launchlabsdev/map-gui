import os

from PySide2.QtCore import QEventLoop, QUrl
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView ,QWebEnginePage

class MapWidget(QWebEngineView):

    @property
    def page(self):
        return self._page

    @property
    def channel(self):
        return self._channel

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._page = QWebEnginePage()
        self.setPage(self._page)
        self._channel = QWebChannel()
        self._page.setWebChannel(self._channel)
        self._loadPage()

    def _loadPage(self):
        html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geojson.html')
        init_loop = QEventLoop()
        self._page.loadFinished.connect(init_loop.quit)
        self._page.load(QUrl().fromLocalFile(html_path))
        init_loop.exec_()

