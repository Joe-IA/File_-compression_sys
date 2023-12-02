from pydub import AudioSegment
import base64
class AudioProcessor:
    @staticmethod
    def audio_to_binary(audio_file):
        audio = AudioSegment.from_file(audio_file, format="wav")
        audio = audio.set_frame_rate(44100).set_channels(1)
        return audio.raw_data

    @staticmethod
    def binary_to_text(binary_data):
        return base64.b64encode(binary_data).decode()

    @staticmethod
    def text_to_binary(text):
        return base64.b64decode(text)

    @staticmethod
    def binary_to_audio(binary_data, output_audio_file):
        sample_width = 2
        channels = 1
        frame_rate = 44100
        datalen = len(binary_data)
        expected_len = (datalen // (sample_width)) *sample_width
        if datalen != expected_len:
            print(f"Warning: expected {expected_len} bytes of audio data, but got {datalen}")
            raise Exception("Invalid audio data length")
        AudioSegment(data=binary_data, sample_width=2, frame_rate=44100, channels=1).export(output_audio_file, format="wav", bitrate="192k")

    @staticmethod
    def process_audio_to_text(input_audio_file):
        binary_data = AudioProcessor.audio_to_binary(input_audio_file)
        compressed_text_data = AudioProcessor.binary_to_text(binary_data)
        return compressed_text_data
        

if __name__ == "__main__":
    audio_processor = AudioProcessor()
    input_audio_file, output_audio_file = "Musica de 15 segundos.wav", "Musica de 15 segundos2.wav"

    # Procesar de audio a texto (compresión)
    compressed_text_data = audio_processor.process_audio_to_text(input_audio_file)
    print(f"Compressed text data: {compressed_text_data}")

    # Procesar de texto a audio (descompresión)
    binary_data = audio_processor.text_to_binary(compressed_text_data)
    audio_processor.binary_to_audio(binary_data, output_audio_file)
    print(f"Audio file saved to {output_audio_file}")