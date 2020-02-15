from tkinter import ttk, IntVar, StringVar, Checkbutton, Frame, Label, OptionMenu, E, W, LEFT, RIGHT
import gui.widgets as widgets

def entrando_page(parent):
    # Entrance Randomizer
    self = ttk.Frame(parent)

    # Entrance Randomizer options
    self.widgets = {}

    ## Pyramid pre-opened
    key = "openpyramid"
    self.widgets[key] = widgets.make_widget(
      self,
      "checkbox",
      self,
      "Pre-open Pyramid Hole",
      None
    )
    self.widgets[key].pack(anchor=W)

    ## Shuffle Ganon
    key = "shuffleganon"
    self.widgets[key] = widgets.make_widget(
      self,
      "checkbox",
      self,
      "Include Ganon's Tower and Pyramid Hole in shuffle pool",
      None
    )
    self.widgets[key].pack(anchor=W)

    ## Entrance Shuffle
    key = "entranceshuffle"
    self.widgets[key] = widgets.make_widget(
      self,
      "selectbox",
      self,
      "Entrance Shuffle",
      None,
      {"label": {"side": LEFT}, "selectbox": {"side": RIGHT}},
      {
        "Vanilla": "vanilla",
        "Simple": "simple",
        "Restricted": "restricted",
        "Full": "full",
        "Crossed": "crossed",
        "Insanity": "insanity",
        "Restricted (Legacy)": "restricted_legacy",
        "Full (Legacy)": "full_legacy",
        "Madness (Legacy)": "madness_legacy",
        "Insanity (Legacy)": "insanity_legacy",
        "Dungeons + Full": "dungeonsfull",
        "Dungeons + Simple": "dungeonssimple"
      }
    )
    self.widgets[key].pack(anchor=W)

    return self