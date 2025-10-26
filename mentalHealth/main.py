from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from screens.home_screen import HomeScreen
from screens.edit_patient_screen import EditPatientScreen
from screens.add_patient_screen import AddPatientScreen
from screens.view_data_screen import ViewDataScreen
from kivy.graphics import Color, Rectangle

from controllers.patient_controller import PatientController



class HomeScreen(BoxLayout):
    """Tampilan awal dengan tombol navigasi."""
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        # Judul
        self.add_widget(Label(text='Selamat Datang di Konsultasiku', font_size=24, bold=True))

        # Tombol navigasi
        add_button = Button(text='Tambah Data', size_hint=(1, 0.2))
        add_button.bind(on_press=lambda instance: self.change_screen(screen_manager, 'add_patient'))
        self.add_widget(add_button)

        view_button = Button(text='Lihat Seluruh Data', size_hint=(1, 0.2))
        view_button.bind(on_press=lambda instance: self.change_screen(screen_manager, 'view_data'))
        self.add_widget(view_button)

        edit_button = Button(text='Edit Data Pasien', size_hint=(1, 0.2))
        edit_button.bind(on_press=lambda instance: self.change_screen(screen_manager, 'edit_patient'))
        self.add_widget(edit_button)

        delete_button = Button(text='Hapus Data Pasien', size_hint=(1, 0.2))
        delete_button.bind(on_press=self.delete_patient_popup)  
        self.add_widget(delete_button)

        export_button = Button(text='Export ke Excel', size_hint=(1, 0.2))
        export_button.bind(on_press=self.export_to_excel)
        self.add_widget(export_button)

    def change_screen(self, screen_manager, screen_name):
        """Mengganti screen berdasarkan nama screen."""
        screen_manager.current = screen_name

    def export_to_excel(self, instance):
        """Export patient data ke file Excel."""
        try:
            data = []  # Ganti dengan data asli
            import pandas as pd
            df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Gender", "Diagnosis", "Consultation Date"])
            df.to_excel("export/exported_data.xlsx", index=False)
            print("Data berhasil diexport ke Excel.")
        except Exception as e:
            print(f"Error exporting data: {e}")
    
    

    def delete_patient_popup(self, instance):
        """Menampilkan popup untuk konfirmasi hapus data pasien berdasarkan ID."""
        # Layout untuk popup
        popup_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        popup_layout.add_widget(Label(text='Masukkan ID Pasien yang akan dihapus'))
        id_input = TextInput(hint_text='ID Pasien', input_filter='int', multiline=False)
        popup_layout.add_widget(id_input)

        # Tombol Hapus
        button_layout = BoxLayout(spacing=10)
        delete_button = Button(text='Hapus', size_hint=(1, 0.8))
        delete_button.bind(on_press=lambda instance: self.delete_patient(id_input.text))  # Mengikat pemanggilan delete_patient
        button_layout.add_widget(delete_button)

        # Tombol Batal
        cancel_button = Button(text='Batal', size_hint=(1, 0.8))
        cancel_button.bind(on_press=lambda instance: self.close_popup(instance))
        button_layout.add_widget(cancel_button)

        popup_layout.add_widget(button_layout)

        # Popup
        self.popup = Popup(title='Hapus Data Pasien', content=popup_layout, size_hint=(0.8, 0.4))
        self.popup.open()

    def delete_patient(self, patient_id):
        """Memanggil fungsi controller untuk menghapus data pasien berdasarkan ID."""
        if patient_id:
            try:
                patient_id = int(patient_id)  # Mengkonversi id menjadi integer
                from controllers.patient_controller import PatientController
                PatientController.delete_patient(patient_id)  # Memanggil fungsi dari controller untuk menghapus
                print(f"Data pasien dengan ID {patient_id} berhasil dihapus.")
                self.close_popup(None)  # Menutup popup setelah sukses
            except ValueError:
                print("ID harus berupa angka!")
            except Exception as e:
                print(f"Terjadi kesalahan saat menghapus data pasien: {e}")
        else:
            print("Harap masukkan ID pasien.")

    def close_popup(self, instance):
        """Menutup popup setelah penghapusan selesai atau dibatalkan."""
        if self.popup:
            self.popup.dismiss()
            
class ViewDataScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # GridLayout dengan 6 kolom, padding, dan spacing
        layout = GridLayout(cols=6, size_hint_y=None, padding=[10, 10], spacing=[10, 5])
        layout.bind(minimum_height=layout.setter('height'))

        # Header tabel
        headers = ['ID', 'Nama', 'Gender', 'Diagnosis', 'Tanggal Konsultasi', 'Usia']
        for header in headers:
            layout.add_widget(Label(
                text=header,
                bold=True,
                size_hint_y=None,
                height=40,
                size_hint_x=0.16  # Lebar setiap kolom sama rata (1/6 = 0.16)
            ))

        # Mengambil data pasien dari database
        patients = PatientController.get_all_patients()
        if not patients:
            layout.add_widget(Label(
                text="Tidak ada data pasien.",
                size_hint_y=None,
                height=30,
                size_hint_x=1,
                col_span=6  # Membuat label ini memenuhi seluruh baris
            ))
        else:
            for patient in patients:
                for field in patient:
                    layout.add_widget(Label(
                        text=str(field),
                        size_hint_y=None,
                        height=30,
                        size_hint_x=0.16
                    ))

        # ScrollView untuk membuat tampilan bisa di-scroll
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)
        
class MentalHealthApp(App):
    def build(self):
        screen_manager = ScreenManager()

        # Membungkus HomeScreen dalam Screen
        home_screen = Screen(name='home')
        home_screen.add_widget(HomeScreen(screen_manager))
        screen_manager.add_widget(home_screen)

        # Menambahkan layar lainnya
        screen_manager.add_widget(AddPatientScreen(name='add_patient'))
        screen_manager.add_widget(ViewDataScreen(name='view_data'))
        screen_manager.add_widget(EditPatientScreen(name='edit_patient'))

        return screen_manager

if __name__ == '__main__':
    MentalHealthApp().run()
