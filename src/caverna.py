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
CAMARAS = [0, 1, 2, 3]
TUNEIS = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (1, 3)]
#[par for par in TUNEIS if 0 in par]


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
        self.camara = None
        self.sala = None
        self.esconde = self.html.DIV()

    def movimenta(self, sala):
        self.esconde <= self.sala.div
        self.main <= sala.div
        self.sala = sala

    def cria_caverna(self):
        """Cria a caverna e suas partes."""
        self.camara = {
            'camara_%d' % a:
            Camara(self.html, "camara_%d" % a, self).cria_camara()
            for a in CAMARAS
        }
        #criando uma colecao de tuneis
        self.sala = self.camara['camara_0']
        self.main <= self.sala.div

        self.tunel = {
            'tunel_ %d_%d' % par_ordenado:
            Tunel(self.html, "tunel_%d_%d" % par_ordenado, self.sala,
                  par_ordenado, self) .cria_tunel()
            for par_ordenado in TUNEIS
        }
        return self


class Camara:
    """Uma camera da caverna com tuneis e habitantes. :ref:'camara'
    """
    def __init__(self, html, nome, lugar):
        """Inicia a camara"""
        self.html, self.nome, self.lugar = html, nome, lugar
        self.passagem = self.div = None
        self.tunel = {}

    def cria_camara(self):
        """Cria a camara e suas partes."""
        self.div = self.html.DIV()
        self.passagem = self.html.DIV()
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEX
        self.div.style.width = 1200
        self.div.style.height = 655
        self.div.text = "Caverna da Jess %s" % self.nome
        self.div <= self.passagem
        self.lugar.esconde <= self.div
        return self


class Tunel:
    """Um tunel da caverna que liga camaras. :ref: 'tunel'
    """
    def __init__(self, html, nome, lugar, par_ordenado, caverna):
        """Inicia a tunel."""
        self.html, self.nome, self.caverna = html, nome, caverna
        self.lugar, self.par_ord = lugar, par_ordenado
        self.entrada_camara = self.entrada = self.passagem = self.div = None
        self.camara = {}
        self.lugar0 = self.caverna.camara['camara_%d' % par_ordenado[0]]
        self.lugar1 = self.caverna.camara['camara_%d' % par_ordenado[1]]

    def movimenta(self, ev):
        print(ev.target.ID)
        self.caverna.movimenta(self)

    def sai_tunel0(self, ev):
        print(ev.target.ID)
        self.caverna.movimenta(self.lugar0)

    def sai_tunel1(self, ev):
        print(ev.target.ID)
        self.caverna.movimenta(self.lugar1)

    def cria_saida(self):
        """Cria uma saida desse tunel."""
        estilo = dict(
            width="50%", height=300, Float='left')
        self.entrada_camara = self.html.DIV(
            Id='entra_' + self.nome,  style=estilo
        )
        self.entrada_camara.onclick = self.sai_tunel0
        self.passagem <= self.entrada_camara

        estilo = dict(
            width="50%", height=300, Float='left')
        self.entrada_camara = self.html.DIV(
            Id='entra_' + self.nome,  style=estilo
        )
        self.entrada_camara.onclick = self.sai_tunel1
        self.passagem <= self.entrada_camara

    def cria_entrada(self, saida1):
        estilo = dict(
            width="33.33%", height=300, Float='left')
        entrada = self.html.DIV(
            Id='entra_' + self.nome, style=estilo
        )
        entrada.onclick = self.movimenta
        saida1.div <= entrada

    def cria_tunel(self):
        """Cria o tunel e suas partes."""
        self.div = self.html.DIV(Id=self.nome)
        self.passagem = self.html.DIV(Id='passa_'+self.nome)
        #camaras = [camara for camara in self.par_ord]
        [self.cria_entrada(self.caverna.camara["camara_%d" % saida])
         for saida in self.par_ord]
        self.div.style.backgroundSize = 'cover'
        self.div.style.backgroundImage = 'url(%s)' % CAVEZ
        self.div.style.width = 1200
        self.div.style.height = 655
        self.div.text = "Caverna da Jess %s" %self.nome
        self.div <= self.passagem
        self.cria_saida()
        return self


def main(gui):
        print('Caverna 0.1.0')
        Caverna(gui).cria_caverna()