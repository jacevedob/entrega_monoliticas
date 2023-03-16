from entregasalpes.modulos.unificacion_pedidos.dominio.eventos import UnificacionPedidosCreada, UnificacionPedidosCancelada
from entregasalpes.seedwork.aplicacion.handlers import Handler
from entregasalpes.modulos.unificacion_pedidos.infraestructura.despachadores import Despachador


class HandlerUnificacionPedidosIntegracion(Handler):

    @staticmethod
    def handle_unificacion_pedidos_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

    @staticmethod
    def handle_unificacion_pedidos_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

