import pygame
import random
import math
import sys


class Store_Floor:
    def __init__(self, screen, x, y, map):
        self.screen = screen
        self.x = x
        self.y = y
        self.map = map

    def draw(self):
        self.screen.blit(self.map, (self.x, self.y))


class Departments:
    def __init__(self, screen, x, y, width, height, department_name, items):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.deparment_name = department_name
        self.items = items

    def draw(self):
        self.deparment_area = pygame.Rect(self.x, self.y, self.width, self.height)

    def locator(self, protagonist):

        if self.x < protagonist.x < self.x - self.width:
            if self.y > protagonist.y > self.y + self.height:
                return True
                # print(shoe_area.x - shoe_area.width, shoe_area.y + shoe_area.height)
                # print(shoe_area.width, shoe_area.height)
                # print(shoe_area.x, shoe_area.y)
                # print(ness.x, ness.y)
            else:
                return False
        else:
            return False

    # TODO: Over the break, I will finish my initial goal. My initial goal was to buy objects in the store.
    def items_window(self):
        pass


class Protagonist:
    def __init__(self, screen, protagonist, flipped_protagonist, x, y):
        self.screen = screen
        self.protagonist = protagonist
        self.flipped_protagonist = flipped_protagonist
        self.x = x
        self.y = y
        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]

    def draw(self):
        self.screen.blit(self.protagonist, (self.width // 2, self.height // 2))

        # count = 2
        # while True:
        #     if count % 2 == 0:
        #         self.screen.blit(self.protagonist, (self.width // 2, self.height // 2))
        #     else:
        #         self.screen.blit(self.flipped_protagonist, (self.width // 2, self.height // 2))


# TODO: When I have time over the break, I will create other shoppers that you can interact with.
class Other_Shoppers:
    def __init__(self):
        pass


class Checklist:
    def __init__(self, screen):
        self.screen = screen
        self.list = ["Cotton Bed Sheets", "Microfiber Bed Sheets", "Polyester Bed Sheets", "Men's Dress Pants",
                     "Men's Sweatpants", "Men's Carpenter Pants", "Men's T-Shirt", "Men's Polo Shirt",
                     "Men's Long_Sleeve T-Shirt", "Men's Button-Front Shirt", "60'' Television", "75'' Television",
                     "40'' Television", "LXI Series Boombox", "LXI Series Stereo Dual Cassette System",
                     "LXI Series Speakers", "Women's Split Neck Shirt", "Women's Sweatshirt", "Women's Flannel Shirt",
                     "Women's V-Neck Dress", "Women's Sarong Dress", "Women's Sheath Dress",
                     "Women's Straight Leg Jeans", "Women's Junior Leggings", "Women's Roebuck and Co Slim Boot Jeans",
                     "Proform Treadmill", "Proform Elliptical", "Proform Indoor Cycle", "Craftsman Lawnmower",
                     "Craftsman Weed Wacker", "Kenmore Gas Grill", "Kenmore Top-Freezer Refrigerator",
                     "Kenmore Side-by-Side Refrigerator", "LG Side-by-Side Refrigerator", "Kenmore 24'' Dishwasher",
                     "Kenmore Top Loader Washer", "Kenmore Front Loader Washer", "Wristlet Wallet", "Satchel Purse",
                     "Crossbody Purse", "Small Tote Purse", "Round Diamond Ring", "Diamond Engagement Ring",
                     "Stainless Steel Watch", "Chronograph Watch", "Dial Bracelet Watch", "Gold Mesh Watch",
                     "Men's Soft Toe Work Boot", "Men's Steel Toe Work Boot", "Women's Sweater Boot",
                     "Women's Heeled Loafer", "Women's Sneaker", "Diehard Automotive Battery", "Spark Plugs",
                     "Craftsman 320-Piece Tool Set", "Craftsman Impact Wrench", "Craftsman 450-Piece Tool Set",
                     "Craftsman 3-Piece Wrench Set", "Craftsman Gas Chainsaw",
                     "Craftsman Chain-Drive Garage Door Opener"]
        self.font = pygame.font.Font("prstart.ttf", 11)

    def make_checklist(self):
        self.checklist = []
        for k in range(5):
            self.checklist += [self.list[random.randint(0, len(self.list) - 1)]]
        print(self.checklist)

    def draw(self):
        checklist_string = "Checklist: "
        for k in range(len(self.checklist)):
            checklist_string += "{}, ".format(str(self.checklist[k]))
        checklist_image = self.font.render(checklist_string, True, (0, 0, 0), (255, 255, 122))
        self.screen.blit(checklist_image, (5, 5))


class Locator:
    def __init__(self, screen, current_location):
        self.screen = screen
        self.current_location = current_location
        self.font = pygame.font.Font("prstart.ttf", 15)

        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]

    def draw(self):
        location_string = "Location: " + str(self.current_location)
        location_image = self.font.render(location_string, True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(location_image, (0, self.height - 30))

class Department:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pass




class Radio:
    def __init__(self):
        self.lights_on = pygame.mixer.Sound("Lights On.wav")
        self.three_to_five = pygame.mixer.Sound("Three to Five.wav")
        self.time_magazine = pygame.mixer.Sound("Time Magazine.wav")
        self.radio_list = [pygame.mixer.Sound("Lights On.wav"), pygame.mixer.Sound("Three to Five.wav"),
                           pygame.mixer.Sound("Time Magazine.wav")]

    def queue(self):
        # TODO: Currently a work in progress. Trying to make a queue.
        # k = 0
        # while True:
        #     self.lights_on.play()
        #     if pygame.mixer.music.get_endevent():
        #         if k == 1:
        #             self.three_to_five.play()
        #         elif k == 2:

        self.lights_on.play(-1)
        # pygame.mixer.music.queue("Three to Five.wav")
        # pygame.mixer.music.queue("Time Magazine.wav")
        pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Shopping Simulator')

    clock = pygame.time.Clock()

    store_floor_image = pygame.image.load("Store Floor.png")
    store_floor_image = pygame.transform.scale(store_floor_image, (6084, 8112))
    store_floor = Store_Floor(screen, 75, -4500, store_floor_image)
    # store_floor = Store_Floor(screen, 70, -2850, store_floor_image)

    ness_image = pygame.image.load("ness walking.png")
    ness_image = pygame.transform.scale(ness_image, (120, 124))
    ness_image_reflect = pygame.transform.flip(ness_image, True, False)
    ness = Protagonist(screen, ness_image, ness_image_reflect, 75, -4500)

    home_area = Departments(screen, 1700, -150, -700, -1950, "Home Department",
                            ["Cotton Bed Sheets", "Microfiber Bed Sheets", "Polyester Bed Sheets"])
    clothing_area_1 = Departments(screen, 2625, -150, -2075, -1150, "Clothing Department",
                                  ["Men's Dress Pants", "Men's Sweatpants", "Men's Carpenter Pants"])
    clothing_area_2 = Departments(screen, 2625, -1300, -1125, -1550, "Clothing Department",
                                  ["Men's T-Shirt", "Men's Polo Shirt", "Men's Long_Sleeve T-Shirt",
                                   "Men's Button-Front Shirt"])
    electronics_area = Departments(screen, 3750, -1300, -950, -1550, "Electronics Department",
                                   ["60'' Television", "75'' Television", "40'' Television", "LXI Series Boombox",
                                    "LXI Series Stereo Dual Cassette System", "LXI Series Speakers"])
    clothing_area_3 = Departments(screen, 1700, -3050, -2350, -1300, "Clothing Department",
                                  ["Women's Split Neck Shirt", "Women's Sweatshirt", "Women's Flannel Shirt",
                                   "Women's V-Neck Dress", "Women's Sarong Dress", "Women's Sheath Dress",
                                   "Women's Straight Leg Jeans", "Women's Junior Leggings",
                                   "Women's Roebuck and Co Slim Boot Jeans"])
    fitness_area = Departments(screen, 4250, -5250, -450, -1100, "Fitness Department",
                               ["Proform Treadmill", "Proform Elliptical", "Proform Indoor Cycle"])
    outdoor_area = Departments(screen, 4250, -4150, -450, -1250, "Outdoor Department",
                               ["Craftsman Lawnmower", "Craftsman Weed Wacker", "Kenmore Gas Grill"])
    appliance_area = Departments(screen, 1700, -5750, -2350, -1250, "Appliance Department",
                                 ["Kenmore Top-Freezer Refrigerator", "Kenmore Side-by-Side Refrigerator",
                                  "LG Side-by-Side Refrigerator", "Kenmore 24'' Dishwasher",
                                  "Kenmore Top Loader Washer", "Kenmore Front Loader Washer"])
    accessory_area = Departments(screen, 750, -4600, -850, -2400, "Accessory Department",
                                 ["Wristlet Wallet", "Satchel Purse", "Crossbody Purse", "Small Tote Purse"])
    jewelry_area = Departments(screen, 70, -4600, -620, -2600, "Jewelry Department",
                               ["Round Diamond Ring", "Diamond Engagement Ring", "Stainless Steel Watch",
                                "Chronograph Watch", "Dial Bracelet Watch", "Gold Mesh Watch"])
    shoe_area = Departments(screen, 70, -2850, -620, -1500, "Shoe Department",
                            ["Men's Soft Toe Work Boot", "Men's Steel Toe Work Boot", "Women's Sweater Boot",
                             "Women's Heeled Loafer", "Women's Sneaker"])
    automotive_area = Departments(screen, 600, -2200, -1000, -1600, "Automotive Department",
                                  ["Diehard Automotive Battery", "Spark Plugs"])
    tool_area = Departments(screen, 1700, -4600, -2350, -1150, "Tool Department",
                            ["Craftsman 320-Piece Tool Set", "Craftsman Impact Wrench", "Craftsman 450-Piece Tool Set",
                             "Craftsman 3-Piece Wrench Set", "Craftsman Gas Chainsaw",
                             "Craftsman Chain-Drive Garage Door Opener"])

    checklist = Checklist(screen)
    checklist.make_checklist()

    location = Locator(screen, "Walking the Aisles... ")

    radio1 = Radio()
    radio1.queue()

    walking_sound = pygame.mixer.Sound("walking sound.wav")
    walking_sound.play(-1)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] and store_floor.y < -150:
            store_floor.y += 5
            home_area.y -= 5
            clothing_area_1.y -= 5
            clothing_area_2.y -= 5
            electronics_area.y -= 5
            clothing_area_3.y -= 5
            fitness_area.y -= 5
            outdoor_area.y -= 5
            appliance_area.y -= 5
            accessory_area.y -= 5
            jewelry_area.y -= 5
            shoe_area.y -= 5
            automotive_area.y -= 5
            tool_area.y -= 5

        if pressed_keys[pygame.K_a] and store_floor.x < 150:
            store_floor.x += 5
            home_area.x += 5
            clothing_area_1.x += 5
            clothing_area_2.x += 5
            electronics_area.x += 5
            clothing_area_3.x += 5
            fitness_area.x += 5
            outdoor_area.x += 5
            appliance_area.x += 5
            accessory_area.x += 5
            jewelry_area.x += 5
            shoe_area.x += 5
            automotive_area.x += 5
            tool_area.x += 5

        if pressed_keys[pygame.K_s] and store_floor.y > -7500:
            store_floor.y -= 5
            home_area.y += 5
            clothing_area_1.y += 5
            clothing_area_2.y += 5
            electronics_area.y += 5
            clothing_area_3.y += 5
            fitness_area.y += 5
            outdoor_area.y += 5
            appliance_area.y += 5
            accessory_area.y += 5
            jewelry_area.y += 5
            shoe_area.y += 5
            automotive_area.y += 5
            tool_area.y += 5

        if pressed_keys[pygame.K_d] and store_floor.x > -4700:
            store_floor.x -= 5
            home_area.x -= 5
            clothing_area_1.x -= 5
            clothing_area_2.x -= 5
            electronics_area.x -= 5
            clothing_area_3.x -= 5
            fitness_area.x -= 5
            outdoor_area.x -= 5
            appliance_area.x -= 5
            accessory_area.x -= 5
            jewelry_area.x -= 5
            shoe_area.x -= 5
            automotive_area.x -= 5
            tool_area.x -= 5

        # print(store_floor.x, store_floor.y)
        # if pressed_keys[pygame.MOUSEBUTTONDOWN]:
        #     items_window()

        # if fitness_area.x < ness.x < fitness_area.x - fitness_area.width:
        #     if fitness_area.y > ness.y > fitness_area.y + fitness_area.height:
        #         location.current_location = fitness_area.deparment_name
        # print(shoe_area.x - shoe_area.width, shoe_area.y + shoe_area.height)
        # print(shoe_area.width, shoe_area.height)
        # print(shoe_area.x, shoe_area.y)
        # print(ness.x, ness.y)
        #     else:
        #         location.current_location = "Walking the Aisles... "
        #
        # else:
        #     location.current_location = "Walking the Aisles... "

        location.current_location = "Walking the Aisles... "
        if home_area.locator(ness):
            location.current_location = home_area.deparment_name
        elif clothing_area_1.locator(ness):
            location.current_location = clothing_area_1.deparment_name
        elif clothing_area_2.locator(ness):
            location.current_location = clothing_area_2.deparment_name
        elif electronics_area.locator(ness):
            location.current_location = electronics_area.deparment_name
        elif clothing_area_3.locator(ness):
            location.current_location = clothing_area_3.deparment_name
        elif fitness_area.locator(ness):
            location.current_location = fitness_area.deparment_name
        elif outdoor_area.locator(ness):
            location.current_location = outdoor_area.deparment_name
        elif appliance_area.locator(ness):
            location.current_location = appliance_area.deparment_name
        elif accessory_area.locator(ness):
            location.current_location = accessory_area.deparment_name
        elif jewelry_area.locator(ness):
            location.current_location = jewelry_area.deparment_name
        elif shoe_area.locator(ness):
            location.current_location = shoe_area.deparment_name
        elif automotive_area.locator(ness):
            location.current_location = automotive_area.deparment_name
        elif tool_area.locator(ness):
            location.current_location = tool_area.deparment_name

        screen.fill(pygame.Color('BLACK'))

        store_floor.draw()
        ness.draw()

        home_area.draw()
        clothing_area_1.draw()
        clothing_area_2.draw()
        electronics_area.draw()
        clothing_area_3.draw()
        fitness_area.draw()
        outdoor_area.draw()
        appliance_area.draw()
        accessory_area.draw()
        jewelry_area.draw()
        shoe_area.draw()
        automotive_area.draw()
        tool_area.draw()

        checklist.draw()

        # print(type(location))
        location.draw()

        pygame.display.update()


main()
