import base64

class VideoProcessor:
    @staticmethod
    def read_video(file_path):
            # Lee el archivo de video como una secuencia de bytes
            with open(file_path, 'rb') as f:
                video_data = f.read()      
            return video_data

    @staticmethod
    def write_video(file_path, video_data):
            # Guarda los datos descomprimidos en el archivo de video
            with open(file_path, 'wb') as f:
                f.write(video_data)
            
    @staticmethod        
    def binary_to_text(binary_data):
            return base64.b64encode(binary_data).decode()

    @staticmethod
    def text_to_binary(text):
        return base64.b64decode(text)