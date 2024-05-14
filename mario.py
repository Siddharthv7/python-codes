class Mario(Entity):
    def __init__(self, x, y, w, h, colour):
        Entity.__init__(self, x, y, w, h, colour)
        self.allStates = {
            "idle":MarioStateIdle(),
            "move":MarioStateMove(),
            "jump":MarioStateJump(),
            "fall":MarioStateFall() }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState

    def update(self, deltaTime):
        if len(self.collidingObjects) > 0:
            self.collide(self.collidingObjects[0])

        self.currState.execute(self, deltaTime)

    def changeState(self, stateID):
        if self.allStates.get(stateID) is None:
            return
        else:
            self.newState = self.allStates.get(stateID)
            self.currState.exitState(self)
            self.prevState = self.currState
            self.currState = self.newState
            self.currState.enterState(self)

    def collide(self, collided):
        if self.currState.name == "jump":
            if type(collided) == GroundBlock:
                self.changeState("fall")

        if self.currState.name == "fall":
            if type(collided) == GroundBlock:
                self.changeState("idle")