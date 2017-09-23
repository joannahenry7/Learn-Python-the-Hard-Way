from rooms import *


class Engine(object):

    scenes = {
        'begin': Begin(), 
        'fluffy_room': FluffyRoom(),
        'devils_snare_room': DevilsSnareRoom(),
        'key_room': KeyRoom(),
        'chess_room': ChessRoom(),
        'troll_room': TrollRoom(),
        'potion_room': PotionRoom(),
        'mirror_room': MirrorRoom(),
        'final_boss_battle': FinalBossBattle(),
        'failed': Failed(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = self.scenes.get(scene_name)
        return val

    def play(self):
        current_scene = self.next_scene(self.start_scene)
        last_scene = self.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.next_scene(next_scene_name)

        current_scene.enter()
