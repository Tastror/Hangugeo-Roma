import wx
import hankukeo


class HankukeoFrame(wx.Frame):

    placeholder = None
    separate = False

    def __init__(self, *args, **kw):

        # ensure the parent's __init__ is called
        super(HankukeoFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # create box
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.type_in_textbox = wx.TextCtrl(pnl, style=wx.TE_MULTILINE)
        self.type_in_textbox.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, "Malgun Gothic"))
        self.hbox.Add(self.type_in_textbox, 1, wx.EXPAND)
        self.show_textbox = wx.TextCtrl(pnl, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.show_textbox.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, "Segoe UI"))
        self.hbox.Add(self.show_textbox, 1, wx.EXPAND)

        # set box
        pnl.SetSizer(self.hbox)

        # bind type-in box
        self.type_in_textbox.Bind(wx.EVT_KEY_UP, self.update)

        # create a menu bar
        self.menu_bar_init()

        # create a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to use Hankukeo-UI!")

    # Bars
    def menu_bar_init(self):

        # file menu
        file_menu = wx.Menu()
        usage_item = file_menu.Append(-1, "&Usage...\tCtrl-U", "Usage about this UI")
        self.separate_item = file_menu.Append(-1, "&Separate...\tCtrl-P", "Separate the letter with prime(')", wx.ITEM_CHECK)
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT)

        # help menu
        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menu_bar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.on_usage, usage_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)
        self.Bind(wx.EVT_MENU, self.on_separate, self.separate_item)

    def on_exit(self, event):
        self.Close(True)

    def on_usage(self, event):
        self.placeholder = None
        wx.MessageBox(
            "Type Hankeur (Hangul, Hangeul) in the left, and the Roman-Form will be show in the right.",
            "Usage"
        )

    def on_separate(self, event):
        if self.separate_item.IsChecked():
            self.separate = True
            self.update(None)
        else:
            self.separate = False
            self.update(None)

    def on_about(self, event):
        self.placeholder = None
        wx.MessageBox("Welcome to use Hankukeo-UI", "About Hankukeo-UI", wx.OK | wx.ICON_INFORMATION)

    def update(self, event):
        self.show_textbox.SetValue(hankukeo.roma(self.type_in_textbox.GetValue(), self.separate)["res_str"])


if __name__ == '__main__':
    app = wx.App()
    frm = HankukeoFrame(None, title='Hankukeo-UI')
    frm.Show()
    app.MainLoop()
