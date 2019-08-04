from mox.controllers.controller import Controller


def test_resource_name():
    class MonkeysController(Controller):
        pass

    controller = MonkeysController()

    assert controller.resource_name == 'monkeys'
