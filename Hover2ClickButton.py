import time
import threading
import tkinter as tk

def blinkdecorator(func):
    '''
    Decorator to make the button blink after the functioning.
    :param func: function to apply decorator.
    :return: None
    '''
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.blink()

        return

    return wrapper

class Hover2ClickButton(tk.Button):
    '''
    This class successes tk.Button and make it clickable with mouse hovering.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(command = self.click_function)

        self.stay_time = 0.75 # Default staying time. You can change this time with self.set_stay_time() function.
        self.blink_time = 0.05 # Blinking time when the button is clicked.

        # Flags
        self.click_flag = False
        self.exit_flag = True

        self.running_thread = False

        return

    def bind_event(self):
        '''
        Bind <Enter>, <Leave> events.
        :return: None
        '''

        self.bind('<Enter>', self.cursor_enter)
        self.bind('<Leave>', self.cursor_leave)

        return

    def set_stay_time(self, stay_time):
        '''
        Change the hoverting time to click.
        :param stay_time: When you hover your cursor for this time, the button would be clicked.
        :return: None
        '''
        self.stay_time = stay_time

        return

    @blinkdecorator
    def click_function(self):
        '''
        This function is called automatically when the cursor is hovering on the button for "self.stay_time".
        :return: None
        '''

        return

    def blink(self):
        '''
        This function helps you recognize the button click visually.
        :return: None
        '''

        def _blink():
            bg_color = self['bg']
            font_color = self['fg']

            self.config(bg = font_color, fg = bg_color)

            time.sleep(self.blink_time)

            self.config(bg = bg_color, fg = font_color)

        blink_thread = threading.Thread(target = _blink)
        blink_thread.start()

        return

    def delayed_click(self):
        '''
        Call self.click_function if the mouse is still on the button even after "self.stay_time".
        :return: None
        '''
        time.sleep(self.stay_time)

        if self.click_flag:
            self.click_function()

        self.running_thread = False

        if self.exit_flag == False:
            self.cursor_enter(None)

        return

    def cursor_enter(self, e):
        '''
        This function is called when the mouse enter the button.
        :return: None
        '''

        # print(f'Cursor Entered!')

        self.exit_flag = False

        if self.running_thread:
            return

        self.running_thread = True

        self.click_thread = threading.Thread(target = self.delayed_click)
        self.click_thread.start()

        self.click_flag = True

        return

    def cursor_leave(self, e):
        '''
        This function is called when the mouse leave button.
        :return: None
        '''

        # print(f'Cursor Left!')

        self.click_flag = False
        self.exit_flag = True

        return