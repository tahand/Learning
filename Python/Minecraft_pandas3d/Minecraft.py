from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        grassBlock = loader.loadModel("grass-block.glb")
        grassBlock.reparentTo(render)





game = MyGame()
game.run()