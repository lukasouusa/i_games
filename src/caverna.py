"""
############################################################
Caverna - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/11/04
:Status: This is a "work in progress"
:Revision: 0.1.3
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.

Caverna é um jogo de aventuras em uma caverna.
"""
CAVEX = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernax.jpg"
CAVEZ = "https://dl.dropboxusercontent.com/u/1751704/labase/caverna/img/cavernaz.jpg"

class Caverna:
    """Uma caverna com cameras tuneis e habitantes. :ref:`caverna`
    """
    def __init__(self, gui):
        """Initializes builder and gui. """
        self.doc = gui.DOC
        self.html = gui.HTML
        self.camera = {}
        self.tunel = {}
        self.heroi = None
        self.main = self.doc['main']

    def cria_caverna(self):
        """Cria a caverna e suas partes."""
        self.camara = Camara (self.html, "Camara0", self).cria_camara()
        # criando um tunel
        tunel_1 = Tunel (self.html, "Tunel0", self.camara).cria_tunel()
        tunel_2 = Tunel (self.html, "Tunel1", self.camara).cria_tunel()
        tunel_3 = Tunel (self.html, "Tunel2", self.camara).cria_tunel()
        #self.main <= self.camara.div
        return self

class Camara:
    """Uma camera da caverna com tuneis e habitantes. :ref:'camara'
    """
    def __init__(self, html, nome , lugar):
        """Inicia a camara"""
        self.html, self.nome, self.lugar = html, nome, lugar
        self.passagem = self.div = None
        self.tunel = {}

    def cria_camara(self):
        """Cria a camara e suas partes"""
        self.div = self.html.DIV()
        self.passagem = self.html.DIV()
        self.div <= self.passagem
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEX
        self.div.style.widht = 1000
        self.div.style.height = 800
        self.div.text = "Caverna do Carlo"
        self.div <= self.passagem
        self.lugar.main <= self.div
        return self

class Tunel:
    """Um tunel da caverna que liga camaras :ref:'tunel'
    """
    def __init__(self, html, nome , lugar):
        """Inicia a camara"""
        self.html, self.nome, self.lugar = html, nome, lugar
        self.passagem = self.div = None
        self.tunel = {}

    def cria_tunel(self):
        """Cria a tunel e suas partes"""
        self.div = self.html.DIV()
        self.passagem = self.html.DIV()
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEZ
        self.div.style.widht = 1000
        self.div.style.height = 800
        self.div.text = "Caverna do Carlo"
        self.div <= self.passagem
        return self

def main(gui):
    print('Caverna 0.1.0')
    caverna = Caverna(gui).cria_caverna()
