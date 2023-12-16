import pygame
import sys
import os
import base64
import pymsgbox

from pygame import Color
# Made by awesome poopy ChatGPT
# Initialize Pygame
pygame.init()

# Set up display
width, height = 550, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pyincremental v0.0 - .gg/XdysywUk53")

# Set up Spartan font
font_path = f"{os.getcwd()}\\spartan-regular.ttf"
spartan_font = pygame.font.Font(font_path, 24)
spartan_font_medium = pygame.font.Font(font_path, 18)
small_font = pygame.font.Font(font_path, 14)

# Earning frame
earning_frame_text = "Click the 'Start/Stop' button to earn money."
earning_frame_text_surface = spartan_font.render(earning_frame_text, True, (255, 255, 255))
earning_frame_rect = pygame.Rect(20, 20, width - 40, height - 100)

# Upgrades frame
upgrades_frame_text = "Upgrades Shop"
upgrades_frame_text_surface = spartan_font.render(upgrades_frame_text, True, (255, 255, 255))
upgrades_frame_rect = pygame.Rect(20, 20, width - 40, height - 100)
ai_generated_money_button_rect = pygame.Rect(285, height - 125, 225, 40)
home_games_button_rect = pygame.Rect(30, height - 125, 225, 40)


# Upgrades frame 2
games_button_rect = pygame.Rect(30, height - 125, 225, 40)

# Games frame
games_frame_text = "GameMaker3000"
games_frame_text_surface = spartan_font.render(games_frame_text, True, (255, 255, 255))
games_frame_rect = pygame.Rect(20, 20, width - 40, height - 100)
games_unlocked = False


# Money display
money_surface = spartan_font.render("", True, (255, 255, 255))
money_rect = pygame.Rect(20, height - 63, width - 40, 30)
money_gain = (2 / 60)

# Toggle button in the Upgrades frame
toggle_button_rect = pygame.Rect((width - 225) // 2, 30, 225, 40)

rainbow_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (128, 0, 128)]
current_color_index = 0
current_button_color = pygame.Color(*rainbow_colors[current_color_index])
target_color = pygame.Color(*rainbow_colors[(current_color_index + 1) % len(rainbow_colors)])
transition_start_time = pygame.time.get_ticks()
transition_duration = 1000  # 1000 milliseconds (1 second)

# Button for Next Page
next_page_button_rect_frame2 = pygame.Rect(410, height - 275, 115, 40)
next_page_button_rect_frame3 = pygame.Rect(410, height - 275, 115, 40)

prev_page_button_rect_frame3 = pygame.Rect(25, height - 275, 115, 40)

# Upgrade button
upgrade_button_rect = pygame.Rect(30, height - 125, 225, 40)
upgrade_cost = 25
fraud_purchased = False  # Initially set to False

# Upgrade name and description
upgrade_name = "Fraud"
upgrade_description = "Multiply money gain by 2"
upgrade_name_surface = spartan_font.render(upgrade_name, True, (255, 255, 255))
upgrade_description_surface = small_font.render(upgrade_description, True, (255, 255, 255))  # Smaller font

# File paths
data_directory = os.path.join(os.getcwd(), 'data')
upgrade_file_path = os.path.join(data_directory, 'upgrade1.pyincremental')

# Function to simplify large numbers
def simplify(num):
    magdict = {
        0: "", 1: "K", 2: "M", 3: "B", 4: "T",
        5: "Qd", 6: "Qn", 7: "Sx", 8: "Sp", 9: "Oc", 10: "No",
        11: "Dc", 12: "UDc", 13: "DDc", 14: "TDc", 15: "QdDc", 16: "QnDc", 17: "SxDc", 18: "SpDc", 19: "OcDc", 20: "NoDc",
        21: "Vg", 22: "UVg", 23: "DVg", 24: "TVg", 25: "QdVg", 26: "QnVg", 27: "SxVg", 28: "SpVg", 29: "OcVg", 30: "NoVg",
        31: "Tg", 32: "UTg", 33: "DTg", 34: "TTg", 35: "QdTg", 36: "QnTg", 37: "SxTg", 38: "SpTg", 39: "OcTg", 40: "NoTg",
        41: "qg", 42: "Uqg", 43: "Dqg", 44: "Tqg", 45: "Qdqg", 46: "Qnqg", 47: "Sxqg", 48: "Spqg", 49: "Ocqg", 50: "Noqg",
        51: "Qg", 52: "UQg", 53: "DQg", 54: "TQg", 55: "QdQg", 56: "QnQg", 57: "SxQg", 58: "SpQg", 59: "OcQg", 60: "NoQg",
        61: "sg", 62: "Usg", 63: "Dsg", 64: "Tsg", 65: "Qdsg", 66: "Qnsg", 67: "Sxsg", 68: "Spsg", 69: "Ocsg", 70: "Nosg",
        71: "Sg", 72: "USg", 73: "DSg", 74: "TSg", 75: "QdSg", 76: "QnSg", 77: "SxSg", 78: "SpSg", 79: "OcSg", 80: "NoSg",
        81: "Og", 82: "UOg", 83: "DOg", 84: "TOg", 85: "QdOg", 86: "QnOg", 87: "SxOg", 88: "SpOg", 89: "OcOg", 90: "NoOg",
        91: "Ng", 92: "UNg", 93: "DNg", 94: "TNg", 95: "QdNg", 96: "QnNg", 97: "SxNg", 98: "SpNg", 99: "OcNg", 100: "NoNg",
        101: "Ce", 102: "UCe"
    }
    try:
        magnitude = 0
        while num >= 1000.0:
            magnitude += 1
            num = num / 1000.0
    except:
        return "Infinity"
    try:
        numberstr = str(round(num, 2)) + str(magdict[magnitude])
    except:
        return "Infinity"
    if magnitude == 0:
        numberstr = str(round(num, 1))
    return numberstr

# Function to check if the upgrade is purchased
def check_upgrade():
    global fraud_purchased
    if os.path.exists(upgrade_file_path):
        with open(upgrade_file_path, 'r') as file:
            data = file.read()
            fraud_purchased = base64.b64decode(data).decode() == "True"

# Function to purchase the upgrade
def purchase_upgrade():
    global money, fraud_purchased
    if money >= upgrade_cost and not fraud_purchased:
        money -= upgrade_cost
        fraud_purchased = True
        with open(upgrade_file_path, 'w') as file:
            data = base64.b64encode("True".encode()).decode()
            file.write(data)
    elif money <= upgrade_cost:
        pymsgbox.alert(text="you don't have enough money to buy this :(", title='oh no!', button='OK')

# Initialize variables
money = 0
counting = True
games_counting = True
current_frame = 1

# Create a button rectangle for Start/Stop
start_stop_button_rect = pygame.Rect(30, height - 220, 225, 40)

# Create a button rectangle for Upgrades
upgrades_button_rect = pygame.Rect(30, height - 170, 225, 40)

# File path for money!!
money_file_path = os.path.join(data_directory, 'money.pyincremental')
games_file_path = os.path.join(data_directory, 'games.pyincremental')

# Load money from the file if it exists
if os.path.exists(money_file_path):
    with open(money_file_path, 'r') as money_file:
        encoded_money_data = money_file.read()
        try:
            decoded_money_data = base64.b64decode(encoded_money_data).decode()
            money = float(decoded_money_data)
        except (base64.binascii.Error, ValueError):
            money = 0.0
else:
    # Set initial money value if the file doesn't exist
    money = 0.0

if os.path.exists(games_file_path):
    with open(games_file_path, 'r') as games_file:
        encoded_games_data = games_file.read()
        try:
            decoded_games_data = base64.b64decode(encoded_games_data).decode()
            games = int(decoded_games_data)
        except (base64.binascii.Error, ValueError):
            games = 0
else:
    games = 0

# Upgrade 2 variables
upgrade2_file_path = os.path.join(data_directory, 'upgrade2.pyincremental')
upgrade2_cost = 100
ai_generated_money_purchased = False

# Upgrade 2 name and description
upgrade2_name = "AI Generated Money"
upgrade2_description = "Boosts money gain by x10"
upgrade2_name_surface = spartan_font.render(upgrade2_name, True, (255, 255, 255))
upgrade2_description_surface = small_font.render(upgrade2_description, True, (255, 255, 255))

# Upgrade 3 variables
upgrade3_file_path = os.path.join(data_directory, 'upgrade3.pyincremental')
upgrade3_cost = 2500

# Upgrade 3 name and description
upgrade3_name = "Games"
upgrade3_description = "Unlock a new currency & a button"
upgrade3_name_surface = spartan_font.render(upgrade3_name, True, (255, 255, 255))
upgrade3_description_surface = small_font.render(upgrade3_description, True, (255, 255, 255))

# Upgrade 4 variables
upgrade4_file_path = os.path.join(data_directory, 'upgrade4.pyincremental')
upgrade4_cost = 50000
titanium_cash_purchased = False

# Upgrade 4 name and description
upgrade4_name = "Titanium Cash"
upgrade4_description = "Multiply cash gain by 500"
upgrade4_name_surface = spartan_font.render(upgrade3_name, True, (255, 255, 255))
upgrade4_description_surface = small_font.render(upgrade3_description, True, (255, 255, 255))

def check_upgrade2():
    global ai_generated_money_purchased
    if os.path.exists(upgrade2_file_path):
        with open(upgrade2_file_path, 'r') as file:
            data = file.read()
            ai_generated_money_purchased = base64.b64decode(data).decode() == "True"

# Function to purchase the AI Generated Money upgrade
def purchase_upgrade2():
    global money, ai_generated_money_purchased
    if money >= upgrade2_cost and not ai_generated_money_purchased:
        money -= upgrade2_cost
        ai_generated_money_purchased = True
        with open(upgrade2_file_path, 'w') as file:
            data = base64.b64encode("True".encode()).decode()
            file.write(data)
    elif money <= upgrade2_cost:
        pymsgbox.alert(text="you don't have enough money to buy this :(", title='oh no!', button='OK')


def handle_games_button_click():
    if isunlocked():
        return
    else:
        purchase_upgrade3()
        print('Games are not unlocked, purchased upgrade')

def check_upgrade3():
    global games_unlocked
    if os.path.exists(upgrade3_file_path):
        with open(upgrade3_file_path, 'r') as file:
            data = file.read()
            games_unlocked = base64.b64decode(data).decode() == "True"

def purchase_upgrade3():
    global money, games_unlocked
    if money >= upgrade3_cost and not games_unlocked:
        money -= upgrade3_cost
        games_unlocked = True
        with open(upgrade3_file_path, 'w') as upgrade3_file:
            data = base64.b64encode(str(games_unlocked).encode()).decode()
            upgrade3_file.write(data)
            print("Upgrade 3 purchased and file updated")  # Add this line
    elif money <= upgrade3_cost:
        pymsgbox.alert(text="you don't have enough money to buy this :(", title='oh no!', button='OK')

def check_upgrade4():
    global titanium_cash_purchased
    if os.path.exists(upgrade4_file_path):
        with open(upgrade4_file_path, 'r') as file:
            data = file.read()
            titanium_cash_purchased = base64.b64decode(data).decode() == "True"

# Function to purchase the AI Generated Money upgrade
def purchase_upgrade4():
    global money, titanium_cash_purchased
    if money >= upgrade4_cost and not titanium_cash_purchased:
        money -= upgrade4_cost
        titanium_cash_purchased = True
        with open(upgrade4_file_path, 'w') as file:
            data = base64.b64encode("True".encode()).decode()
            file.write(data)
    elif money <= upgrade4_cost:
        pymsgbox.alert(text="you don't have enough money to buy this :(", title='oh no!', button='OK')

def isunlocked():
    global games_unlocked
    if games_unlocked:
        return True
    else:
        return False
    
def save_game():
    with open(money_file_path, 'w') as money_file:
        money_data = base64.b64encode(str(money).encode()).decode()
        money_file.write(money_data)

    with open(games_file_path, 'w') as games_file:
        games_data = base64.b64encode(str(round(games)).encode()).decode()
        games_file.write(games_data)

    with open(upgrade_file_path, 'w') as upgrade_file:
        data = base64.b64encode(str(fraud_purchased).encode()).decode()
        upgrade_file.write(data)

    with open(upgrade2_file_path, 'w') as upgrade2_file:
        data = base64.b64encode(str(ai_generated_money_purchased).encode()).decode()
        upgrade2_file.write(data)

    with open(upgrade3_file_path, 'w') as upgrade3_file:
        data = base64.b64encode(str(games_unlocked).encode()).decode()
        upgrade3_file.write(data)

    with open(upgrade4_file_path, 'w') as upgrade4_file:
        data = base64.b64encode(str(titanium_cash_purchased).encode()).decode()
        upgrade4_file.write(data)

save_timer = pygame.time.get_ticks() + 1000

# Run the game loop
while True:
    # Inside the while loop
    check_upgrade()
    check_upgrade2()
    check_upgrade3()
    check_upgrade4()
    current_time = pygame.time.get_ticks()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_stop_button_rect.collidepoint(event.pos) and current_frame == 1:
                counting = not counting
            elif upgrades_button_rect.collidepoint(event.pos) and current_frame == 1:
                current_frame = 2
            elif toggle_button_rect.collidepoint(event.pos):
                current_frame = 1
            elif upgrade_button_rect.collidepoint(event.pos) and current_frame == 2:
                purchase_upgrade()
            elif ai_generated_money_button_rect.collidepoint(event.pos) and current_frame == 2:
                purchase_upgrade2()
            mouse_x, mouse_y = event.pos
            if games_button_rect.left <= mouse_x <= games_button_rect.right and \
                    games_button_rect.top <= mouse_y <= games_button_rect.bottom and current_frame == 3:
                handle_games_button_click()  # Add this line
            elif next_page_button_rect_frame2.collidepoint(event.pos) and current_frame == 2:
                current_frame = 3  # Move to Frame 3 (Upgrades Frame 2)
            elif next_page_button_rect_frame3.collidepoint(event.pos) and current_frame == 3:
                current_frame = 4  # Move to Frame 4 (Upgrades Frame 3)
            elif prev_page_button_rect_frame3.collidepoint(event.pos) and current_frame == 3:
                current_frame = 2  # Move to Frame 3 (Upgrades Frame 2)
            elif home_games_button_rect.collidepoint(event.pos) and current_frame == 1:
                current_frame = 5
            if start_stop_button_rect.collidepoint(event.pos) and current_frame == 5:
                games_counting = not games_counting
            elif upgrades_button_rect.collidepoint(event.pos) and current_frame == 5:
                current_frame = 6

    # Update logic
    if counting:
        money += (2 / 60)
        if fraud_purchased:
            money += (2 / 60)
            money_gain = (4 / 60)
        if ai_generated_money_purchased:
            money += (36 / 60)  # Boost money gain by x10 with the AI Generated Money upgrade
            money_gain = (40 / 60)

    if games_counting:
        if games_unlocked:
            games += 1
            games_gain = 1

    # Draw on the screen
    screen.fill((45, 45, 45))

    # Save money and upgrade data every second
    current_button_color = Color(0, 175, 0)  # Initial color
    target_color = Color(*rainbow_colors[current_color_index])
    current_button_color = current_button_color.lerp(target_color, 0.1)  # Adjust the interpolation factor if needed
    start_stop_button_color = current_button_color

    if current_time > save_timer:
        save_game()
        save_timer = current_time + 1000  # Update the timer for the next second
    
    elapsed_time = current_time - transition_start_time

    # Check if the transition is complete
    if elapsed_time >= transition_duration:
        # Reset the start time and swap colors for the next transition
        transition_start_time = current_time
        current_color_index = (current_color_index + 1) % len(rainbow_colors)
        current_button_color = pygame.Color(*rainbow_colors[current_color_index])
        target_color = pygame.Color(*rainbow_colors[(current_color_index + 1) % len(rainbow_colors)])

    else:
        # Interpolate between the current color and the target color
        alpha = elapsed_time / transition_duration
        start_stop_button_color = (
            int(current_button_color.r + alpha * (target_color.r - current_button_color.r)),
            int(current_button_color.g + alpha * (target_color.g - current_button_color.g)),
            int(current_button_color.b + alpha * (target_color.b - current_button_color.b))
        )

    # Draw the current frame
    if current_frame == 1:
        pygame.draw.rect(screen, (70, 70, 70), earning_frame_rect)
        screen.blit(earning_frame_text_surface, (width // 2 - earning_frame_text_surface.get_width() // 2, 40))
        pygame.draw.rect(screen, (0, 175, 0), start_stop_button_rect)
        start_stop_button_text = spartan_font.render("Stop/Start", True, (255, 255, 255))
        text_x = start_stop_button_rect.centerx - start_stop_button_text.get_width() // 2
        text_y = start_stop_button_rect.centery - start_stop_button_text.get_height() // 2
        screen.blit(start_stop_button_text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 0, 175), upgrades_button_rect)
        upgrades_button_text = spartan_font.render("Upgrades", True, (255, 255, 255))
        text_x = upgrades_button_rect.centerx - upgrades_button_text.get_width() // 2
        text_y = upgrades_button_rect.centery - upgrades_button_text.get_height() // 2
        screen.blit(upgrades_button_text, (text_x, text_y))
        money_str = simplify(money)
        money_surface = spartan_font.render(f"Money: ${money_str}", True, (255, 255, 255))
        pygame.draw.rect(screen, (70, 70, 70), money_rect)
        screen.blit(money_surface, (width // 2 - money_surface.get_width() // 2, height - 60))
        if games_unlocked:
            pygame.draw.rect(screen, (175, 0, 0), home_games_button_rect)
            home_games_button_text_color = (255, 255, 255)
            home_games_button_text = spartan_font.render("Games", True, home_games_button_text_color)
            text_x = home_games_button_rect.centerx - home_games_button_text.get_width() // 2
            text_y = home_games_button_rect.centery - home_games_button_text.get_height() // 2
            screen.blit(home_games_button_text, (text_x, text_y))
    elif current_frame == 2:
        pygame.draw.rect(screen, (70, 70, 70), upgrades_frame_rect)
        screen.blit(upgrades_frame_text_surface, (width // 2 - upgrades_frame_text_surface.get_width() // 2, 75))
        pygame.draw.rect(screen, (0, 175, 0), toggle_button_rect)
        toggle_button_text = spartan_font.render("Back to Earning", True, (255, 255, 255))
        text_x = toggle_button_rect.centerx - toggle_button_text.get_width() // 2
        text_y = toggle_button_rect.centery - toggle_button_text.get_height() // 2
        screen.blit(toggle_button_text, (text_x, text_y))
        pygame.draw.rect(screen, (175, 0, 0), upgrade_button_rect)
        upgrade_button_text_color = (255, 255, 255) if not fraud_purchased else (70, 70, 70)
        upgrade_button_content = "($25) Buy Upgrade" if not fraud_purchased else "Already Bought!"
        upgrade_button_text = spartan_font.render(f"{upgrade_button_content}", True, upgrade_button_text_color)
        text_x = upgrade_button_rect.centerx - upgrade_button_text.get_width() // 2
        text_y = upgrade_button_rect.centery - upgrade_button_text.get_height() // 2
        screen.blit(upgrade_button_text, (text_x, text_y))

        pygame.draw.rect(screen, (10, 10, 10), next_page_button_rect_frame2)
        next_page_button_text_frame2 = spartan_font.render("Next Page", True, (255, 255, 255))
        text_x = next_page_button_rect_frame2.centerx - next_page_button_text_frame2.get_width() // 2
        text_y = next_page_button_rect_frame2.centery - next_page_button_text_frame2.get_height() // 2
        screen.blit(next_page_button_text_frame2, (text_x, text_y))

        text_x = upgrade_button_rect.centerx - upgrade_name_surface.get_width() // 2
        text_y = upgrade_button_rect.centery - upgrade_name_surface.get_height() - 35 
        screen.blit(upgrade_name_surface, (text_x, text_y))
        text_x = upgrade_button_rect.centerx - upgrade_description_surface.get_width() // 2
        text_y = upgrade_button_rect.centery - upgrade_name_surface.get_height() - 12
        screen.blit(upgrade_description_surface, (text_x, text_y))

        money_gain_frame_text = f"Money/tick: ${simplify(round(money_gain, 2))}"
        money_gain_second_text = f"Money/s: ${simplify(round(money_gain * 60))}"

        money_str = simplify(money)
        money_surface = spartan_font_medium.render(f"{money_gain_frame_text} || {money_gain_second_text}", True, (255, 255, 255))
        pygame.draw.rect(screen, (70, 70, 70), money_rect)
        screen.blit(money_surface, (width // 2 - money_surface.get_width() // 2, height - 57))

        ai_generated_money_button_rect = pygame.Rect(285, height - 125, 225, 40)
        pygame.draw.rect(screen, (175, 0, 175), ai_generated_money_button_rect)
        ai_generated_money_button_text_color = (255, 255, 255) if not ai_generated_money_purchased else (70, 70, 70)
        ai_generated_money_button_content = f"(${upgrade2_cost}) Buy Upgrade" if not ai_generated_money_purchased else "Already Bought!"
        ai_generated_money_button_text = spartan_font.render(f"{ai_generated_money_button_content}", True, ai_generated_money_button_text_color)
        text_x = ai_generated_money_button_rect.centerx - ai_generated_money_button_text.get_width() // 2
        text_y = ai_generated_money_button_rect.centery - ai_generated_money_button_text.get_height() // 2
        screen.blit(ai_generated_money_button_text, (text_x, text_y))

        text_x = ai_generated_money_button_rect.centerx - upgrade2_name_surface.get_width() // 2
        text_y = ai_generated_money_button_rect.centery - upgrade2_name_surface.get_height() - 35
        screen.blit(upgrade2_name_surface, (text_x, text_y))
        text_x = ai_generated_money_button_rect.centerx - upgrade2_description_surface.get_width() // 2
        text_y = ai_generated_money_button_rect.centery - upgrade2_name_surface.get_height() - 12
        screen.blit(upgrade2_description_surface, (text_x, text_y))
    elif current_frame == 3:
        pygame.draw.rect(screen, (70, 70, 70), upgrades_frame_rect)
        screen.blit(upgrades_frame_text_surface, (width // 2 - upgrades_frame_text_surface.get_width() // 2, 75))
        pygame.draw.rect(screen, (0, 175, 0), toggle_button_rect)
        toggle_button_text = spartan_font.render("Back to Earning", True, (255, 255, 255))
        text_x = toggle_button_rect.centerx - toggle_button_text.get_width() // 2
        text_y = toggle_button_rect.centery - toggle_button_text.get_height() // 2
        screen.blit(toggle_button_text, (text_x, text_y))

        pygame.draw.rect(screen, (10, 10, 10), next_page_button_rect_frame3)
        next_page_button_text_frame3 = spartan_font.render("Next Page", True, (255, 255, 255))
        text_x = next_page_button_rect_frame3.centerx - next_page_button_text_frame3.get_width() // 2
        text_y = next_page_button_rect_frame3.centery - next_page_button_text_frame3.get_height() // 2
        screen.blit(next_page_button_text_frame3, (text_x, text_y))

        pygame.draw.rect(screen, (10, 10, 10), prev_page_button_rect_frame3)
        prev_page_button_text_frame3 = spartan_font.render("Prev Page", True, (255, 255, 255))
        text_x = prev_page_button_rect_frame3.centerx - prev_page_button_text_frame3.get_width() // 2
        text_y = prev_page_button_rect_frame3.centery - prev_page_button_text_frame3.get_height() // 2
        screen.blit(prev_page_button_text_frame3, (text_x, text_y))

        # Money Display
        games_content = '[SPOILER]s'
        if isunlocked():
            games_content = "games"
        

        games_value_frame_text = f"You have {simplify(games)} {games_content}."

        money_str = simplify(money)
        money_surface = spartan_font_medium.render(f"{games_value_frame_text}", True, (255, 255, 255))
        pygame.draw.rect(screen, (70, 70, 70), money_rect)
        screen.blit(money_surface, (width // 2 - money_surface.get_width() // 2, height - 57))

        # Upgrade 3
        pygame.draw.rect(screen, (30, 144, 255), games_button_rect)
        games_button_text_color = (255, 255, 255) if not games_unlocked else (70, 70, 70)
        games_button_content = f"(${simplify(upgrade3_cost)}) Buy Upgrade" if not games_unlocked else "Already Bought!"
        games_button_text = spartan_font.render(f"{games_button_content}", True, games_button_text_color)
        text_x = games_button_rect.centerx - games_button_text.get_width() // 2
        text_y = games_button_rect.centery - games_button_text.get_height() // 2
        screen.blit(games_button_text, (text_x, text_y))

        text_x = games_button_rect.centerx - upgrade3_name_surface.get_width() // 2
        text_y = games_button_rect.centery - upgrade3_name_surface.get_height() - 35
        screen.blit(upgrade3_name_surface, (text_x, text_y))
        text_x = games_button_rect.centerx - upgrade3_description_surface.get_width() // 2
        text_y = games_button_rect.centery - upgrade3_name_surface.get_height() - 12
        screen.blit(upgrade3_description_surface, (text_x, text_y))
    elif current_frame == 4:
        ... # Leave this alone for now
    elif current_frame == 5:
        pygame.draw.rect(screen, (70, 70, 70), games_frame_rect)
        pygame.draw.rect(screen, (0, 175, 0), toggle_button_rect)
        toggle_button_text = spartan_font.render("Back to Earning", True, (255, 255, 255))
        text_x = toggle_button_rect.centerx - toggle_button_text.get_width() // 2
        text_y = toggle_button_rect.centery - toggle_button_text.get_height() // 2
        screen.blit(toggle_button_text, (text_x, text_y))

        pygame.draw.rect(screen, start_stop_button_color, start_stop_button_rect)
        
        start_stop_button_text = spartan_font.render("Stop/Start", True, (255, 255, 255))
        text_x = start_stop_button_rect.centerx - start_stop_button_text.get_width() // 2
        text_y = start_stop_button_rect.centery - start_stop_button_text.get_height() // 2
        screen.blit(start_stop_button_text, (text_x, text_y))

        pygame.draw.rect(screen, (0, 0, 175), upgrades_button_rect)
        upgrades_button_text = spartan_font.render("Games Upgrades", True, (255, 255, 255))
        text_x = upgrades_button_rect.centerx - upgrades_button_text.get_width() // 2
        text_y = upgrades_button_rect.centery - upgrades_button_text.get_height() // 2
        screen.blit(upgrades_button_text, (text_x, text_y))

        money_str = simplify(money)
        games_str = simplify(games)
        money_surface = spartan_font.render(f"Money: ${money_str} || Games: {games_str}", True, (255, 255, 255))
        pygame.draw.rect(screen, (70, 70, 70), money_rect)
        screen.blit(money_surface, (width // 2 - money_surface.get_width() // 2, height - 60))
    # Update the display
    pygame.display.flip()

    # Control the frame rate (optional)
    pygame.time.Clock().tick(60)
