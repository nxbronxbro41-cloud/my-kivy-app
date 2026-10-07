from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # वर्टिकल लेआउट
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 1. लेबल
        self.label = Label(text="अपना नाम लिखें:")
        layout.add_widget(self.label)
        
        # 2. टेक्स्ट इनपुट (टेक्स्ट बॉक्स)
        self.input_text = TextInput(multiline=False)
        layout.add_widget(self.input_text)
        
        # 3. बटन
        btn = Button(text="Submit")
        btn.bind(on_press=self.on_click)
        layout.add_widget(btn)
        
        return layout

    # बटन क्लिक होने पर चलने वाला फ़ंक्शन
    def on_click(self, instance):
        user_name = self.input_text.text
        self.label.text = f"नमस्ते {user_name}! ऐप में स्वागत है।"

if __name__ == "__main__":
    MyApp().run()

