"""This is a minigame that lets a player try to catch the moving light by
touching the nearest button(s). After a set time, a winning or losing tone
would play depending on how well the player did.

NOTE: This took up just enough memory on the chip. Any more addition
will cause MemoryError.

"""
import random
import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.3
LIGHT_LIST = list(range(10))
MUSIC_FACTOR = 0.25  # Chip dependent music interval factor

# Maps A sensors to LEDs for scoring.
A_TO_LED_MAP = {1: [5, 6, 7], 2: [7, 8], 3: [8, 9], 4: [0, 1],
                5: [1, 2], 6: [2, 3], 7: [3, 4], -1: []}

# Music notes.
NOTE_E3 = 165
NOTE_F3 = 175
NOTE_G3 = 196
NOTE_GS3 = 208
NOTE_A3 = 220
NOTE_AS3 = 233
NOTE_B3 = 247
NOTE_C4 = 262
NOTE_E5 = 659
NOTE_G5 = 784
NOTE_C6 = 1047
NOTE_D6 = 1175
NOTE_E6 = 1319
NOTE_G6 = 1568


# NOTE: Tried not to include chip specific code in here.
class CatchMeGame:
    """Class to handle game logic."""
    def __init__(self):
        self._is_running = False
        self._scores = {}
        self._time_start = 0
        self._subtimer_start = 0
        self._current_player = None
        self._current_objective = None

        self.min_score_to_win = 10
        self.game_duration = 30  # seconds

        # TODO: Adjust by difficulty level? Probably not enough memory.
        self.subtimer_wait = 1  # seconds

    @property
    def current_objective(self):
        """Current objective of the game."""
        return self._current_objective

    @current_objective.setter
    def current_objective(self, val):
        if val in LIGHT_LIST:
            self._current_objective = val

    @property
    def is_running(self):
        """State of the game (bool)."""
        return self._is_running

    @property
    def scores(self):
        """Current game scores (dict)."""
        return self._scores

    @property
    def game_elapsed_time(self):
        """Current game elapsed time in seconds."""
        if self.is_running:
            t = time.time() - self._time_start
        else:
            t = 0
        return t

    @property
    def time_is_up(self):
        """Is the time up for the current player?"""
        return self.game_elapsed_time > self.game_duration

    def start_subtimer(self):
        """Start/re-start the sub-timer for the current game."""
        if self.is_running:
            self._subtimer_start = time.time()

    @property
    def subtimer_elapsed_time(self):
        """Current sub-timer elapsed time in seconds."""
        if self.is_running:
            t = time.time() - self._subtimer_start
        else:
            t = 0
        return t

    @property
    def subtimer_is_up(self):
        """Is the sub-timer up for the current game state?"""
        return self.subtimer_elapsed_time > self.subtimer_wait

    def increase_score(self, player_name):
        """Given player got a point."""
        if player_name in self._scores:
            self._scores[player_name] += 1

    def current_score(self, player_name):
        """Current score for the given player."""
        if player_name in self._scores:
            return self._scores[player_name]

    def player_won(self, player_name):
        """Did the player win?"""
        return self._scores[player_name] >= self.min_score_to_win

    def start_new_game(self, player_name):
        """Starts a new game for the given player."""
        self._scores[player_name] = 0
        self._time_start = time.time()
        self._is_running = True
        self._current_player = player_name

    def stop_game(self):
        """Stop the game for the current player."""
        if self.is_running:
            self._is_running = False
            self._time_start = 0
            self._subtimer_start = 0
            self._current_player = None


def play_score_tones():
    cpx.play_tone(NOTE_G3, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_G6, 0.5 * MUSIC_FACTOR)


def play_missed_tones():
    cpx.play_tone(NOTE_A3, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_G3, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_E3, 0.5 * MUSIC_FACTOR)


def play_win_tones():
    cpx.play_tone(NOTE_E5, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_G5, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_E6, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_C6, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_D6, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_G6, 0.5 * MUSIC_FACTOR)


def play_lost_tones():
    cpx.play_tone(NOTE_C4, 0.25 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_G3, 0.25 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_E3, 0.5 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_A3, 0.375 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_B3, 0.375 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_GS3, 0.375 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_AS3, 0.375 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_GS3, 0.375 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_G3, 0.25 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_F3, 0.25 * MUSIC_FACTOR)
    cpx.play_tone(NOTE_G3, 0.5 * MUSIC_FACTOR)


def light_one_up(led_index, led_color=(0, 50, 0)):
    """Light up the given LED. Default is greenish."""
    cpx.pixels.fill((0, 0, 0))  # Reset all
    if led_index in LIGHT_LIST:
        cpx.pixels[led_index] = led_color
    cpx.pixels.show()


def blink_lights(n_blinks, n_pixels, color):
    for _ in range(n_blinks):
        for i in range(n_pixels):
            cpx.pixels[i] = color
        cpx.pixels.show()
        time.sleep(0.05)
        cpx.pixels.fill((0, 0, 0))
        cpx.pixels.show()


catchme = CatchMeGame()

# TODO: Implement multi-player? Probably not enough memory.
player_name = 'player_01'

# Main loop controlling overall chip behavior
while True:
    time.sleep(0.05)  # To prevent overheating?

    # Press A to turn it on (and start a game)
    if cpx.button_a:
        print('Start game... Ready, {}!'.format(player_name))
        cpx.play_tone(NOTE_C4, 1.0 * MUSIC_FACTOR)
        cpx.red_led = True
        catchme.start_new_game(player_name)
        catchme.current_objective = random.choice(LIGHT_LIST)
        light_one_up(catchme.current_objective)
        catchme.start_subtimer()

    # Press B to turn it off (same as giving up)
    if cpx.button_b:
        print('Stop game')
        cpx.play_tone(NOTE_C6, 1.0 * MUSIC_FACTOR)
        light_one_up(-1)
        cpx.red_led = False
        catchme.stop_game()

    # When game is started, light jumps around randomly
    if catchme.is_running:
        if catchme.time_is_up:
            if catchme.player_won(player_name):
                print('You win!')
                play_win_tones()
                blink_lights(3, 10, (0, 50, 0))
            else:
                print('You lost!')
                play_lost_tones()
                blink_lights(3, catchme.current_score(player_name), (50, 0, 0))
            catchme.stop_game()
            cpx.red_led = False
            light_one_up(-1)
        else:
            # See if sensor is touched.
            if cpx.touch_A1:
                i_sensor = 1
            elif cpx.touch_A2:
                i_sensor = 2
            elif cpx.touch_A3:
                i_sensor = 3
            elif cpx.touch_A4:
                i_sensor = 4
            elif cpx.touch_A5:
                i_sensor = 5
            elif cpx.touch_A6:
                i_sensor = 6
            elif cpx.touch_A7:
                i_sensor = 7
            else:
                i_sensor = -1

            # Increase score if correct sensor is touched.
            objective_met = False
            if catchme.current_objective in A_TO_LED_MAP[i_sensor]:
                objective_met = True
                catchme.increase_score(player_name)
                print('You score! {}/{}'.format(
                    catchme.current_score(player_name),
                    catchme.min_score_to_win))
                play_score_tones()
            elif i_sensor != -1:
                print('You missed! {}/{}'.format(
                    catchme.current_score(player_name),
                    catchme.min_score_to_win))
                play_missed_tones()

            # If sub-timer is up, change the light.
            if catchme.subtimer_is_up or objective_met:
                print('Changing it up...')
                cpx.play_tone(NOTE_C4, 0.5 * MUSIC_FACTOR)
                catchme.current_objective = random.choice(LIGHT_LIST)
                light_one_up(catchme.current_objective)
                catchme.start_subtimer()
