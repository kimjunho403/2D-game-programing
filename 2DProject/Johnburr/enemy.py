import random
from pico2d import *
import gfw
import gobj
from enemy_bullet import *
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Enemy:
    POSITIONS = [( 1680// 2, 140),( 1680, 140),(0 , 140)]
    ACTIONS = ['Attack','Dead','Idle','Walk']
    images = {}
    FPS = 12
    CHASE_DISTANCE_SQ = 600 ** 2
    IDLE_INTERVAL = 2.0
    def __init__(self, num, x):
        if len(Enemy.images) == 0:
            Enemy.load_all_images()

        self.pos = (x, 140)
        self.delta = 0.1, 0.1
        self.life = 120
        self.dir = 0
        self.power = 1
        self.choice_num = random.randrange(1, num+1)
        self.char = 'red'
        self.action = 'Idle'
        self.speed = 100
        self.fidx = 0
        self.time = 0
        self.shot_speed = 0.6
        self.dead_time = 0
        self.shot_time =0.5
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.player = layer[0]
        self.patrol_order = -1
        self.build_behavior_tree()
        self.init_enemy()

    def init_enemy(self):

        if self.choice_num == 1:
            self.char = 'green'
        elif self.choice_num == 2:
            self.char = 'gray'
        elif self.choice_num == 3:
            self.char = 'red'
        elif self.choice_num == 4:
            self.char = 'blue'
        elif self.choice_num == 5:
            self.char = 'armor'
        self.images = Enemy.load_images(self.char)

        if self.char == 'green':
            self.shot_time = 0.5
            self.speed = 200
            self.power = 1
            self.shot_speed = 0.6
        elif self.char == 'gray':
            self.shot_speed = 0.3
        elif self.char == 'armor':
            self.life = 400
        elif self.char == 'red':
            self.speed = 500
        elif self.char == 'blue':
            self.power = 2



    def find_nearest_pos(self):
        x, y = self.pos
        nearest_dsq = 1000000000
        index = 0
        nearest_index = 0
        for (px, py) in Enemy.POSITIONS:
            dsq = (x-px)**2 + (y-py)**2
            if nearest_dsq > dsq:
                nearest_dsq = dsq
                nearest_index = index
            index += 1
        self.patrol_order = nearest_index
        self.set_patrol_target()

    def set_patrol_target(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
            return BehaviorTree.SUCCESS
        self.set_target(Enemy.POSITIONS[self.patrol_order])
        self.patrol_order = (self.patrol_order + 1) % len(Enemy.POSITIONS)
        return BehaviorTree.SUCCESS

    def set_target(self, target):
        x,y = self.pos
        tx,ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance

    def find_player(self):
        dist_sq = gobj.distance_sq(self.player.pos, self.pos)
        if dist_sq < Enemy.CHASE_DISTANCE_SQ:
            if self.patrol_order >= 0:
                self.patrol_order = -1
                self.action = 'Attack'
            return BehaviorTree.SUCCESS
        else:
            if self.action == 'Attack':
                self.action = 'Idle'
                self.time = 0
            else:
                self.action = 'Walk'

            return BehaviorTree.FAIL


    def follow_patrol_positions(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
        done = self.update_position()
        if done:
            self.set_patrol_target()


    def do_idle(self):
        if self.action != 'Idle':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Enemy.FPS)
        if self.time >= Enemy.IDLE_INTERVAL:
            self.action = 'Walk'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_attack(self):
        if self.action != 'Attack':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Enemy.FPS)
        if self.fidx >= len(self.images['Attack']):
            self.shot_time += gfw.delta_time
            if self.shot_time > self.shot_speed:
                self.shot()
                self.shot_time = 0


        return BehaviorTree.SUCCESS

    def shot(self):
        enemy_bullet = Enemy_Bullet(*self.pos, self.dir, 700)
        gfw.world.add(gfw.layer.enemy_bullet, enemy_bullet)


    def do_dead(self):
        if self.action != 'Dead':
            return BehaviorTree.FAIL

        self.dead_time += gfw.delta_time
        self.fidx = round(self.dead_time * Enemy.FPS)
        if self.fidx >= len(self.images['Dead']):
            self.remove()
        return BehaviorTree.SUCCESS

    @staticmethod
    def load_all_images():
        Enemy.load_images('armor')
        Enemy.load_images('blue')
        Enemy.load_images('green')
        Enemy.load_images('red')
        Enemy.load_images('gray')

    @staticmethod
    def load_images(char):
        if char in Enemy.images:
            return Enemy.images[char]

        images = {}
        count = 0
        file_fmt = '%s/alienfiles/%s/%s (%d).png'
        for action in Enemy.ACTIONS:
            action_images = []
            n = 0
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR, char, action, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Enemy.images[char] = images
        print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        self.bt.run()


    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Enemy.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        done = False
        tx,ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or y < 0 and y <= ty:
            y = ty
            done = True
        self.pos = x,y

        return done

    def remove(self):
        gfw.world.remove(self)

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0


    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] < 0 else ''
        image.composite_draw(0, flip, *self.pos, 60, 120)

    def get_bb(self):

        x,y = self.pos
        return x - 30, y - 60, x + 30, y + 60


    def build_behavior_tree(self):
        self.bt = BehaviorTree.build({
            "name": "PatrolChase",
            "class": SelectorNode,
            "children": [
                {
                    "class": LeafNode,
                    "name": "Idle",
                    "function": self.do_idle,
                },
                {
                    "class": LeafNode,
                    "name": "Dead",
                    "function": self.do_dead,
                },
                {
                    "name": "attack",
                    "class": SequenceNode,
                    "children": [
                        {
                            "class": LeafNode,
                            "name": "Find Player",
                            "function": self.find_player,
                        },
                        {
                            "class": LeafNode,
                            "name": "attack to Player",
                            "function": self.do_attack,
                        },
                    ],
                },
                {
                    "class": LeafNode,
                    "name": "Patrol positions",
                    "function": self.follow_patrol_positions,
                },
            ],
        })

