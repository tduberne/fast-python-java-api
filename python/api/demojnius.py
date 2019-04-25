import jnius


ProtobufAdapter = jnius.autoclass('ch.dubernet.demopythonapi.simulation.api.ProtobufAdapter')
ProtobufBufferedAdapter = jnius.autoclass('ch.dubernet.demopythonapi.simulation.api.ProtobufBufferedAdapter')

from api.protobuf.JumpEvent_pb2 import JumpEvent
from api.protobuf.SingEvent_pb2 import SingEvent
from api.protobuf.SpeakEvent_pb2 import SpeakEvent
from api.protobuf.EventBuffer_pb2 import EventBuffer, EventContainer


def create_event_handler(handler):
    """
    Annotation to annotate python classes that "implement" and event handler

    :param handler:
    :return:
    """
    class ProtobufHandler(jnius.PythonJavaClass):
        __javainterfaces__ = ['ch/dubernet/demopythonapi.simulation.api.ProtobufEventHandler']

        @jnius.java_method('()V')
        def notifyStart(self):
            if hasattr(handler, "notifyStart"):
                handler.notifyStart()

        @jnius.java_method('()V')
        def notifyEnd(self):
            if hasattr(handler, "notifyEnd"):
                handler.notifyEnd()

        @jnius.java_method('([B)V')
        def handleJumpEventMessage(self, message):
            if hasattr(handler, "handleJumpEvent"):
                event = JumpEvent()
                event.ParseFromString(bytearray(message))
                handler.handleJumpEvent(event)

        @jnius.java_method('([B)V')
        def handleSingEventMessage(self, message):
            if hasattr(handler, "handleSingEvent"):
                event = SingEvent()
                event.ParseFromString(bytearray(message))
                handler.handleSingEvent(event)

        @jnius.java_method('([B)V')
        def handleSpeakEventMessage(self, message):
            if hasattr(handler, "handleSpeakEvent"):
                event = SpeakEvent()
                event.ParseFromString(bytearray(message))
                handler.handleSpeakEvent(event)

    impl = ProtobufHandler()
    return ProtobufAdapter(impl)

def create_buffered_event_handler(handler, buffer_size):
    """
    Annotation to annotate python classes that "implement" and event handler

    :param handler:
    :return:
    """
    class ProtobufHandler(jnius.PythonJavaClass):
        __javainterfaces__ = ['ch/dubernet/demopythonapi.simulation.api.ProtobufEventBufferHandler']

        @jnius.java_method('()V')
        def notifyStart(self):
            if hasattr(handler, "notifyStart"):
                handler.notifyStart()

        @jnius.java_method('()V')
        def notifyEnd(self):
            if hasattr(handler, "notifyEnd"):
                handler.notifyEnd()

        @jnius.java_method('([B)V')
        def handleEventBuffer(self, message):
            buffer = EventBuffer()
            buffer.ParseFromString(message[:])

            for event in buffer.events:
                event_type = event.WhichOneof("event")
                if event_type == "jumpEvent" and hasattr(handler, "handleJumpEvent"):
                    handler.handleJumpEvent(event.jumpEvent)
                elif event_type == "singEvent" and hasattr(handler, "handleSingEvent"):
                    handler.handleSingEvent(event.singEvent)
                elif event_type == "speakEvent" and hasattr(handler, "handleSpeakEvent"):
                    handler.handleSpeakEvent(event.speakEvent)

    impl = ProtobufHandler()
    return ProtobufBufferedAdapter(impl, buffer_size)

