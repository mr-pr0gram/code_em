import unittest
import bot_id
import slackpi
import wray.slacklib
import chris.slacklib
import joe.slacklib
import homeschool.baron.slacklib
import homeschool.elliot.slacklib
import homeschool.kaleb.slacklib
import homeschool.owen.slacklib
import homeschool.vivian.slacklib

class TestSlackBotFunctions(unittest.TestCase):

    def test_ci(self):
        self.assertTrue(True)

    def test_slack_client(self):
        self.assertTrue(bot_id.get_id() == None)

    def test_slack_pi(self):
        self.assertTrue(slackpi.handle_command("","") == None)

    def test_wray_handler(self):
        self.assertFalse(wray.slacklib.handle_command('') == None)
        self.assertTrue(len(wray.slacklib.handle_command(
            wray.slacklib.COMMAND1)) > 1)
        resp = wray.slacklib.handle_command(wray.slacklib.COMMAND4)
        print(resp)
        self.assertTrue(len(resp) > 1)

    def test_chris_handler(self):
        self.assertFalse(chris.slacklib.handle_command('') == None)
        self.assertTrue(len(chris.slacklib.handle_command(
            chris.slacklib.COMMAND1)) > 1)
    
    def test_joe_handler(self):
        self.assertFalse(joe.slacklib.handle_command('') == None)
        self.assertTrue(joe.slacklib.handle_command(
            joe.slacklib.COMMAND1) == "Just barely..." )
        self.assertTrue(slackpi.handle_command(
            joe.slacklib.COMMAND1,"") == None)
        #self.assertFalse(joe.slacklib.handle_command('green led on') == None)

    def test_baron_handler(self):
        self.assertFalse(homeschool.baron.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.baron.slacklib.handle_command(
            homeschool.baron.slacklib.COMMAND1)) > 1)

    def test_elliot_handler(self):
        self.assertFalse(homeschool.elliot.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.elliot.slacklib.handle_command(
            homeschool.elliot.slacklib.COMMAND1)) > 1)

    def test_kaleb_handler(self):
        self.assertFalse(homeschool.kaleb.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.kaleb.slacklib.handle_command(
            homeschool.kaleb.slacklib.COMMAND1)) > 1)

    def test_owen_handler(self):
        self.assertFalse(homeschool.owen.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.owen.slacklib.handle_command(
            homeschool.owen.slacklib.COMMAND1)) > 1)

    def test_vivian_handler(self):
        self.assertFalse(homeschool.vivian.slacklib.handle_command('') == None)
        self.assertTrue(len(homeschool.vivian.slacklib.handle_command(
            homeschool.vivian.slacklib.COMMAND1)) > 1)

    def test_new_command_handler(self):
        self.assertTrue(wray.slacklib.handle_command("new command: how are you?, i'm fine thank you") == 'ok')
        self.assertTrue(wray.slacklib.handle_command('how are you?') == "i'm fine thank you")
        self.assertTrue(wray.slacklib.handle_command('del command: how are you?') == 'ok')



if __name__ == '__main__':
    unittest.main()
