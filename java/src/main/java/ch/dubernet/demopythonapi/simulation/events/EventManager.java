package ch.dubernet.demopythonapi.simulation.events;

import java.util.ArrayList;
import java.util.List;

public class EventManager {
    private final List<SpeakEventHandler> speakEventHandlers = new ArrayList<>();
    private final List<SingEventHandler> singEventHandlers = new ArrayList<>();
    private final List<JumpEventHandler> jumpEventHandlers = new ArrayList<>();

    private final List<EventHandler> allHandlers = new ArrayList<>();

    public void addEventHandler(EventHandler handler) {
        allHandlers.add(handler);
        if (handler instanceof SpeakEventHandler) speakEventHandlers.add((SpeakEventHandler) handler);
        if (handler instanceof SingEventHandler) singEventHandlers.add((SingEventHandler) handler);
        if (handler instanceof JumpEventHandler) jumpEventHandlers.add((JumpEventHandler) handler);
    }

    public void handleEvent(Event event) {
        if (event instanceof SpeakEvent) speakEventHandlers.forEach(h -> h.handleEvent((SpeakEvent) event));
        if (event instanceof SingEvent) singEventHandlers.forEach(h -> h.handleEvent((SingEvent) event));
        if (event instanceof JumpEvent) jumpEventHandlers.forEach(h -> h.handleEvent((JumpEvent) event));
    }

    public void handleStartOfSimulation() {
        allHandlers.forEach(EventHandler::notifyStart);
    }

    public void handleEndOfSimulation() {
        allHandlers.forEach(EventHandler::notifyEnd);
    }
}
