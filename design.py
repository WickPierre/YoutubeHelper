import asyncio
from multiprocessing.pool import ThreadPool
from new_nodpi import main
from download_video_2 import download
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar


def run2():
    asyncio.run(main(host='127.0.0.1', port=8881))


class MainApp(App):
    def on_start(self):
        pool = ThreadPool(processes=1)
        async_start = pool.apply_async(run2)

    def build(self):
        self.main_layout = BoxLayout(orientation="horizontal", padding=10, spacing=10)
        # padding - отступ, spacing - размер пробела

        self.left_layout = BoxLayout(
            orientation="vertical", size_hint=(0.3, 1), spacing=5
        )  # size_hint - размер в процентах, 1 весь экран, 0.3 30% экрана
        self.selected_button = None

        for i in range(1, 6):
            btn = ToggleButton(
                text=f"Качество {i}", size_hint=(1, None), height=50, group="selection"
            )
            btn.bind(on_press=self.on_selection)
            self.left_layout.add_widget(btn)

        self.right_layout = BoxLayout(
            orientation="vertical", size_hint=(0.7, 1), spacing=10
        )

        self.text_input = TextInput(hint_text="Введите ссылку", multiline=False)
        self.right_layout.add_widget(self.text_input)

        # Прогресс-бар
        self.progress_bar = ProgressBar(max=100, value=25, size_hint=(1, 0.1))
        self.right_layout.add_widget(self.progress_bar)

        action_button = Button(
            text="Скачать видео",
            size_hint=(1, 0.2),
            background_color=(0.3, 0.6, 0.9, 1),
        )
        action_button.bind(on_press=self.on_action)
        self.right_layout.add_widget(action_button)

        self.main_layout.add_widget(self.left_layout)
        self.main_layout.add_widget(self.right_layout)

        return self.main_layout

    def on_action(self, instance):  # instance передает инфу по элементу, в 51 инфу о тексте
        print("---> connect here code to download video <---")
        self.start_progress()
        url = self.text_input.text
        download(url)

    def on_selection(self, instance):
        print(instance.text)

    def start_progress(self):
        # Здесь реализовать заполнение прогресс бара, не уверен, что в фнции это удобно
        pass


if __name__ == "__main__":
    app = MainApp()
    app.run()