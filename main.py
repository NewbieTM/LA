from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from bs4 import BeautifulSoup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
import requests

Builder.load_string('''

# Define the scroll view
<ScrollableLabel>:
    Label:
        canvas.before:
            Color:
                rgba: (.93, .91, .67, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        id: label
        color: (0,0,0,1)
        font_size: 20
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
<MyGridLayout>:
    spacing: 30
    size_hint_y: None
    size: self.width, 50
    padding: (10,0,10,10)
<NextButton>:
    text: 'Следующая стр...'
    font_size: self.width / 9
    size_hint: 0.5,1
    background_color: (.93, .91, .67, 1)
    background_normal: ''
    color: (0,0,0,1)
    
<PreviousButton>:
    text: 'Предыдущая стр...'
    font_size: self.width / 9
    size_hint: 0.5,1
    background_color: (.93, .91, .67, 1)
    background_normal: ''
    color: (0,0,0,1)
<MyLabel>:
    size_hint: 0.01,0.01
    
''')

x = 1

class MyGridLayout(GridLayout):
    pass
class NextButton(Button):
    pass
class PreviousButton(Button):
    pass
class MyLabel(Label):
    pass
class MyButton(Button):
    color = (0, 0, 0, 1)
    valign = 'bottom'
    padding_y = 10
    background_color = (.93, .91, .67, 1)
    background_normal = ''
    font_size = 13

class ScrollableLabel(ScrollView):
    pass




class Box(BoxLayout):
    color = (.98, .98, .82, 1)
    orientation = "vertical"
    spacing = 10

    def on_kv_post(self, widget):
        self.add_widget(MyButton(text='4 класс', on_press=self.btn_menu))
        self.add_widget(MyButton(text='5 класс', on_press=self.btn_menu))
        self.add_widget(MyButton(text='6 класс', on_press=self.btn_menu))
        self.add_widget(MyButton(text='7 класс', on_press=self.btn_menu))
        self.add_widget(MyButton(text='8 класс', on_press=self.btn_menu))
        self.add_widget(MyButton(text='9 класс', on_press=self.btn_menu))
        self.add_widget(MyButton(text='10 класс', on_press=self.btn_menu))
        self.add_widget(MyButton(text='11 класс', on_press=self.btn_menu))


    def btn_menu(self,widget):
        self.clear_widgets()
        self.add_widget(MyButton(text='И. С. Тургенев. Отцы и дети', on_press=self.btn_press))
        self.add_widget(MyButton(text='И. А. Гончаров. Обломов.', on_press=self.btn_press))
        self.add_widget(MyButton(text='Ф. М. Достоевский. Преступление и наказание.', on_press=self.btn_press))
        self.add_widget(MyButton(text='Л. Н. Толстой. Война и мир.', on_press=self.btn_press))
        self.add_widget(MyButton(text='Н. С. Лесков. Очарованный странник. ', on_press=self.btn_press))
        self.add_widget(MyButton(text='Н. А. Некрасов. Лирика. Кому на Руси жить хорошо...', on_press=self.btn_press))
        self.add_widget(MyButton(text='А. И. Островский. Гроза.', on_press=self.btn_press))
        self.add_widget(MyButton(text='А. П. Чехов. Вишневый сад.', on_press=self.btn_press))


    def btn_press(self, instance):
        self.clear_widgets()
        sc = ScrollableLabel()
        global x
        data = ''
        url = "http://loveread.ec/read_book.php?id=12021&p=1"
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        teme = soup.find_all("p", class_="MsoNormal")
        for temes in teme:
            data += temes.text
        sc.ids.label.text = data

        self.add_widget(sc)
        gd = MyGridLayout(cols = 3)
        gd.add_widget(PreviousButton(on_press=self.previous_page))
        gd.add_widget(MyLabel(text = f'стр № {x}',color = (1,1,1,1)))
        gd.add_widget(NextButton(on_press=self.next_page))

        self.add_widget(gd)

    def next_page(self,instance):
        self.clear_widgets()
        sc = ScrollableLabel()
        data = ''
        global x
        x += 1
        url = "http://loveread.ec/read_book.php?id=12021&p=" + f'{x}'
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        teme = soup.find_all("p", class_="MsoNormal")
        for temes in teme:
            data += temes.text
        sc.ids.label.text = data
        self.add_widget(sc)
        gd = MyGridLayout(cols=3)
        gd.add_widget(PreviousButton(on_press=self.previous_page))
        gd.add_widget(MyLabel(text=f'стр № {x}'))
        gd.add_widget(NextButton(on_press=self.next_page))

        self.add_widget(gd)

    def previous_page(self,instance):
        self.clear_widgets()
        sc = ScrollableLabel()
        data = ''
        global x
        if x != 1:
            x -= 1
        url = "http://loveread.ec/read_book.php?id=12021&p=" + f'{x}'
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        teme = soup.find_all("p", class_="MsoNormal")
        for temes in teme:
            data += temes.text
        sc.ids.label.text = data
        self.add_widget(sc)
        gd = MyGridLayout(cols=3)
        gd.add_widget(PreviousButton(on_press=self.previous_page))
        gd.add_widget(MyLabel(text=f'стр № {x}'))
        gd.add_widget(NextButton(on_press=self.next_page))

        self.add_widget(gd)


class MyApp(App):

    def build(self):
        return Box()


if __name__ == "__main__":
    MyApp().run()


