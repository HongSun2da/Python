####### class   ######################################
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#     def attack(self, loacation):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, loacation, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if(self.hp <= 0):
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

####### class  상속 ######################################
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         print("{0} 유닛이 생성 되었습니다. [체력 {1}]".format(self.name, self.hp))

# marine1 = Unit("메딕", 40)
# marine2 = Unit("메딕2", 40)

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다. [체력 {1}] [공격력 {2}]".format(self.name, self.hp, self.damage))

#     def attack(self, loacation):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, loacation, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if(self.hp <= 0):
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃1", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

####### class  다중 상속 ######################################
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         print("{0} 유닛이 생성 되었습니다. [체력 {1}]".format(self.name, self.hp))

# marine1 = Unit("메딕", 40)
# marine2 = Unit("메딕2", 40)

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다. [체력 {1}] [공격력 {2}]".format(self.name, self.hp, self.damage))

#     def attack(self, loacation):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, loacation, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if(self.hp <= 0):
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃1", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#         print("Flyable 생성 [속도 {0}]".format(self.flying_speed))

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아 갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "12시")
# valkyrie.attack("12시")
# valkyrie.attack("12시")

# valkyrie.damaged(50)
# valkyrie.damaged(50)
# valkyrie.damaged(50)
# valkyrie.damaged(50)


####### class  연산자 오버로딩 ######################################
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성 되었습니다. [체력 {1}] [속도 {2}]".format(self.name, self.hp, self.speed))

#     def move(self, location):
#         print("[지상 유닛 이동]")    
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [속도 {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다. [체력 {1}] [속도 {2}] [공격력 {3}]".format(self.name, self.hp, self.speed, self.damage))

#     def attack(self, loacation):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, loacation, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if(self.hp <= 0):
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#         print("Flyable 생성 [속도 {0}]".format(self.flying_speed))

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아 갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# vulture.move("11시")

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# battlecruiser.fly(battlecruiser.name, "12시")
# battlecruiser.move("9시")


from random import *
####### Project ######################################
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} : 유닛이 생성 되었습니다. [체력 {self.hp}] [속도 {self.speed}]")

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동(지상) 합니다. [체력 {self.hp}] [속도 {self.speed}]")
    
    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다. [체력 {self.hp}] [속도 {self.speed}]")
        self.hp -= damage
        print(f"{self.name} : [체력 {self.hp}] [속도 {self.speed}]")
        if(self.hp <= 0):
            print(f"{self.name} : 파괴되었습니다.")

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print(f"{self.name} : 유닛이 생성 되었습니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}]")

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격(지상) 합니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다. [체력 {self.hp}] [속도 {self.speed}]")
        self.hp -= damage
        print(f"{self.name} : [체력 {self.hp}] [속도 {self.speed}]")
        if(self.hp <= 0):
            print(f"{self.name} : 파괴되었습니다.")


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
        print(f"{self.name} : 유닛이 생성 되었습니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}]")

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")    

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
        print(f"{self.name} : 유닛이 생성 되었습니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}] [시즈 모드 {self.seize_mode}]")

    def set_seize_mode(self):
        if self.seize_developed == False:
            return

        if self.seize_mode == False:
            #self.damaged *= 2
            self.seize_mode = True
            print(f"{self.name} : 시즈모드로 전환합니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}] [시즈 모드 {self.seize_mode}]")
        else:
            #self.damaged /= 2
            self.seize_mode = False
            print(f"{self.name} : 시즈모드로 해제합니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}] [시즈 모드 {self.seize_mode}]")


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        print("Flyable 생성 [속도 {0}]".format(self.flying_speed))

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아 갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
        print(f"{self.name} : 유닛이 생성 되었습니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}] [크로킹 모드 {self.clocked}]")

    def clocking(self):
        if self.clocked == False:
            self.clocked = True
            print(f"{self.name} : 크로킹 모드로 전환합니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}] [크로킹 모드 {self.clocked}]")
        else:
            self.clocked = False
            print(f"{self.name} : 크로킹 모드로 해제합니다. [체력 {self.hp}] [속도 {self.speed}] [공격력 {self.damage}] [크로킹 모드 {self.clocked}]")


def game_start():
    print("[알람] 새로운 게임을 시작 합니다.")

def game_over():
    print("Player : GG")    
    print("[Player] 님이 게임에서 퇴장하셨습니다.")



game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")


for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()    





