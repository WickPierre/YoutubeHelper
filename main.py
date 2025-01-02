import asyncio
from multiprocessing.pool import ThreadPool
from new_nodpi import main
from download_video_2 import download
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


def run2():
    asyncio.run(main(host='127.0.0.1', port=8881))


class MainApp(App):
    def on_start(self):
        pool = ThreadPool(processes=1)
        async_start = pool.apply_async(run2)

    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        self.text_input = TextInput(multiline=False, font_size="55sp")
        self.button = Button(
            text="Install", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        self.button.bind(on_press=self.run_process)

        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)

        return self.layout

    def run_process(self, instance):
        url = self.text_input.text
        download(url)


if __name__ == "__main__":
    app = MainApp()
    app.run()